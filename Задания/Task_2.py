#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Составить программу с использованием классов и объектов для решения задачи. Во всех
заданиях, помимо указанных в задании операций, обязательно должны быть реализованы
следующие методы:
метод инициализации __init__ ;
ввод с клавиатуры read ;
вывод на экран display .
Номер варианта необходимо уточнить у преподавателя. В раздел программы, начинающийся
после инструкции if __name__ = '__main__': добавить код, демонстрирующий возможности
разработанного класса.
---------------------------------------------------------------------------------------------------------------------
Реализовать класс Cursor. Полями являются координаты курсора по горизон тали и
вертикали — целые положительные числа, вид курсора — горизонталь ный или
вертикальный, размер курсора — целое от 1 до 15 Реализовать мето ды изменения
координат курсора, изменения вида курсора, изменения размера курсора, метод гашения и
восстановления курсора."""


class Cursor:
    def __init__(self, x=0, y=0, orientation='horizontal', size=1):
        self.x = max(0, x)  # координата по горизонтали
        self.y = max(0, y)  # координата по вертикали
        self.orientation = orientation  # вид курсора: 'horizontal' или 'vertical'
        self.size = max(1, min(15, size))  # размер курсора от 1 до 15
        self.is_visible = True  # видимость курсора

    def read(self):
        self.x = int(input("Введите координату X: "))
        self.y = int(input("Введите координату Y: "))
        self.orientation = input("Введите ориентацию курсора (horizontal/vertical): ")
        self.size = int(input("Введите размер курсора (от 1 до 15): "))
        self.validate()

    def display(self):
        print(f"Координаты курсора: ({self.x}, {self.y}), Ориентация: {self.orientation}, Размер: {self.size}, Видимость: {'Видимый' if self.is_visible else 'Скрытый'}")

    def change_orientation(self):
        if self.orientation == 'horizontal':
            self.orientation = 'vertical'
        else:
            self.orientation = 'horizontal'

    def change_size(self, new_size):
        self.size = max(1, min(15, new_size))

    def toggle_visibility(self):
        self.is_visible = not self.is_visible

    def validate(self):
        if self.orientation not in ['horizontal', 'vertical']:
            raise ValueError("Ориентация курсора должна быть 'horizontal' или 'vertical'")
        self.size = max(1, min(15, self.size))

if __name__ == '__main__':
    cursor = Cursor()
    cursor.read()
    cursor.display()

    # Изменение ориентации курсора
    cursor.change_orientation()
    print("\nПосле изменения ориентации:")
    cursor.display()

    # Изменение размера курсора
    new_size = int(input("\nВведите новый размер курсора: "))
    cursor.change_size(new_size)
    print("После изменения размера:")
    cursor.display()

    # Переключение видимости курсора
    cursor.toggle_visibility()
    print("После переключения видимости:")
    cursor.display()