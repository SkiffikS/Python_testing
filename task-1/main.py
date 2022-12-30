# -*- coding: utf-8 -*-

import Testorg # Імпортуємо написаний нами соновний модуль
import os

def Cyclic_testing(filepath):
    # Перевірка всіх функцій із різними файлами через цикл
    os.remove(filepath) # Очищаємо файл перед використанням
    # Задача 1
    task_1_files = Testorg.get_file_list(r"Testing_files\Task_1") # Дістаємо всі файли із папки для тесту
    Testorg.input_to_file(filepath, "Задача 1\n" + f"---" * 30) # Декоруємо файл для запису

    for i in task_1_files: # Проходимось по усім файлам
        input_data = Testorg.read_text(i) # Читаємо текст із файла
        result = Testorg.FnSol1(i) # виконуємо функцію із даними з файла
        Testorg.input_to_file(filepath,  f"\nВведені дані:\n{input_data}\n\nРезультат:") # Записуємо у файл результатів введені дані
        Testorg.input_to_file(filepath, f"\nКількість додатніх чисел: {result[0]}\nKількість відємних чисел: {result[1]}\nСереднє арифметичне відємних чисел: {result[2]}\n")
    Testorg.input_to_file(filepath, f"---" * 30) # Записуємо в файл результат виконання функцію та декоруємо

    # Процедуру зверху повторюємо для усіх функцій замінюючи деякі особливості

    # Задача 2
    task_2_files = Testorg.get_file_list(r"Testing_files\Task_2")
    Testorg.input_to_file(filepath, "\n\nЗадача 2\n" + f"---" * 30)

    for i in task_2_files:
        input_data = Testorg.read_text(i)
        data = Testorg.read_abc(i)
        result = Testorg.FnSol2(data[0], data[1], data[2])
        Testorg.input_to_file(filepath,  f"\nВведені дані:\n{input_data}\n\nРезультат:\n{result}\n")
    Testorg.input_to_file(filepath, f"---" * 30)

    task_3_files = Testorg.get_file_list(r"Testing_files\Task_3")
    Testorg.input_to_file(filepath, "\n\nЗадача 3\n" + f"---" * 30)

    for i in task_3_files:
        input_data = Testorg.read_text(i)
        result = Testorg.FnSol3(input_data)
        Testorg.input_to_file(filepath,  f"\nВведені дані:\n{input_data}\n\nРезультат:\n{result}\n")
    Testorg.input_to_file(filepath, f"---" * 30)

    task_4_files = Testorg.get_file_list(r"Testing_files\Task_4")
    Testorg.input_to_file(filepath, "\n\nЗадача 4\n" + f"---" * 30)

    for i in task_4_files:
        input_data = Testorg.read_text(i).replace(" ", "")
        result = Testorg.FnSol4(Testorg.read_matrix(i))
        Testorg.input_to_file(filepath,  f"\nВведені дані:\n{input_data}\n\nРезультат:\n{result}\n")
    Testorg.input_to_file(filepath, f"---" * 30)
        


if __name__ == "__main__":
    
    Cyclic_testing(r"ResultAll.txt") # Циклічно перевіряємо усі функції та записуємо результат у файл
    Testorg.Testorg() # Основна функція Testorg()