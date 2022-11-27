#калькулятор 
a = int(input('Введи первое число: '))
b = int(input('Введи второе число: '))

c = input('Введи знак: ')

if c == '+':
    print(a + b)

elif c == '-':
    print(a - b)

elif c == '*':
    print(a * b)

elif c == '/' and b != 0:
    print(a / b)

else:
    print('Error')
