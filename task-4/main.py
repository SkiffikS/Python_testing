# -*- coding: utf-8 -*-


import re


class Stack:
    # Клас стека
    def __init__(self):
        self.elements = [] # ініціалізація змінної стека

    def push(self, data):
        self.elements.append(data) # додавання зміної у стек

    def pop(self): # видалення елемента із стеку
        if self.elements:
            return self.elements.pop()
        else:
            return None

    def size(self): # довжина стеку
        return len(self.elements)

    def empty(self): # перевірка чи сте не пустий
        return True if self.size() == 0 else False

    def peek(self): # останній елемент стеку
        return self.elements[-1]

    def string(self): # перетворення стеку у рядок
        return "".join(str(elem) for elem in self.elements)

    def clear(self): # очищення стеку
        self.elements = []


    def task_1(self): # задача 1

        s = self.string() # рядок стеку
        toret = {} # словник із дужками
        pstack = []

        for i, c in enumerate(s):
            if c == "(": # перевіряємо чи є відкрита дужка
                pstack.append(i) # додаємо у список
            elif c == ")": # перевіряємо чи є відповідна закриваюча дужка
                if len(pstack) == 0: # якщо немає
                    return f"\nНемає відповідної закриваючої дужки для: {i}"
                toret[pstack.pop()] = i # якщо є додаємо пару дужок у словник

        if len(pstack) > 0: # якщо список відкриваючих дужок пустий
            return f"\nНемає відкриваючої дужки для: {pstack.pop()}"

        #return toret
        result_string = ""
        opening_brackets = [] # списки для сортування дужок
        closing_brackets = []

        for key, value in toret.items():
            
            opening_brackets.append(key) #
            closing_brackets.append(value) # заповнюємо списки

            #result_string += f"\n({key} -> {value})"

        #return result_string

        result_string += "\nПари дужок у порядку зростання відкриваючих дужок: "
        opening_brackets = sorted(opening_brackets) # сортуємо список у порядку зростання відкриваючих дужок

        for i in opening_brackets: # проходимось по списку
            for key, value in toret.items(): # проходимось по словнику
                if i == key: # шукаємо відповідну пару
                    result_string += f"\n({i} -> {value})" # виводимо

        result_string += "\nПари дужок у порядку зростання закриваючих дужок: "
        closing_brackets = sorted(closing_brackets) # це ж саме у порадку зростання закриваючої

        for i in closing_brackets: #
            for key, value in toret.items(): #
                if i == value: #
                    result_string += f"\n({key} -> {i})"

        return result_string # повертаємо результат у вигляді рядка


    def task_2(self):

        string = self.string() 
        string = string.replace(" ", "")
        string = string.replace("::=", "=") # форматуємо ряд

        def check_balance():
            # функція для перевірки балансу формули
            expression = string
            open_tup = tuple('({[')
            close_tup = tuple(')}]') # список із відкриваючими та закриваючими дужками
            map = dict(zip(open_tup, close_tup)) #
            queue = []

            for i in expression: # проходимось по рядку
                if i in open_tup:
                    queue.append(map[i])
                elif i in close_tup: # перевіряємо на дужки
                    if not queue or i != queue.pop():
                        return "\nФормула несбалансована"
            if not queue: # повертаємо відповідні результати
                return "\nПідходяща формула"
            else:
                return "\nФормула несбалансована"

        if not string: # повертаємо помилку якщо дані не коректні
            return "\nНеправильний формат формули"

        brackets = ["(", ")", "{", "}", "[", "]"]
        if any(s in string for s in brackets): # перевіряємо чи є дужки
            if check_balance() == "Формула несбалансована":
                return "Формула несбалансована" # перевіряємо на баланс дужок
 
        string = re.sub("[^0-9+*/%-=]", "", string) # шукаємо потрібні символи
        
        try:
            string, result = string.split("=")
            return f"\nРезультат обчислення формули:\n{eval(result)}" # повертаємо результат

        except:
            return "\nФормула правильна, але обрахувати результат неможливо"


    def task_3(self): 
        # задача 3
        def find_between_r(s, first, last):
            try: # функція для пошуку формули у рядку
                start = (s.rindex(first) + len(first))-2
                end = s.index(last, start) + 1
                return s[start:end] # повертаємо рядок
            except ValueError:
                return ""#

        try:
            all_string = self.string()
            all_string = all_string.replace(" ", "")
            all_string = all_string.replace("=", "::=") #
            string_1 = all_string.split("::=")[0]
            string = all_string.split("::=")[1] # формутуємо ряд

            def S(x): # функція суми
                numbers = re.findall(r"\d+", x)
                numbers = [int(x) for x in numbers]
                return sum(numbers)

            def D(x): # функція ділення
                numbers = re.findall(r"\d+", x)
                numbers = [int(x) for x in numbers]
                #print(numbers)
                return numbers[0] / numbers[-1]

            S_start = "S(" #
            S_end = ")" # символи функції суми

            while S_start in string: # проходимоь по усіх формулах суми рядка та заміняємо не результат
                S_result = find_between_r(string, S_start, S_end)
                #print(S_result)
                string = string.replace(S_result, f"{S(S_result)}")

            D_start = "D(" #
            D_end = ")"

            while D_start in string:  # проходимоь по усіх формулах ділення рядка та заміняємо не результат
                D_result = find_between_r(string, D_start, D_end)
                #print(D_result)
                string = string.replace(D_result, f"{D(D_result)}")
            
            return f"\n{string_1} = {eval(string)}" # повертаємо розрахунок

        except: # повертаємо негативний результат
            return f"\nНеправильна формула"


def tasker_1():
    # функції для розв'язку та запису у файл
    decided_1 = Stack()

    info_file = open(r"inData_1.txt", "r", encoding = "utf-8")
    info_list = info_file.read().split("\n")
    info_file.close()
    
    result_file = open(r"Result.txt", "a", encoding = "utf-8")
    result_file.write(f"Задача 1\n{'----------' * 50}\n")

    for example in info_list:
        #example = example.replace(" ", "")
        example_sybmols = list(example)

        for sybmol in example_sybmols:
            decided_1.push(sybmol)

        result = decided_1.task_1()
        result_file.write(f"\nПриклад:\n{example}\nРішення:{result}\n\n")
        
        decided_1.clear()
    
    result_file.write('----------' * 50)
    result_file.close()


def tasker_2():

    decided_2 = Stack()

    info_file = open(r"inData_2.txt", "r", encoding="utf-8")
    info_list = info_file.read().split("\n")
    info_file.close()

    result_file = open(r"Result.txt", "a", encoding="utf-8")
    result_file.write(f"\n\n\nЗадача 2\n{'----------' * 50}\n")

    for example in info_list:
        #example = example.replace(" ", "")
        example_sybmols = list(example)

        for sybmol in example_sybmols:
            decided_2.push(sybmol)

        result = decided_2.task_2()
        result_file.write(f"\nПриклад:\n{example}\nРішення:{result}\n")

        decided_2.clear()

    result_file.write('----------' * 50)
    result_file.close()


def tasker_3():

    decided_3 = Stack()

    info_file = open(r"inData_3.txt", "r", encoding="utf-8")
    info_list = info_file.read().split("\n")
    info_file.close()

    result_file = open(r"Result.txt", "a", encoding="utf-8")
    result_file.write(f"\n\n\nЗадача 3\n{'----------' * 50}\n")

    for example in info_list:
        #example = example.replace(" ", "")
        example_sybmols = list(example)

        for sybmol in example_sybmols:
            decided_3.push(sybmol)

        result = decided_3.task_3()
        result_file.write(f"\nПриклад:\n{example}\nРішення:{result}\n")

        decided_3.clear()

    result_file.write('----------' * 50)
    result_file.close()

    
def main():
    # основна функція запису у файл всіх результатів
    f = open(f"Result.txt", "w", encoding="utf-8").close()
    tasker_1()
    tasker_2()
    tasker_3()


if __name__ == "__main__":

    main() # початок виконання программи, виклик основної функції