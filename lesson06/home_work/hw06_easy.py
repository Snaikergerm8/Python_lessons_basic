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
        list_len_tr = len_ab, len_ac, len_bc
        return list_len_tr

    def perimeter(self):
        import math
        # вычисляем периметр
        p = self.len_side()[0] + self.len_side()[1] + self.len_side()[2]
        print(f"Периметр треугольника: {p}")
        return p

    def square(self):
        import math
        pl = self.perimeter() / 2
        square = math.sqrt(pl * ((pl - self.len_side()[0]) * (pl - self.len_side()[1]) * (pl - self.len_side()[2])))
        print(f"Площадь треугольника: {square}")
        return square

    def height(self):
        import math
        pl = self.perimeter() / 2
        height_a = 2 * (
            math.sqrt(pl * (pl - self.len_side()[0]) * (pl - self.len_side()[1]) * (pl - self.len_side()[2]))) / \
                   self.len_side()[0]
        height_b = 2 * (
            math.sqrt(pl * (pl - self.len_side()[0]) * (pl - self.len_side()[1]) * (pl - self.len_side()[2]))) / \
                   self.len_side()[1]
        height_c = 2 * (
            math.sqrt(pl * (pl - self.len_side()[0]) * (pl - self.len_side()[1]) * (pl - self.len_side()[2]))) / \
                   self.len_side()[2]
        print(f"Высоты треугольника:\nВысота а = {height_a}\nВысота b = {height_b}\nВысота c = {height_c}")


triangle1 = Triangle([1, 2], [3, 5], [9, 8])
triangle1.square()
triangle1.perimeter()
triangle1.height()

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
class Trapezium:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def len_side(self):
        import math
        # вычисляем коодинаты сторон трпеции
        ab = [self.b[0] - self.a[0], self.b[1] - self.a[1]]
        bc = [self.c[0] - self.b[0], self.c[1] - self.b[1]]
        cd = [self.d[0] - self.c[0], self.d[1] - self.c[1]]
        da = [self.a[0] - self.d[0], self.a[1] - self.d[1]]
        # вычисляем длину сторон трапеции
        len_ab = math.sqrt(math.fabs(ab[0] ** 2 + ab[1] ** 2))
        len_bc = math.sqrt(math.fabs(bc[0] ** 2 + bc[1] ** 2))
        len_cd = math.sqrt(math.fabs(cd[0] ** 2 + cd[1] ** 2))
        len_da = math.sqrt(math.fabs(da[0] ** 2 + da[1] ** 2))
        list_len_tr = len_ab, len_bc, len_cd, len_da
        # print(f"Сторона ab = {len_ab}\nСторона bc = {len_bc}\nСторона cd = {len_cd}\nСторона da = {len_da}")
        return len_ab, len_bc, len_cd, len_da

    def check(self):
        if self.len_side()[0] == self.len_side()[2]:
            print("Трапеция является равнобокой")
        else:
            print("Трапеция не является равнобокой")

    def perimetr(self):
        p = 0
        for i in self.len_side():
            p += i
        print(f"Периметр трапеции = {p}")
        return p

    def square(self):
        import math
        s = ((self.len_side()[1] + self.len_side()[3]) / 2) * math.sqrt(
            (self.len_side()[0] ** 2) - ((self.len_side()[3] - self.len_side()[1]) ** 2) / 4)
        print(f"Площаль трапеции = {s}")
        return s


trapezium1 = Trapezium([1, 2], [3, 5], [4, 5], [6, 8])
trapezium1.len_side()
trapezium1.check()
trapezium1.perimetr()
trapezium1.square()

