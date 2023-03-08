def count_num(num, count_even=0, count_odd=0):
    if num == 0:
        print(f'Нечетных цифр в числе - {count_odd}, четных цифр - {count_even}')
        return
    else:
        if num % 10 % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        return count_num(round(num // 10), count_even, count_odd)

count_num(num = int(input('Введите число: ')))