import random
import sys
sys.setrecursionlimit(1000000000)

class Rational_Coefficent:
    k = 0
    for i in range(1, 10):
        k += random.randint(1, 10)


class Rational:
    def __init__(self, num, denum):
        if num < 0:
            if denum < 0:
                self.numerator = abs(num)
                self.denominator = abs(denum)
            else:
                self.numerator = num
                self.denominator = denum
        else:
            if denum < 0:
                self.numerator = num * -1
                self.denominator = abs(denum)
            else:
                self.numerator = num
                self.denominator = denum

    def __lt__(self, other):
        if type(other) == int:
            return (self.numerator / self.denominator) < other
        elif type(other) == Rational:
            return (self.numerator / self.denominator) < (other.numerator / other.denominator)

    def __gt__(self, other):
        if type(other) == int:
            return (self.numerator / self.denominator) > other
        elif type(other) == Rational:
            return (self.numerator / self.denominator) > (other.numerator / other.denominator)

    def __eq__(self, other):
        if type(other) == int:
            return (self.numerator / self.denominator) == other
        elif type(other) == Rational:
            return (self.numerator / self.denominator) == (other.numerator / other.denominator)

    def __le__(self, other):
        if type(other) == int:
            return (self.numerator / self.denominator) <= other
        elif type(other) == Rational:
            return (self.numerator / self.denominator) <= (other.numerator / other.denominator)

    def __ge__(self, other):
        if type(other) == int:
            return (self.numerator / self.denominator) >= other
        elif type(other) == Rational:
            return (self.numerator / self.denominator) >= (other.numerator / other.denominator)

    def __add__(self, other):
        if self.denominator % other.denominator == 0:
            k = self.denominator / other.denominator
            steps = f"Умножаем числитель и знаменатель второй дроби на {k};Складываем числители;"
            return Rational(self.numerator + other.numerator * k,
                            self.denominator), steps
        elif other.denominator % self.denominator == 0:
            k = other.denominator / self.denominator
            steps = f"Умножаем числитель и знаменатель первой дроби на {k};Складываем числители;"
            return Rational(self.numerator * k + other.numerator,
                            other.denominator), steps
        steps = (f"Умножаем числитель и знаменатель 1 дроби на {other.denominator};"
                 f"Умножаем числитель и знаменатель 2 дроби на {self.denominator};"
                 f"Складываем числители;")
        return Rational(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator), steps

    def __sub__(self, other):
        if self.denominator % other.denominator == 0:
            k = self.denominator / other.denominator
            steps = f"Умножаем числитель и знаменатель второй дроби на {k};Вычитаем первый числитель из второго;"
            return Rational(self.numerator - other.numerator * k,
                            self.denominator), steps
        elif other.denominator % self.denominator == 0:
            k = other.denominator / self.denominator
            steps = f"Умножаем числитель и знаменатель второй дроби на {k};Вычитаем второй числитель из первого;"
            return Rational(self.numerator * k - other.numerator,
                            other.denominator), steps
        steps = (f"Умножаем числитель и знаменатель 1 дроби на {other.denominator};"
                 f"Умножаем числитель и знаменатель 2 дроби на {self.denominator};"
                 f"Вычитаем второй числитель из первого;")
        return Rational(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator),steps

    def __mul__(self, other):
        if type(self) == type(other):
            steps = ("Перемножаем числители;"
                     "Перемножаем знаменатели;")
            return Rational(self.numerator * other.numerator,
                            self.denominator * other.denominator), steps
        elif type(Rational_Coefficent()) == type(other):
            return Rational(self.numerator * other.k,
                            self.denominator * other.k)

    def __truediv__(self, other):
        steps = ("Переворачиваем вторую дробь;"
                 "Перемножаем числители;"
                 "Перемножаем знаменатели;")
        return Rational(self.numerator * other.denominator,
                        self.denominator * other.numerator), steps

    def __pow__(self, n):
        return Rational(self.numerator ** n, self.denominator ** n)

    def __str__(self):
        nod = euqlid_search(abs(self.numerator), abs(self.denominator))
        return fr"\\frac{'{'} {int(self.numerator / nod)} {'}'}{'{'} {int(self.denominator / nod)} {'}'}"

    def rational_now(self):
        return fr"\\frac{'{'} {int(self.numerator)} {'}'}{'{'} {int(self.denominator)} {'}'}"


def euqlid_search(m, n):
    if m == n:
        return m
    else:
        if m > n:
            m = m - n
        else:
            n = n - m
        # print(n, m)
        if m == 0:
            return 1
        if n == 0:
            raise ZeroDivisionError
        return euqlid_search(m, n)


def addition_or_substraction(a: Rational, b: Rational):
    if b > 0:
        ans = tuple(a + b)
        return f"{a.rational_now()}~+~{b.rational_now()}", str(ans[0]), ans[1]
    else:
        b = Rational(abs(b.numerator), abs(b.denominator))
        ans = tuple(a - b)
        return f"{a.rational_now()}~-~{b.rational_now()}", str(ans[0]), ans[1]


def multiplication(a: Rational, b: Rational):
    ans = tuple(a * b)
    return f"{a.rational_now()}~*~{b.rational_now()}", str(ans[0]), ans[1]


def division(a: Rational, b: Rational):
    ans = tuple(a / b)
    return f"{a.rational_now()}~:~{b.rational_now()}", str(ans[0]), ans[1]


def templates(a: Rational, b: Rational, c: Rational, template):
    problem = ""
    ans = ""
    if template == 1:
        if random.choice(["*", "/"]) == "/":
            problem = f"{a.rational_now()}~/~{b.rational_now()}"
            ans = a / b
        else:
            problem = f"{a.rational_now()}~*~{b.rational_now()}"
            ans = a * b
        if random.choice(["+", "-"]) == "+":
            if c > 0:
                problem = problem + f"~+~{c.rational_now()}"
                act = ans[0] + c
                ans = (act[0], ans[1] + act[1])
            else:
                c = Rational(abs(c.numerator), abs(c.denominator))
                problem = problem + f"~-~{c.rational_now()}"
                act = ans[0] - c
                ans = (act[0], ans[1] + act[1])
        else:
            if c > 0:
                problem = problem + f"~-~{c.rational_now()}"
                act = ans[0] - c
                ans = (act[0], ans[1] + act[1])
            else:
                c = Rational(abs(c.numerator), abs(c.denominator))
                problem = problem + f"~+~{c.rational_now()}"
                act = ans[0] + c
                ans = (act[0], ans[1] + act[1])
    if template == 2:
        if random.choice(["+", "-"]) == "+":
            if b > 0:
                problem = f"({a.rational_now()}~+~{b.rational_now()})"
                ans = a + b
            else:
                b = Rational(abs(b.numerator), abs(b.denominator))
                problem = f"({a.rational_now()}~-~{b.rational_now()})"
                ans = a - b
        else:
            if b > 0:
                problem = f"({a.rational_now()}~-~{b.rational_now()})"
                ans = a - b
            else:
                b = Rational(abs(b.numerator), abs(b.denominator))
                problem = f"({a.rational_now()}~+~{b.rational_now()})"
                ans = a + b
        if random.choice(["*", "/"]) == "/":
            problem = f"{c.rational_now()}~/~" + problem
            act = c / ans[0]
            ans = (act[0], ans[1] + act[1])
        else:
            problem = f"{c.rational_now()}~*~" + problem
            act = c * ans[0]
            ans = (act[0], ans[1] + act[1])
    if template == 3:
        if random.choice(["+", "-"]) == "+":
            if b > 0:
                problem = f"({a.rational_now()}~+~{b.rational_now()})"
                ans = a + b
            else:
                b = Rational(abs(b.numerator), abs(b.denominator))
                problem = f"({a.rational_now()}~-~{b.rational_now()})"
                ans = a - b
        else:
            if b > 0:
                problem = f"({a.rational_now()}~-~{b.rational_now()})"
                ans = a - b
            else:
                b = Rational(abs(b.numerator), abs(b.denominator))
                problem = f"({a.rational_now()}~+~{b.rational_now()})"
                ans = a + b
        if random.choice(["+", "-"]) == "+":
            if c > 0:
                problem = problem + f"~+~{c.rational_now()}"
                act = ans[0] + c
                ans = (act[0], ans[1] + act[1])
            else:
                c = Rational(abs(c.numerator), abs(c.denominator))
                problem = problem + f"~-~{c.rational_now()}"
                act = ans[0] - c
                ans = (act[0], ans[1] + act[1])
        else:
            if c > 0:
                problem = problem + f"~-~{c.rational_now()}"
                act = ans[0] - c
                ans = (act[0], ans[1] + act[1])
            else:
                c = Rational(abs(c.numerator), abs(c.denominator))
                problem = problem + f"~+~{c.rational_now()}"
                act = ans[0] + c
                ans = (act[0], ans[1] + act[1])
    decimal = str(ans[0])
    return problem, decimal, ans[1] + f"Сокращаем до {decimal}"


if __name__ == "__main__":
    a = Rational(30, 15) - Rational(10, 5)
    print(str(a[0]))
    b = Rational(16, 28) / a[0]
    print(str(b[0]))