# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def len_side(self):
        import math
        # вычисляем коодинаты сторон треугольника
        ab = [self.b[0] - self.a[0], self.b[1] - self.a[1]]
        ac = [self.c[0] - self.a[0], self.c[1] - self.a[1]]
        bc = [self.c[0] - self.b[0], self.c[1] - self.b[1]]
        # вычисляем длину сторон треугольника
        len_ab = math.sqrt(math.fabs(ab[0] ** 2 + ab[1] ** 2))
        len_ac = math.sqrt(math.fabs(ac[0] ** 2 + ac[1] ** 2))
        len_bc = math.sqrt(math.fabs(bc[0] ** 2 + bc[1] ** 2))
        return len_ab, len_ac, len_bc
    def perimeter(self):
        import math
        #вычисляем периметр
        p = len_ab + len_ac + len_bc
        return print(f"Периметр треугольника: {p}")
    def square(self):
        import math
        pl = self.p / 2
        square = math.sqrt(pl*((pl - len_ab)*(pl - len_ac)*(pl - len_bc)))
        return print(f"Площадь треугольника: {square}")


    '''def height(self):
        height_a =
        height_b =
        height_c =
    '''


triangle1 = Triangle([1, 2], [3, 5], [9, 8])
triangle1.square()
triangle1.perimeter()

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

