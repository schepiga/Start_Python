from time import sleep

class TrafficLight:

    def running(self, color):
        self.color = color

a_1 = TrafficLight()
a_2 = TrafficLight()
a_3 = TrafficLight()

a_1.running('red')
a_2.running('yellow')
a_3.running('green')

print(a_1.color, sleep(7))
print(a_2.color, sleep(2))
print(a_3.color, sleep(3))
