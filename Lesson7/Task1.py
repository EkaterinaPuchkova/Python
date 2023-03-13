from time import sleep as wait
from datetime import datetime as d_t

class TrafficLight:
    colors = {'красный': 7, 'желтый': 2, 'зеленый': 10}
    color = ''

    def burn(pers):
        for color, sw_time in pers.colors.items():
            pers.color = color
            start_state_time = d_t.now()

            print(f"Светофор горит цветом '{pers.color}' {sw_time} секунды ")

            wait(sw_time)

            print(f"Светофор закончил гореть цветом '{pers.color}' " 
                  f"{(d_t.now() - start_state_time).seconds} секунды ")


if __name__ == '__main__':
    TrafficLight().burn()
