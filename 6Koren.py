import math                                         # math - Модуль для вычесления
def koren():                                        # def - Функция (Koren) название функции
    print("Введите цело неотрицательное число:")    # Print - Выводит информацию на экран
    num = int(input())                              # num - Переменная в которую мы задаем целое число с помощью (int) и сама команда (input)
    sqrt = math.sqrt(num)                           # sqrt - Функция которая возвращает корель числа
    sqrt = round(sqrt)                              # round - Функция которая округляет число
    print(sqrt)                                     # Print - Выводит информацию на экран
koren()                                             # Закрывает Функцию