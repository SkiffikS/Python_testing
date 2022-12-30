# -*- coding: utf-8 -*-


import re


"""
# Дія 1. із сайту "https://uk.wikipedia.org/wiki/Львівський_трамвай" дістаю усі зупинки та записуємо їх у файл

# На момент створення програми файл мав наступні дані:
'''
Залізничний вокзал > Вул. Чернівецька > Приміський вокзал > Площа Кропивницького > Вул. Бандери > Вул. Коперника > Вул. Дорошенка > Вул. Беринди > Площа Ринок > Вул. Руська > Вул. Підвальна > Вул. Володимира Винниченка > Площа Митна > Вул. Личаківська > Вул. Мечникова > Личаківський цвинтар > Вул. Левицького > Погулянка.
Вул. Євгена Коновальця > Вул. Пасічна
Площа Соборна > Аквапарк
Залізничний вокзал - Городоцька - Пл. Кропивницького - Бандери - Русових - Київська - Котляревського - Нечуя-Левицького - Вітовського - Франка - Свєнціцького - Стуса - Червоної Калини - Вернадського.
Вул. Торфʼяна > Вул. Замарстинівська > Вул. Богдана Хмельницького > Площа Князя Ярослава Осмомисла > Вул. Івана Гонти > Площа Данила Галицького > Вул. Підвальна > Вул. Володимира Винниченка > Вул. Івана Франка > Вул. Дмитра Вітовського > Вул. Академіка Андрія Сахарова > Вул. Княгині Ольги
Залізничний вокзал > Вул. Миколайчука. Залізничний вокзал - Городоцька - Торгова - Хмельницького - Замарстинівська - Гайдамацька - Хмельницького (Підзамче) - Промислова - Миколайчука
Пасічна - Личаківська - Пл. Митна - Підвальна - Гонти - Торгова - Городоцька - Шевченка - Татарбунарська
Вернадського - Червоної Калини - Стуса - Свєнціцького - Франка - Пл. Соборна
Залізничний вокзал - Городоцька - Пл. Кропивницького - Бандери - Русових - Київська - Котляревського - Нечуй-Левицького - Вітовського - Франка - Винниченка - Підвальна - Гонти - Хмельницького - Замарстинівська - Торфʼяна
'''
f = open(r"All_stops.txt", "r", encoding="utf-8") # відкриваємо цей файл
text = f.read() # дістаємо увесь текст із файла
text = text.replace("\n", " - ") # заміняємо пропуски рядка
text = text.replace(" - ", " > ") # заміняємо символи для одного і зручного формату
text = text.replace("Вул. ", "Вул. ") # редагуємо дані під 1 фармат
text = text.replace("Площа ", "Площа ") # редагуємо дані під 1 фармат
text = text.replace("Площа ", "Пл. ") # редагуємо дані під 1 фармат
text_list = text.split(" > ") # створюємо список із усіх зупинок
text_list = list(set(text_list)) # видаляємо з списку елементи які повторяються
text_list = [elem.title() for elem in text_list] # усі назви робимо із великої букви
text_list = sorted(text_list) # сортуємо список за алфавітом
f.close() # закриваємо файл

file = open(r"All_stops_formate.txt", "w", encoding="utf-8") # відкриваємо новий файл
for i in text_list: # проходимось по списку зупинок
    file.write(f"{i}\n") # записуємо їх у файл

# після чого переглядаємо та мінімальне редагуємо файл і получаємо готовий список зупинок
"""


trams = {
    "1": ["Залізничний Вокзал", "Вул. Чернівецька", "Приміський Вокзал", "Пл. Кропивницького", 
        "Вул. Бандери", "Вул. Коперника", "Вул. Дорошенка", "Вул. Беринди", "Пл. Ринок", 
        "Вул. Руська", "Вул. Підвальна", "Вул. Володимира Винниченка", "Пл. Митна",
        "Вул. Личаківська", "Вул. Мечникова", "Личаківський цвинтар", "Вул. Левицького", 
        "Погулянка"],
    "2": ["Вул. Євгена Коновальця", "Вул. Пасічна"],
    "3": ["Пл. Соборна", "Аквапарк"], 
    "4": ["Залізничний вокзал", "Городоцька", "Пл. Кропивницького", "Бандери", "Русових",
        "Київська", "Котляревського", "Нечуя-Левицького", "Вітовського", "Франка",
        "Свєнціцького", "Стуса", "Червоної Калини", "Вернадського"],
    "5": ["Вул. Торфʼяна", "Вул. Замарстинівська", "Вул. Богдана Хмельницького",
        "Пл. Князя Ярослава Осмомисла", "Вул. Івана Гонти", "Пл. Данила Галицького",
        "Вул. Підвальна", "Вул. Володимира Винниченка", "Вул. Івана Франка",
        "Вул. Дмитра Вітовського", "Вул. Академіка Андрія Сахарова", "Вул. Княгині Ольги"],
    "6": ["Залізничний вокзал", "Городоцька", "Торгова", "Хмельницького", "Замарстинівська",
        "Гайдамацька", "Хмельницького (Підзамче)", "Промислова", "Миколайчука"],
    "7": ["Вул. Пасічна", "Личаківська", "Пл. Митна", "Підвальна", "Гонти", "Торгова",
        "Городоцька", "Шевченка", "Татарбунарська"],
    "8": ["Вернадського", "Червоної Калини", "Стуса", "Свєнціцького", "Франка", "Пл. Соборна"],
    "9": ["Залізничний вокзал", "Городоцька", "Пл. Кропивницького", "Бандери", "Русових", 
        "Київська", "Котляревського", "Нечуй-Левицького", "Вітовського", "Франка", "Винниченка", 
        "Підвальна", "Гонти", "Хмельницького", "Замарстинівська", "Торфʼяна"]
} # словник із трамваями та маршрутами


def get_tram_way(number_tram: str = "1") -> str:
    # функція яка дає шляї трамвая
    ways = trams[number_tram]
    result = ""

    for way in ways:
        result += f"{way} -> " # додаємо кожну зупинку у змінну шляху
    
    result = result[:-3] # обрізаємо кінець

    return result # повертаємо шлях


def return_route(number_tram: str = "1") -> list:
    # функція для получення зворотнього шляху
    ways = trams[number_tram] # получаємо список шляху
    return ways.reverse() # повертаємо перевернутий список


def check_is_in_this_route(route, start, end):
    # функція для перевірки чи є зупинки в 1 трамваї
    if start in route and end in route: # якщо так
        return True # повертаємо істинну
    else:
        return False


def make_route(trams_routes: dict, start: str, end: str) -> list: 
    # функція для пошуку шляху
    route = []
    buses = []

    for i in range(1, len(trams_routes)+1): # проходимось по усім трамваям
        item = trams_routes[str(i)]

        if check_is_in_this_route(item, start, end): # перевіряємо чи є шлях у 1 трамваї
            route.append(f"{i}: ")
            for i in range(item.index(start), item.index(end) + 1):
                route.append(item[i])
            return route # повертаємо результат

        if start in item: 
            buses.append(str(i)) # якщо ні у список додаємо трамвай

    for bus in buses: # проходимось по списку трамваїв
        broute = trams_routes[bus]

        for i in range(1, len(trams_routes) + 1):
            if bus != str(i):
                item = trams_routes[str(i)] # получаємо шляхи

                for station in item:
                    if station in broute and station in item and end in item and item != station: #
                        if broute.index(start) < broute.index(station)+1: #
                            route.append(f"{bus}: ") # додаємо у список шлях
                            for i in range(broute.index(start), broute.index(station)+1): #
                                route.append(broute[i]) #
                        else: #
                            route.append(f"{bus}: ")  # додаємо у список шлях
                            for i in range(broute.index(station)+1, broute.index(start)): #
                                route.append(broute[i]) #
                        if item.index(station) < item.index(end) + 1: #
                            route.append(f"{i}: ")  # додаємо у список трамвай
                            for i in range(item.index(station), item.index(end) + 1): #
                                route.append(item[i]) #
                        else: #
                            route.append(f"{i}: ")  # додаємо у список шлях
                            for i in range(item.index(end)+1, item.index(station)): #
                                route.append(item[i]) #
                        return route # повертаємо список


#print(make_route(trams, "Вул. Беринди", "Хмельницького"))


def check_message(message: str) -> str:

    #message = message.lower()

    #try: 
    trams_number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] # список трамваїв

    return_funk = "" # htpekmnfn

    stants = re.findall('"([^"]*)"', message) # шукаємо усі слова в лапках
    result = make_route(trams, stants[0], stants[1]) # шукаємо шлях по зупинках

    trams_numbers = []
    trams_index = []
    trams_stands = []

    for i in range(len(result)):
        if result[i].replace(": ", "") in trams_number_list:
            trams_numbers.append(result[i].replace(": ", "").title()) # збираєио список трамваїв
            trams_index.append(i) # збираємо індекси трамваїв
        else:
            trams_stands.append(result[i]) # збираємо список зупинок

    if len(trams_numbers) == 1: # якщо у нас 1 трамвай без пересадок
        tram = trams_numbers[0] # получаємо № трамваю

        question_answers = {
            "потрапити від на": f"Прийдіть на зупинку '{stants[0]}', сідайте на трамвай '{tram}' в напрямку '{trams_stands[0]} - {trams_stands[-1]}' Слухайте оголошення в трамваї про зупинку {stants[1]}!",
            "чи можна від на": f"Так, можна це зробити на трамваї №{tram}.",
            "cкільки від": f"{len(trams_stands)} зупинок без пересадки."
        } # словник із питаннями та відповідями по ключових словах

        for key, value in question_answers.items():
            if all(word in message.lower() for word in key.split(" ")):
                return_funk = value # повертаємо значення із словника
    
    elif len(trams_numbers) > 1: # якщо у нас є пересадки (2 або більше трамваї)

        res = ""
        for i in result:
            if i.replace(": ", "") in trams_number_list:
                res += f"трамвай {i.replace(': ', '')}"
            else:
                res += f" -> '{i}' "

        question_answers = {
            "потрапити від на": f"Прийдіть на зупинку '{stants[0]}', сідайте на {res}",
        } # відповідь на питання

        for key, value in question_answers.items():
            if all(word in message.lower() for word in key.split(" ")):
                return_funk = value # повертаємо змінну

    return return_funk # повертаємо значення функції

    #except:

        #return "На можу дати відповідь на ваше питання :("


"""
message = 'Як потрапити від "Промислова" на "Франка"'
file = open("results.txt", "a", encoding="utf-8")
file.write("------" * 10)
file.write("\n" + message + "\n\n")
file.write(check_message(message))
file.write("\n" + "------" * 10 + "\n\n")
"""

if __name__ == "__main__":

    message = input("Що хочете дізнатись?\n")
    print(check_message(message))