def calculator(sign):
    signs = ['+', '-', '*', '/', '0']

    if sign not in signs:
        print('Это не знак операции, повторите попытку')
        return (calculator(sign=input(f'Введите знак операции (+, -, *, / или 0 для выхода):   ')))
    else:
        if sign == '0':
            return (print('Работа калькулятора завершена'))
        num1 = input(f'Введите первое число : ')
        num2 = input(f'Введите второе число : ')
        if num1.isdigit() and num2.isdigit():
            if num2.isdigit() != 0:
                if sign == '+': print(f'Результат = {float(num1) + float(num2)}')
                if sign == '-': print(f'Результат = {float(num1) - float(num2)}')
                if sign == '/': print(f'Результат = {float(num1) / float(num2)}')
                if sign == '*': print(f'Результат = {float(num1) * float(num2)}')
            return (calculator(sign=input(f'Введите знак операции (+, -, *, / или 0 для выхода):   ')))
        else:
            print('Числа введены некорректно. Повторите ввод.')
            return (calculator(sign=input(f'Введите знак операции (+, -, *, / или 0 для выхода):   ')))


calculator(sign=input(f'Введите знак операции: '))