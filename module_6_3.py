class Horse:                      # создаем класс лошади

    def __init__(self, *arge):    # вписываем динамические атрибуты
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__(*arge)

    def run(self, dx):            # метод увеличивает дистанцию на "dx"
        self.x_distance += dx


class Eagle:                      # создаем класс орла

    def __init__(self, *arge):    # вписываем динамические атрибуты
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'
        super().__init__(*arge)

    def fly(self, dy):            # метод увеличивает дистанцию на "dy"
        self.y_distance += dy


class Pegasus(Horse, Eagle):     # создаем дочерний класс лошади и орла

    def __init__(self, *arge):
        super().__init__(*arge)

    def move(self, dx, dy):     # метод наследует функции "run" и "fly"
        self.run(dx)
        self.fly(dy)

    def get_pos(self):          # метод возвращает измененную дистанцию
        return self.x_distance, self.y_distance

    def voice(self):            # печатает унаследованный звук
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
