print('Программа принимает на вход вещественное число и показывает сумму его цифр.')
while True:
    number = input('Введите число: ').replace('.', '')
    if number.isdigit():
        break
    print('Неверно введено число!')

result = 0
for i in number:
    result += int(i)
print(result)
