# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
# Решение

# n = int(input('ВВедите первый элимент: '))
# d = int(input('Введите разность: '))
# m = int(input('Введите количетсов элементов: '))
# list_first = list()
# for i in range(m):
#     an = n + i * d
#     list_first.append(an)

# print(list_first)



# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]  Всего (20)
# Вывод: [1, 9, 13, 14, 19]

#### РЕШЕНИЕ #####

# list_first = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

# list_second = list()
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_first)):
#     if min_number <= list_first[i] <= max_number:
#         list_second.append(i)
# print(list_second)    

