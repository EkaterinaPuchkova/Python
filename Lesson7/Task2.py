class Road():
    __weight = 0.5
    def __init__(pers, length, width):
        pers._length = length
        pers._width = width
        print(f'Дорога длиной {pers._length} метров и шириной {pers._width} метров')

    def get_weight(pers, depth):
        ret_val = pers._length * pers._width * depth * pers.__weight
        print(f'Вес асфальта, требуемый для укладки полотна толщиной '
              f'{depth} см, равен {ret_val} т')

        return ret_val

road1 = Road(100, 5)
w1 = road1.get_weight(10)

road2 = Road(1000, 20)
w2 = road2.get_weight(20)

print(f'Общий вес асфальта для двух объектов = {w1 + w2}')