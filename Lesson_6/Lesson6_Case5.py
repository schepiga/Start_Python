class Stationary:

    def __init__(self, tittle="Канцелярский предмет"):
        self.tittle = tittle

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationary):
    def draw(self):
        print('Шариковая ручка')

class Pencil(Stationary):
    def draw(self):
       print('Простой карандаш')

class Handle(Stationary):
    def draw(self):
        print('Маркер')

b = Stationary()
b.draw()

a = Pen()
a.draw()

a = Handle()
a.draw()





