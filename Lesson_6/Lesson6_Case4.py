class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        print('Машина повернула')

    def show_speed(self, speed):
        print(f'Текущая скорость {speed}')

class TownCar(Car):
    def town_car_method (self):
        print('Машина класса комфорт')

    def show_speed(self, speed):
        if speed > 60:
            print('Вы превысили скорость')

class SportCar(Car):
    def sport_car_method (self):
        print('Машина класса спорт')

class WorkCar(Car):
    def work_car_method (self):
        print('Машина класса рабочая')

    def show_speed(self, speed):
        if speed > 40:
            print('Вы превысили скорость')

class PoliceCar(Car):
    def town_car_method (self):
        print('Полицейская машина')

a = PoliceCar(70, 'red', 'Mazda', True)
a.turn()
a.stop()
print(a.name)
print(a.is_police)

a = TownCar(90, 'black', 'Jeep', False)
print(a.is_police)



