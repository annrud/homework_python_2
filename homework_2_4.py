# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint

number_of_elements = 10

lst = [randint(-number_of_elements, number_of_elements)
       for _ in range(number_of_elements)]
print(lst)
with open('file.txt', 'r') as f:
    product = 1
    for i in f.readlines():
        product *= lst[int(i.strip())]
    print(product)
