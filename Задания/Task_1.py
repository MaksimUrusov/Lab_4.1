#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Парой называется класс с двумя полями, которые обычно имею т имена first и second. Требуется
реализовать тип данных с помощью такого класса. Во всех заданиях обязательно должны
присутствовать:
метод инициализации __init__ ; метод должен контролировать значения аргумен тов на
корректность;
ввод с клавиатуры read ;
вывод на экран display .
Реализовать внешнюю функцию с именем make_тип() , где тип — тип реализуе мой структуры.
Функция должна получать в качестве аргументов значения для полей структуры и возвращать
структуру требуемого типа. При передаче оши бочных параметров следует выводить сообщение
и заканчивать работу.
Номер варианта необходимо уточнить у преподавателя. В раздел программы, начинающийся
после инструкции if __name__ = '__main__': добавить код, демонстрирующий возможности
разработанного класса.
Поле first — целое число, целая часть числа; поле second — положительное целое число,
дробная часть числа. Реализовать метод multiply() — умножение на произвольное целое
число типа int. Метод должен правильно работать при любых допустимых значениях first и
second."""

class Pair:
    def __init__(self, first=0, second=0):
        self.first = int(first)
        self.second = int(second)

        if self.second < 0:
            raise ValueError("Значение 'second' должно быть положительным.")

    def read(self, prompt=None):
        line = input(
            "Введите целую и дробную часть числа через запятую (например, '5, 99'): ") if prompt is None else input(
            prompt)
        parts = list(map(int, line.split(',', maxsplit=1)))

        if parts[1] < 0:
            raise ValueError("Дробная часть числа должна быть положительным числом.")

        self.first, self.second = parts

    def display(self):
        print(f"Число: {self.first}.{self.second}")

    def multiply(self, multiplier):
        # Умножение числа с учетом дробной части
        full_number = float(f"{self.first}.{self.second}")
        result = full_number * multiplier
        self.first, self.second = map(int, str(result).split('.'))

    @staticmethod
    def make_pair(first, second):
        """
        Статическая функция создания экземпляра класса Pair
        """
        return Pair(first, second)


if __name__ == '__main__':
    print("Создаем число:")
    number = Pair.make_pair(5, 99)
    number.display()

    print("\nВведите число для создания:")
    number.read()
    number.display()

    multiplier = int(input("Введите множитель: "))
    number.multiply(multiplier)
    print(f"Результат умножения:")
    number.display()
