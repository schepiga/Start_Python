class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_asphalt_mass(self, mass, height):
        return self._length * self._width * mass * height

a = Road(20, 5000)
print(a.get_asphalt_mass(25, 5))





        

