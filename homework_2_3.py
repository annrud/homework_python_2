print('Программа принимает на вход число n, создаёт словарь '
      'из n чисел последовательности (1 + (1/n))^n и '
      'выводит на экран их сумму')
while True:
    number = input('Введите число n: ')
    if number.isdigit():
        break
    print('Неверно введено число!')
dct = {}
for i in range(1, int(number)+1):
    dct[i] = round((1+(1/i))**i, 2)
print(dct)
sum_values = 0
for i in dct.values():
    sum_values += i
print(f'Сумма значений = {sum_values}')

