import random
import sympy
import math
from collections import namedtuple
from hashlib import sha256
from rich import print

"""
Алгоритм дуже короткий і простий. Починаючи з зерна, наступний стан можна обчислити, передавши поточний стан через наступну формулу.

f(x) = x^2 mod(M)

У цій формулі M є добутком p і q , двох великих простих чисел.

Складність цього алгоритму прихована в параметрах; початковий елемент і модуль M  Щоб мати тривалий цикл і виконувати свої обіцянки щодо безпеки, Blum Blum Shub має кілька обмежень щодо своїх параметрів.
Навпаки, деякі складніші алгоритми PRNG можуть працювати майже з будь-яким рандомізованим початковим числом.
"""

"""
Обмеження:
1. Початковий код має бути співпростим для (p і q) . Це означає, що їхній найбільший спільний дільник має бути 1.
2. (p і q) мають відповідати "3 (mod 4)". Це означає, що (p % 4) обидва (q % 4) мають бути "3".
3. (p і q) мають бути безпечними простими числами.
"""


"""
Перш ніж належним чином реалізувати алгоритм, я збираюся пограти з прикладами значень і подивитися, як поводиться функція. Згодом я об’єднаю наші відкриття в більш корисні методи.
Почнемо з однозначного перекладу попередньої формули.
"""
def blum_blum_shub(x, m):
    return (x * x) % m


# Початкові параметри:
P = 11
Q = 23
M = P * Q
urandom = random.randint(0, 256)
seed = 3 

x = seed

# Цифри дуже малі, що призводить до дуже короткого циклу з 20 елементів.
print("[bold red]Результат попередньої формули:[/bold red]")
for _ in range(21):
    x = blum_blum_shub(x, M)
    print(x, end=" ")

# result:
# 9 81 236 36 31 202 71 234 108 26 170 58 75 59 192 179 163 4 16 3 9
print("")

x = seed

print("[bold red]Результат попередньої формули побітово:[/bold red]")
# Замість використання повного стану ми будемо брати один біт з кожної ітерації.
for i in range(21):
    x = blum_blum_shub(x, M)
    bit = x & 1
    print(bit, end="")

# result
# 110010100000110110011
print("")

# Клас алгоритму
class BlumBlumShub:
    def __init__(self, seed, mod):
        self.x = seed
        self.mod = mod

    def next_state(self):
        self.x = pow(self.x, 2, self.mod)
        return self.x


bbs = BlumBlumShub(seed, M)
print("[bold red]Результат формули використовуючи класс:[/bold red]")
for _ in range(21):
    print(bbs.next_state(), end=" ")

# result:
# 9 81 236 36 31 202 71 234 108 26 170 58 75 59 192 179 163 4 16 3 9
print("")

#Тепер ми можемо додати наших помічників для генерування бітів і байтів із цього потоку чисел.
class BlumBlumShub(BlumBlumShub):
    def next_bit(self):
        return self.next_state() & 1

    def next_byte(self):
        byte = 0

        for _ in range(8):
            byte <<= 1
            byte |= self.next_bit()

        return byte

    def buffer(self, size):
        buf = bytearray(size)

        for i in range(size):
            buf[i] = self.next_byte()

        return buf


bbs = BlumBlumShub(seed, M)
print("[bold red]Результат у шіснадцятковому вигляді:[/bold red]")
print(f"[green]{bbs.buffer(64).hex()}[/green]")

# result:
# ca0d9ca0d9ca0d9ca0d9ca0d9ca0d9ca0d9ca0d9ca0d9ca0d9ca0d9ca0d9ca0d9ca0d9ca0d9ca0d9ca0d9ca0d9ca0d9ca0d9ca0d9ca0d9ca0d9ca0d9ca0d9ca0


"""
Вибір параметрів
RNG не дуже корисний, якщо ми не можемо генерувати різні потоки чисел. Щоб це зробити, нам потрібно згенерувати параметри M і seed .

Для деяких алгоритмів PRNG ви можете вибрати їх як уніфіковані випадкові значення. Але Blum Blum Shub має додаткові вимоги, про які йдеться в розділі «Обмеження».
"""
def random_int(rng, bits):
    size = int(bits / 8)
    buf = [random.randint(0, 255) for _ in range(size)]
    buf = bytes(buf)
    return int.from_bytes(buf, 'big')


def random_prime(rng, bits):
    n = random_int(rng, bits)
    n = sympy.nextprime(n)
    return int(n)


def get_safe_prime(rng, bits):
    while True:
        n = random_prime(rng, bits)
        n = 2 * n + 1
        if sympy.isprime(n):
            return n


def get_suitable_prime(rng, bits):
    while True:
        n = get_safe_prime(rng, bits)
        if n % 4 == 3:
            return n


print("[bold red]Результат функції підбору параметрів:[/bold red]")
print(get_suitable_prime(urandom, 128))

# Получаємо сід
def pick_seed(p, q, rng, bits):
    while True:
        n = random_int(rng, bits)

        if n == 0 or n == 1:
            continue

        if math.gcd(n, p) == 1 and math.gcd(n, q) == 1:
            return n

p = get_suitable_prime(urandom, 128)
q = get_suitable_prime(urandom, 128)
#print(pick_seed(p, q, urandom, 128))


Parameters = namedtuple("Parameters", "p q n x")


def get_parameters(rng, bits):
    p = get_suitable_prime(rng, bits)
    q = get_suitable_prime(rng, bits)
    m = p * q

    seed = pick_seed(p, q, rng, bits)
    return Parameters(p, q, m, seed)


print("[bold red]Збираємо все в 1 об'єкт:[/bold red]")
print(get_parameters(urandom, 32))


def keyed_rng(key):
    i = 0

    def inner():
        nonlocal i
        buf = key + i.to_bytes(3, 'big')
        h = sha256(buf)
        i += 1
        return h[0]

    return inner


def get_key(x):
    start_state = 1 << 7 | 1
    lfsr = start_state
    period = 0

    while True:
        #taps: 16 15 13 4; feedback polynomial: x^8 + x^5 + x^3 + x^2 + 1
        bit = (lfsr ^ (lfsr >> 1) ^ (lfsr >> 2) ^ (lfsr >> 4)) & 1
        lfsr = (lfsr >> 1) | (bit << 7)
        period += 1
        if (lfsr == start_state):
            return period


rng = keyed_rng(get_key(x))

#print(bytes([random.randint(0, 256) for _ in range(32)]).hex())


def encrypt(key, data):
    rng = keyed_rng(key)
    params = get_parameters(rng, 256)
    bbs = BlumBlumShub(params.x, params.n)

    res = bytearray(len(data))

    for i, c in enumerate(data):
        res[i] = c ^ bbs.next_byte()

    return data


print(f"\n[bold blue]Шифрування та дешифрування речення:[/bold blue]")
plaintext = b"Blum Blum Shub."
print(f"[bold yellow]Речення:[/bold yellow] [italic green]{plaintext}[/italic green]")
ciphertext = encrypt(get_key(urandom), plaintext)
print(f"[bold yellow]Шифруємо речення:[/bold yellow] [italic green]{ciphertext.hex()}[/italic green]")
print(f"[bold yellow]Скремблер:[/bold yellow] [italic green]x^8 + x^5 + x^3 + x^2 + 1[/italic green]")
print(f"[bold yellow]Параметри:[/bold yellow] [italic green]{get_parameters(ciphertext, 32)}[/italic green]")
decrypt = encrypt
print(f"[bold yellow]Дешифроване речення:[/bold yellow] [italic green]{decrypt(get_key(urandom), ciphertext)}[/italic green]")