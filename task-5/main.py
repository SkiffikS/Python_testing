# -*- coding: utf-8 -*-

avtonn = {
    "auto": "BMW",
    "number": "BC4684CO",
    "owner": "ITstep",
    "data": "02:08:2020",
    "on": "Germany, Berlin",
    "to": "Ukraine, Lviv",
    "goods": {"tires": 10, "motor oil": 100},
    "carriage_contack": True,
    "other": ["insurance", "guarantee"]
} # Стандартний шаблон

litkey = ["auto", "number", "owner", "data", "on", "to", "goods", "carriage_contack", "other"] # Шаблон ключів

data1 = ["Mercedes-benz С63", "AA1804AO", "Green day", "10:07:2018", "Germany, Berlin", "Ukraine, Kyiv", {"tires": 10, "motor oil": 100}, False, ["insurance", "guarantee"]]
data2 = ["Nissan Skyline", "47-35", "R-company", "05:15:2003", "Japan, Kioto", "Ukraine, Lviv", {"motor oil": 340}, False, ["insurance", "guarantee"]]
data3 = ["Toyota Supra", "12-34", "CarWow", "00:00:2006", "Japan, Yamanasi", "Ukraine, Rivne", {"tires": 19, "motor oil": 380}, True, ["guarantee"]]
data4 = ["Mazda RX-7", "44-77", "JDM club", "22:44:2002", "Japan, Tokyo", "Poland, Lublin ", {"tires": 13}, False, ["insurance", "guarantee"]]
data5 = ["Honda Civic", "61-65", "MMN-s", "20:04:2010", "Japan, Fudzi", "Germany, Belril", {"tires": 15, "motor oil": 305}, True, ["insurance"]]
data6 = ["Nissan Silvia", "42-10", "IsUMN", "18:24:1999", "Japan, Hamatsu", "Litva, Riga", {"tires": 16, "motor oil": 200}, False, ["insurance", "guarantee"]]
data7 = ["Toyata Chaser", "00-00", "DRFT", "12:00:1980", "Japan, Toyota", "Chehiya, Praha", {"tires": 16}, True, ["insurance", "guarantee"]]
data8 = ["Nissan GT-R", "41-20", "OBAM", "22:00:2022", "Japan, Ati", "France, Lion", {"tires": 20, "motor oil": 1100}, False, ["insurance", "guarantee"]]
data9 = ["Subaru WRX STI", "02-10", "STI wwo", "22:00:2010", "Japan, Nambu", "France, Paris", {"tires": 19, "motor oil": 250}, True, ["guarantee"]]
data10 = ["Subaru Impreza", "02-10", "Empire", "02:00:2011", "Japan, Toyohasi", "Italy, Roma", {"tires": 16, "motor oil": 451}, True, ["insurance"]]
data11 = ["Nissan 370Z", "11-10", "Z-jdm", "10:21:2001", "Japan, Takamori", "Italy, Milano", {"tires": 19, "motor oil": 1900}, False, ["insurance", "guarantee"]]
data12 = ["Lexus RC F", "10-95", "OHAyo", "20:20:2014", "Yapan, Kiso", "Afrika, Niger", {"tires": 16}, True, ["guarantee"]]
data13 = ["Mazda MX-5", "51-11", "MX=Xm1r", "10:00:2016", "Japan, Isikava", "Chehiya, Brno", {"motor oil": 640}, True, ["insurance"]]
data14 = ["Infiniti Q60 Red Sport 400", "12-60", "DPD-cobra", "12:00:2012", "Japan, Omati", "Ukraine, Lutsk", {"motor oil": 510}, False, ["insurance", "guarantee"]]
data15 = ["Mitsubishi Lancer Evo VII", "11-11", "Evo-company", "22:20:2020", "Japan, Hida", "Poland, Wrotslav", {"tires": 19, "motor oil": 3210}, True, ["guarantee"]]
data16 = ["Honda NSX", "51-99", "BAYD-n", "20:00:2021", "Yapan, Hakuba", "Ukraine, Odesa", {"tires": 16, "motor oil": 2500}, True, ["guarantee"]]
# Шаблони значень автомобілів

auto1 = dict(zip(litkey, data1)) # Перетворюємо шаблони у потрібний формат
auto2 = dict(zip(litkey, data2))
auto3 = dict(zip(litkey, data3))
auto4 = dict(zip(litkey, data4))
auto5 = dict(zip(litkey, data5))
auto6 = dict(zip(litkey, data6))
auto7 = dict(zip(litkey, data7))
auto8 = dict(zip(litkey, data8))
auto9 = dict(zip(litkey, data9))
auto10 = dict(zip(litkey, data10))
auto11 = dict(zip(litkey, data11))
auto12 = dict(zip(litkey, data12))
auto13 = dict(zip(litkey, data13))
auto14 = dict(zip(litkey, data14))
auto15 = dict(zip(litkey, data15))
auto16 = dict(zip(litkey, data16))

car_list = [avtonn, auto1, auto2, auto3, auto4, auto5, auto6, auto7, auto8, auto9, auto10, auto11, auto12, auto13, auto14, auto15, auto16]
# Збираємо усі авто в один список

winners = [] # Список авто що перетнули кордон


class Turn:
    # Основний клас черги
    def __init__(self) -> None:
        "Функція для ініціалізації змінних"
        self.turn_list = [] # Спиок звичайної черги
        self.green_turn_list = [] # Список зеленої черги

    
    def get_info(self, auto: dict) -> str:
        "Функція для получення інформації про автомобіль у зручному вигляді"
        result = "" # Змінна для кінцевого результату

        for key, value in auto.items(): # Проходимовсь по елементах списку
            if key == "auto": # проходимось по ключах
                result += f"Автомобіль: {value};\n" # доавляємо значення ключа у зручному форматі
            if key == "number":
                result += f"Номерний знак: {value};\n"
            if key == "owner":
                result += f"Замовник компанія: {value};\n"
            if key == "data":
                result += f"Машину випущено {value} року;\n"
            if key == "on":
                result += f"Машина відправляється від '{value}' до "
            if key == "to":
                result += f" '{value}';\n"
            if key == "goods":
                result += f"інші товари: {value}\n"
            if key == "carriage_contack":
                if value == True:
                    result += f"Договір перевезення присутній;\n"
                elif value == False:
                    result += f"Договір перевезення відсутній!!!\n"
                else:
                    result += "Не має інформації по договіру перевезення!\n"
            if key == "other":
                outher = " ".join([str(elem) for elem in value])
                result += f"В машині також знаходились наступні речі:\n{outher};\n"

        return result # повертаємо результат

    def get_all_info(self) -> str:
        "Функція яка надає інформацію про всі автомобілі у всіх чернах"
        turn = self.turn_list + self.green_turn_list
        result = ""

        for car in turn:
            result += f"{self.get_info(car)}\n"

        return result

    def add_auto_to_turn(self, auto: dict) -> None:
        "Функція яка додає авто до звичайної черги"
        self.turn_list.append(auto)

    def add_auto_to_green_turn(self, auto: dict) -> None:
        "Функція яка додає авто до зеленої черги"
        self.green_turn_list.append(auto)

    def get_turn_lenght(self) -> int:
        "Функція яка дає кількість автомобілів звичайної черги"
        return len(self.turn_list)
    
    def get_green_turn_lenght(self) -> int:
        "Функція яка дає кількість автомобілів зеленої черги"
        return len(self.green_turn_list)

    def get_number_cars(self) -> str:
        "Функція яка дає всі авто і їх номера"
        turn = self.turn_list + self.green_turn_list # Получаємо повний список авто із 2 черг

        result = ""

        for auto in turn: # Проходимось по кожному авто
            car = auto["auto"] # Получаємо модель авто
            number = auto["number"] # Получаємо номер авто

            result += f"Авто - {car}, номер: {number}\n"  # Додаємо в Результат

        return result  # Повертаємо результат

    def miss_the_car_in_turn(self, number: str) -> str:
        "Функція яка пропускає авто через кордон зі звичайної черги (по номеру автомобіля)"
        index_car = -1  # Створюємл нереальний індекс

        for car in range(len(self.turn_list)): # Проходимся по індексах авто
            for key, value in self.turn_list[car].items():  # Проходимось по словнику
                if value == number:
                    index_car = car  # Повертаємо індекс авто із потрібним номером

        if index_car == -1:
            return f"У списку не має авто із номером {number}"
            
        else:
            result = f"Авто №{index_car} пропущено через кордон;\nІнформація про авто:\n{self.get_info(self.turn_list[index_car])}"
            winners.append(self.turn_list[index_car]) # Додаємо авто у список автомобілів які перетнули кордон
            del self.turn_list[index_car]  # Видаляємо авто із списку
            return result

    def miss_the_car_in_green_turn(self, number: str) -> str:
        "Функція яка пропускає авто через кордон зі зеленої черги (по номеру автомобіля)"
        index_car = -1

        for car in range(len(self.green_turn_list)):
            for key, value in self.green_turn_list[car].items():
                if value == number:
                    index_car = car

        if index_car == -1:
            return f"У списку не має авто із номером {number}"

        else:
            result = f"Авто №{index_car} пропущено через кордон;\nІнформація про авто:\n{self.get_info(self.green_turn_list[index_car])}"
            winners.append(self.green_turn_list[index_car])
            del self.green_turn_list[index_car]
            return result

    def replace_turn_to_green(self, number: str) -> str:
        "Функція переносить авто зі звичайної черги до зеленої (по номеру автомобіля)"
        index_car = -1

        for car in range(len(self.turn_list)):
            for key, value in self.turn_list[car].items():
                if value == number:
                    index_car = car

        if index_car == -1:
            return f"У списку не має авто із номером {number}"

        else:
            self.green_turn_list.append(self.turn_list[index_car])
            del self.turn_list[index_car]
            return f"Машину з номером {number} перенесено у кінець зеленої черги"

    def replace_green_to_turn(self, number: str) -> str:
        "Функція переносить авто зі зеленої черги у звичайну (по номеру автомобіля)"
        index_car = -1

        for car in range(len(self.green_turn_list)):
            for key, value in self.green_turn_list[car].items():
                if value == number:
                    index_car = car

        if index_car == -1:
            return f"У списку не має авто із номером {number}"

        else:
            self.turn_list.append(self.green_turn_list[index_car])
            del self.green_turn_list[index_car]
            return f"Машину з номером {number} перенесено у кінець зеленої черги"

    def delete_auto_on_turn(self, number: str) -> str:
        "Функція яка видаляє авто із звичайної черги (по номеру автомобіля)"
        index_car = -1

        for car in range(len(self.turn_list)):
            for key, value in self.turn_list[car].items():
                if value == number:
                    index_car = car

        if index_car == -1:
            return f"У списку не має авто із номером {number}"

        else:
            del self.turn_list[index_car]
            return f"Машину з номером {number} видалено із черги, перетин кордону ЗАБОРОНЕНО!!!"

    def delete_auto_on_green_turn(self, number: str) -> str:
        "Функція яка видаляє авто із зеленої черги (по номеру автомобіля)"
        index_car = -1

        for car in range(len(self.green_turn_list)):
            for key, value in self.green_turn_list[car].items():
                if value == number:
                    index_car = car

        if index_car == -1:
            return f"У списку не має авто із номером {number}"

        else:
            del self.green_turn_list[index_car]
            return f"Машину з номером {number} видалено із зеленої черги, перетин кордону ЗАБОРОНЕНО!!!"

    def get_auto_in_tovar(self, need_product: str) -> str:
        "Функція яка повертає дані автомобіля у якому є вказаний товар"
        all_cars = self.turn_list + self.green_turn_list
        need_cars = []
        result = ""

        for car in all_cars:
            for key, value in car.items():
                if key == "goods": # Получаємо словник із товарами
                    for key_goods, value_goods in value.items():  # Проходимось по словнику із товарами
                        if value_goods == need_product:  # Перевіряємо чи є потрібний товар у списку товарів авто
                            need_cars.append(car)  # Додаємо авто до списку із потібним авто

        for car in all_cars:
            for need_car in need_cars:
                if car == need_car:
                    result += self.get_number_cars(car)

        return result

    def get_expensive_auto(self) -> str:
        "Функція яка повертає авто із найбільшою сумую товарів"
        all_cars = self.turn_list + self.green_turn_list
        max_sum = 0
        expensive_car = -1
        tovars = ""

        for car in all_cars:
            for key, value in car.items():
                if key == "goods":  # Получаємо словник із товарами
                    check_sum = 0 # Змінна для вирахування максимальної суми
                    for key_goods, value_goods in value.items():
                        check_sum += value_goods # Прибавляємо суми товарів автомобіля 
                    if check_sum >= max_sum: # Перевіряємо чи сума максимальна
                        max_sum = check_sum # Нова максимальна сума
                        expensive_car = car # Получаємо авто із максимальною сумою
        
        need_car = expensive_car

        for key, value in need_car.items():
            # Получаємо потрібну інфомрацію про авто
            if key == "auto":
                auto = value
            if key == "number":
                number_auto = value
            if key == "goods":
                for key_goods, value_goods in value.items():
                    tovars += f"{key_goods}, "

        tovars = tovars[:-2]

        return f"Авто {auto}(Номера: {number_auto}) перевоить товари[{tovars}] на рекордну суму {max_sum}грн."

    def tovar_list(self) -> str:
        "Функція яка повертає списки товарів та їхню загальну вартість із усіх авто"
        all_cars = self.turn_list + self.green_turn_list

        value_list = []
        price_list = []

        for car in all_cars:
            for key, value in car.items():
                if key == "goods": # Проходимось по усіх товарах усіх автомобілів
                    for key_goods, value_goods in value.items():
                        if key_goods in value_list: # Перевіряємо чи цей товар вже є у списку
                            index = value_list.index(key_goods) # беремо його індекс
                            price_list[index] += value_goods # Додаємо суму по індексу
                        else: # якщо товара немає у списку
                            value_list.append(key_goods) # додаємо товар у список
                            price_list.append(value_goods) # додаємо вартість у список

        result = "\tТовари:\t\tЦіна:\n"

        for tovar, price in zip(value_list, price_list):
            result += f"\t{tovar}\t\t{price}\n" # Форматуємо таблицю
    
        return result

    def get_auto_by_way(self, city: str = "Odesa") -> str:
        "Функція яка показує всі автомобілі які прямують до певного міста"
        all_cars = self.turn_list + self.green_turn_list
        cars_to_city = []

        for car in all_cars:
            for key, value in car.items():
                if key == "to": # Дістаємо значення ключа напрямку
                    if city in value: # Перевіряємо чи є місце у значенні напрямку 
                        cars_to_city.append(car) # Додаємо авто у список 

        if len(cars_to_city) == 0:
            return f"У списку немає машин які прямують в {city}"
        elif len(cars_to_city) == 1:
            return f"У списку є одна машина яка прямує в {city}, це:\n{cars_to_city[0]}"
        else:
            return f"У списку безліч машин які прямують до {city}, це:\n{' '.join([str(elem) for elem in cars_to_city])}"


if __name__ == "__main__":

    poland_turn = Turn() # Створюємо екземпляк класу

    for car in range(len(car_list)): # Проходимось по кількості авто у списку
        if car % 2 == 0: # Якщо індекс авто парний 
            poland_turn.add_auto_to_turn(car_list[car]) # Додаємо авто у звичайну чергу
        else: # Якщо індекс авто не парний
            poland_turn.add_auto_to_green_turn(car_list[car]) # Додаємо його у зелену чергу

    result_file = open("result.txt", "w", encoding="utf-8").close() # Очищаємо текстовий фалй
    result_file = open("result.txt", "a", encoding="utf-8") # Відкриваємо файл для запису

    result_file.write(f"Машини у списку:\n{'-----'*10}\n{poland_turn.get_all_info()}{'-----'*10}\n")
    result_file.write(f"\n\nКількість авто у звичайній черзі - {poland_turn.get_turn_lenght()}\nКількість авто у зеленій черзі - {poland_turn.get_green_turn_lenght()}\n")
    result_file.write(f"\nАвтомобілі та номера:\n{'-----'*10}\n{poland_turn.get_number_cars()}{'-----'*10}\n")
    result_file.write(f"\nПереведення авто із звичайної черги у зелену:\n{poland_turn.miss_the_car_in_turn('11-11')}\n")
    result_file.write(f"\nПереведення авто із зeленої черги у звичайну:\n{poland_turn.miss_the_car_in_green_turn('11-11')}\n")
    result_file.write(f"\nВидалення автомобіля із черги:\n{poland_turn.delete_auto_on_green_turn('51-11')}\n")
    result_file.write(f"\nЗнаходимо авто із найдорожчими товарами:\n{poland_turn.get_expensive_auto()}\n")
    result_file.write(f"\nСписок товарів у всіх автомобілях і їхня загальна сума:\n{'-----'*10}\n{poland_turn.tovar_list()}{'-----'*10}\n")
    result_file.write(f"\nАвтомобілі що прямують до Одесси:\n{poland_turn.get_auto_by_way()}\n")
    result_file.write(f"\nСписок авто що перетнули кордон:\n{winners}")
    # Програмно записуємо у файл усю інформацію, і тести деяких методівдд