# Задание №2 Реализовать класс Road (дорога)

class Road:
    __length = None
    __width = None
    weigth = None
    tickness = None

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def intake(self):
        self.weigth = 20
        self.tickness = 5
        intake = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'Нужно {intake} тонн чтобы построить дорогу')


road_to_village = Road(5000, 25)
road_to_village.intake()
