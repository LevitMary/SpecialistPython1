# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

import random


def gen_list(size, of, to):
    gen_list = []

    for n in range(size):

        gen_list.append(random.randint(of, to))

    return gen_list


print(gen_list(5, 1, 5))
print(gen_list(7, 3, 6))


