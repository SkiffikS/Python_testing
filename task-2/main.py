# -*- coding: utf-8 -*-

from datetime import datetime
from collections import Counter


# Наступні функції створенні для максимального заповнення файла із погодою
# ---------------------------------------------------------------------------------------------------------------------------------------------------
"""
import requests # pip install requests
from bs4 import BeautifulSoup as BS # pip install beautifulsoup4
def parse_synoptik(city: str = "київ") -> dict:
    # Функція щоб дістати усю інформацію про погоду вказаного міста
    try: # Обходимо усі можливі помилка
        city = city.lower() # Переписуємо усі букви у нижньому регістрі
        url = f"https://ua.sinoptik.ua/погода-{city}" # Створюємо силку на синоптик погоду міста

        r = requests.get(url) # переходимо за силкою
        html = BS(r.content, "html.parser") # получаємо HTML розмітку сторінки

        infoContainer = html.find("table", class_ = "weatherDetails") # Шукаємо таблицю із погодою
        oDescription = html.find("div", class_ = "oDescription") # Получаємо блок із текстовою інформаціює

        windspeed = infoContainer.findAll('tr')[7]

        speed_list = []
        for td in windspeed.find_all('td'):
            for td1 in td.findAll('div'):
                speed_list.append(td1["data-tooltip"][:-1])

        info = { # Словник із потрібною інформацією зручно розміщеною
            "city": city, # Назва міста
            "date": str(datetime.today().strftime("%Y-%m-%d")), # Дата інформації про погоду
            "gray_time": list(filter(None, infoContainer.find("tr", class_ = "gray time").text.replace(" :", ":").split(" "))), # періоди дня (у списку)
            "temperature": list(filter(None, infoContainer.find("tr", class_ = "temperature").text.split(" "))), # температура відповідно до періоду дня (у списку)
            "temperatureSens": list(filter(None, infoContainer.find("tr", class_ = "temperatureSens").text.split(" "))), # температура "відчувається як" (у списку)
            "gray": list(filter(None, infoContainer.findAll("tr", class_ = "gray")[1].text.split(" "))), # тиск повітря (у списку)
            "humidity": list(filter(None, infoContainer.findAll("tr")[6].text.split(" "))), # вологість у повітрі (у списку)
            "wind_speed": speed_list, # швидкість вітру (у списку)
            "probability_of_precipitation": list(filter(None, infoContainer.findAll("tr")[8].text.replace("-", "0").split(" "))), # ймовірність опадів (у %) (у списку)
            "description_1": html.findAll("div", class_="description")[0].text, # загальна інформація
            "description_2": html.findAll("div", class_="description")[1].text, # народний прогноз
            #"description_3": html.findAll("div", class_="description")[2].text, # інформація на рахунок грози
            #"description_4": html.findAll("div", class_="description")[3].text, # інформація про швидкість вітру
            "description_5": oDescription.find("div", class_="lSide").text # інформація про загальну погоду
        }
        
        #for key, value in info.items(): # проходимось по ключам та значенням 
            #print(f"{key}: {value}") # виводимо у зручному форматі

        return info # повертаємо словник із інформаацією

    except Exception as ex: # якщо сталась помилка

        print(f"Немає достатьно інформації по місту '{city}'") # виводимо інформацію та назву міста
        return None # повертаємо NoneType об'єкт


def dict_to_str(info: dict) -> str:
    # Функція для запису інформації із словника у файл
    try: # обходимо усі можливі помилки
        string_info = "" # змінна для уієї інформації

        for key, value in info.items(): # проходимось по кожному ключу та значенню словника
            
            if type(value) == list: # якщо тип значення список
                list_info = "" # змінна для інформації із списку
                for i in value: # проходимось по списку
                    list_info += str(f"{i}|") # додаємо у рядок інформацію про кожний елемент списку та форматуємо
                value = list_info[:-1] # видаляємо останній зайвий симлов
            
            if type(value) == int: # якщо об'єкт типу int
                value = str(value) # переводимо його у тип str
            
            string_info += f"{key} ::= {value}\n" # записуємо усю інфомацію у 1 стрічку

        return string_info # повертємо інформацію у вигляді стрічки

    except Exception as ex: # якщо сталась помилка
        print(f"Error: {ex}") # виводимо її значення


def formate_file(filepath: str = r"Weather_Info.txt"):
    # Функція яка додає інформацію у основний файл та форматує його
    open(filepath, "w", encoding="utf-8").close() # очищаємо файл перед повторним записом

    url = "https://uk.wikipedia.org/wiki/Міста_України_(за_алфавітом)" # силка на сайт у якому перелічені усі Українські міста у алфавітному порядка
    r = requests.get(url) # передаємо силку 
    html = BS(r.content, "html.parser") # получаємо HTML розмітку сторінки із містами

    citys = [] # створюємо список міст

    for table in html.findAll("tr"): # у загальній таблиці
        city = table.findAll("a")[1].text.replace(" ", "-") # шуккаємо тег у якому є назва маіста та перемо текст
        citys.append(city) # Назву міста додаємо у список міст

    del citys[0] # видаляємо перший елемент списку міст(зайве слово "Місто")
    citys = list(filter(None, citys)) # фільтруємо список, видаляємо непотрібні елементи

    separation = "-----" * 10 # рядок для форматування файла

    for city in citys: # проходимось по кожному місту із списку
        if type(parse_synoptik(city)) != None: # перевіряємо чи є інформація про місто у синоптику
            if dict_to_str(parse_synoptik(city)) != None: # перевіряємо чи ця інформація не є NoneType об'єкт
                f = open(filepath, "a", encoding="utf-8") # відкриваємо файл у якому буде інформація по кожному місту
                f.write(f"{city}\n{separation}\n{dict_to_str(parse_synoptik(city))}{separation}\n\n") # записуємо інфомацію і форматуємо файл
"""
# ---------------------------------------------------------------------------------------------------------------------------------------------------

def cytys(filepath: str = r"Weather_Info.txt") -> list:
    # Функція для получення списку назв усіх міст у файлі
    f = open(filepath, "r", encoding="utf-8") # відкриваємо файл для читання
    s = f.read() # читаємо весь файл в 1 змінну

    start = "city ::= " # початкова точка пошуку
    end = "\ndate ::=" # кінцева точка пошуку
    result = [] # список із результатами
    tmp = s.split(start) # список від початкової точки

    for par in tmp: # проходимось по цьому списку
        if end in par: # знаходимо кінцеву точку у рядку
            result.append(par.split(end)[0]) # додаємо результат у список

    return result # повертаємо результат


def read_data(filepath: str = r"Weather_Info.txt") -> str: 
    # Функція для читання назв міст та їхгьої погодньої інформації
    f = open(filepath, "r", encoding="utf-8") # відкриваємо файл для читання
    s = f.read() # читаємо  весь файл в одну змінну

    result = s.split("--------------------------------------------------") # створюємо список із містами та погодами

    return result # повертаємо список


def read_city(city: str = "Київ") -> dict:
    # Функція для читання погоди у вказаному місці
    data = read_data() # читаємо усб інформацію із файла
    city = city.lower() #
    city = city.title() # міняємо регістри на потрібні

    city_index = -1 # створюємо неможливий індекс

    for i in range(len(data)): # проходимось по списку міст і погод
        if data[i].replace("\n", "") == city: # перевіряємо чи існує таке місто
            city_index = i + 1 # якщо так, то беремо індекст погоди

    info = data[city_index] # за індексом погоди дістаємо інформацію про погоду
    info = info[1:-1] # обрізаємо непотрібні символи
    #print(info)

    variables = {} # словник у який будемо додавати числа

    for line in info.splitlines(): # читаємо кожну лінію
        #line = line.replace(" ", "") # заміняємо можливі пробіли у файлі
        name, value = line.split(" ::= ") # читаємо змінні таким чином що зліва знака "::=" назва змінної, а з права її значення
        if value.find("|") >= 0: # якщо символи розділені таким чином
            value = value.split("|") # робимо список
        variables[name] = value # поміщаємо ці змінні у словник

    return variables # повертаємо словник із інформацією про погоду


def task_1(city: str = "Київ") -> str: 
    # Задача 1: просто відобразити матеодані заданого міста
    city = city.lower()
    #city = city.title()

    all_cytys = cytys() # список усіх міст

    Existing_city = False #

    for i in all_cytys: # проходимось по списку міст
        if i == city: # якщо наше місто є у ньому
            Existing_city = True # задаємо True
    
    if Existing_city != True: # Якщо такого міста немає
        
        print(f"Такого міста не має у списку!\nсписок міст:\n{all_cytys}") # виводимо відповідну інформацію
        return "" # повертаємо пустий рядок
        
    else: # якщо таке місто існує у нашому файлі

        info = read_city(city) # читаємо інформацію про місто

        return_info = "----------------------------------------------------------------------------------------\n" # форматуємо

        for key, value in info.items(): # проходимось по ключам та значенням 
            if key == "city": return_info += f"|Місто: {value}\t\n" # виводимо інформацію по ключам
            if key == "date": return_info += f"|Дата: {value.title()}\n" #
            if key == "gray_time": return_info += f"|Періоди дня: {' / '.join(str(x) for x in value)}\n" #
            if key == "temperature": return_info += f"|Температура повітря: {' / '.join(str(x) for x in value)}\n" #
            if key == "temperatureSens": return_info += f"|Температура відчувається як: {' / '.join(str(x) for x in value)}\n" #
            if key == "gray": return_info += f"|Тиск: {' / '.join(str(x) for x in value)}\n" #
            if key == "humidity": return_info += f"|Вологість: {' / '.join(str(x) for x in value)}\n" #
            if key == "wind_speed": return_info += f"|Швидкість вітру: {' / '.join(str(x) for x in value)}\n" #
            if key == "probability_of_precipitation": return_info += f"|Ймовірність опадів: {' / '.join(str(x) for x in value)}\n" #
            if key == "description_1": return_info += f"|Загальна інформація: {value}\n" #
            if key == "description_2": return_info += f"|{value}\n" #
            if key == "description_3": return_info += f"|{value}\n" #
            if key == "description_4": return_info += f"|{value}\n" #
            if key == "description_5": return_info += f"|{value}\n" #

    return return_info + "----------------------------------------------------------------------------------------" # форматуємо


def task_2() -> str:
    # задача 2: в якому місті найвища/найнижча температура;
    try: # блок у якому може статись помилка

        all_cytys = cytys() # список усіх міст

        max_temperature = -999 # найбільша температура
        max_temperature_cyty = "" # місто із найбільшою температурою

        min_temperature = 999 # найнижча температура
        min_temperature_cyty = "" # місто із найменшою температурою

        for city in all_cytys: # проходимось по усіх містах із списку
            info = read_city(city) # беремо інформацію по кожному місту
            for key, value in info.items(): # проходимось по словнику із інформацією про погоду
                if key == "temperature": # дістаємо значення температури
                    temperatures = value #
                    temperatures_int = [] # список цифр температур
                    for temperature in temperatures: #
                        temperature = temperature.replace("+", "") #
                        temperature = temperature.replace("°", "") # заміняємо зайві символи щоб дістати числло
                        temperatures_int.append(int(temperature)) # число поміщаємо у список

                    max_temp_i = max(temperatures_int) # максимальне число в списку температур
                    min_temp_i = min(temperatures_int) # мінімальне число в списку температур

                    if max_temp_i > max_temperature: # алгоритм пошуку найбільшого чисоа
                        max_temperature = max_temp_i #
                        max_temperature_cyty = city #

                    if min_temp_i < min_temperature: # алгоритм пошуку найменшого чисоа
                        min_temperature = min_temp_i #
                        min_temperature_cyty = city #
    except: # обходимо помилка
        pass # пропускаємо дію якщо сталась помилка

    result = f"Максимальна температура виявлена у місті '{max_temperature_cyty.title()}' ({max_temperature}°C)\n" #
    result += f"Мінімальна температура виявлена у місті '{min_temperature_cyty.title()}' ({min_temperature}°C)" #

    return result # повертаємо відформатовану інформацію


def wind_city_info(city: str = "Київ") -> str:
    # Функція для визначення основного напрямку вітру у місті
    try: # блок із можливою помилкою
        city = city.lower() #

        winds = ["півнійчний", "півнійчний", "східний", "західний", "південно-західний", "південно-східний", "північно-західний", "північно-східний"]
        # список усіх напрямків вітру (як у синоптику)

        info = read_city(city) # інформація про місто

        winds_info = info["wind_speed"] # інформація про вітер у місті
        winds_info = " ".join(str(x) for x in winds_info) # перетворюємо список із інформацією про усі вітри у рядок
        winds_info = winds_info.lower() # форматуємо
        winds_info = winds_info.replace(",", "") # заміняємо непотрібні символи
        winds_info = winds_info.split(" ")  # перетворюємо назад у списко
        counter = Counter(winds_info) # додаємо список у модуль collections
        winds_info_list = counter.most_common() # получаємо найпопулярніше слово і як часто воно зустрічається

        #print(winds_info_list)

        more_wind = "" 

        for wind_info in winds_info_list: # проходимовсь по писку напрямку вітру і його кількості повторянь
            for wind in winds: # проходимось по нашому списку напрямку вітрів
                if wind_info[0] == wind: # перевіряємо найпопулярніший варіант
                    more_wind = wind # якщо такий варіант є у списку вітрів
                    break # зупиняємо цикл
            if more_wind != "": # якщо змінна напрямку вітру не пуста
                break # зупиняємо другий цикл

        return more_wind # повертаємо напрямок вітру
    
    except Exception as ex: # обходимо помилкми
        pass #  пропускаємо дію
        return "" # повертаємо пустий рядок


def task_3(city: str = "Київ") -> str:

    city = city.lower() #
    info = read_city(city) # получаємо інфу про погоду у місті
    temperatures_info = info["temperature"] # получаємо інфу про температуру у місті
    time_info = info["gray_time"] # получаємо список часу

    result = "-----" * 6 # Форматуємо
    result += "\n|  Час: |    Температура:   |\n" # Форматуємо
    result += "-----" * 6 + "\n" # Форматуємо

    for i in range(len(time_info)): # проходимось по списку чату і температур
        result += f"|{time_info[i]}\t|\t{temperatures_info[i]}\t    |\n" # додаємо в табличку та форматуємо
        result += "-----" * 6 + "\n" # Форматуємо

    return result[:-1]


def task_4(city_list: list = cytys()) -> str:
    # Задача 4: динаміка зміни температури в зазначеному місті протягом дня;
    try: #
        windths_city = [] # список із найпопулярнішим напрямком вітру у 1 місці

        for city in city_list: # проходимось по кожному місці із заданого списку 
            wind_info = wind_city_info(city) # получаємо інформацію про напрямок вітру у цьому місті
            if wind_info != "": # якщо він не пустий
                windths_city.append(wind_info) # додаємо його у основний список

        counter = Counter(windths_city) # із основного списку (1 місто - 1 напрямок вітру)
        winds_info_list = counter.most_common() # дістаємо самий популярний варіант серед усіх міст
        #print(winds_info_list)
    except: #
        pass #

    return f"У цьому списпку міст вітер переважно '{winds_info_list[0][0]}'" # повертаємо відформатований результат


def task_5(t: int = 10) -> str:
    # Задача 5: де температура менша від t – тобто, де настало похолодання.
    try: #
        all_cytys = cytys() # усі міста

        result_citys = [] # список результатів

        for city in all_cytys: # проходимось по кожному місту

            info = read_city(city) # получаємо інфу про погоду у місті
            temperatures_info = info["temperature"] # получаємо інфу про температуру у місті
            temperature_info = temperatures_info[0] # вибираємо перший показник
            temperature_info = temperature_info.replace("+", "") # 
            temperature_info = temperature_info.replace("°", "") # заміняємо непотрібні символи
            temperature_info = int(temperature_info) # перетворюємо температуру у число
            #print(temperature_info)

            if temperature_info < t: # перевіряємо чи це число не менше за задане
                result_citys.append(info["city"]) # якщо менше поміщаємо назву міста у список

    except: #
        pass #

    return f"Міста у яких температура менша за {t}°:\n{result_citys}" # повертаємо результат


def main(filepath: str = r"Results.txt"): 
    # Основна функція для запису інформації у файл
    f = open(filepath, "w").close() # стераємо попередню інформацію із файла

    format = "----------" * 10 # рядок для форматування

    f = open(filepath, "a", encoding="utf8") # відкриваємо файл для запису
    f.write(f"task_1\n{format}\n{task_1()}\n{format}\n\n") # записуємо та форматуємо кожну функцію
    f.write(f"task_2\n{format}\n{task_2()}\n{format}\n\n")
    f.write(f"task_3\n{format}\n{task_3()}\n{format}\n\n")
    f.write(f"task_4\n{format}\n{task_4()}\n{format}\n\n")
    f.write(f"task_5\n{format}\n{task_5()}\n{format}\n\n")


"""
зберегти структуру файла можна завдяки модулю pickle
якщо загружати дані у файл функцією pickle.dump(data, file)
і вигружати інформацію через pickle.load(file)
"""

if __name__ == "__main__": # початок виконання програми
    main() # виконуємо основну функцію