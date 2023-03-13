a1= int(input("Введите значение 1-го элемента:"))
d=int(input("Введите разность элементов:"))
n=int(input("Введите количество элементов:"))
res = [a1 + (i - 1) * d for i in range(1, n + 1)]
print(*res)

