import json

from .solution import linear1
import os


def to_debug(num):
    equations_linear1(num, path=r"../../../data.json")


def equations_linear1(num, path=r"..\data.json"):
    if num:
        """max: """
        """расчет количества примеров: надо num примеров
        1. делим num примеров на количество типов
        2. делаем список нужных чисел
        3. делаем product этих чисел
        4. закидываем спискок product'oв в решатор
        5. отрезаем ненужную часть для типа
        6. записываем в бд
        7. закидываем в json оставшиеся пары"""
        if os.path.exists(path):
            with open(path) as f:
                file = f.read()
                to_json = json.loads(file)
                print("data.json найден")
        else:
            to_json = {}
            print("data.json создан")
        numbers = {}
        problems = set()
        numbers_set = []
        for a in range(-20, 20):
            for b in range(-20, 20):
                if a and b:
                    k = 0
                    for i in range(1, int(abs(a - b) ** 0.5)):
                        if abs(a - b) % i == 0:
                            k = i
                    if k:
                        numbers_set.append((k, a, b))
        c = 0
        while c != num:
            pair = numbers_set.pop()
            example = (*linear1(*pair), 4)
            problems.add(example)
            c += 1
        if len(numbers_set) > 50000:
            numbers_set = numbers_set[:50000]
        numbers = numbers_set

        with open(path, "w") as f:
            to_json["linear1"] = numbers
            json.dump(to_json, f)
        return problems
    else:
        if os.path.exists(path):
            with open(path) as f:
                file = f.read()
                to_json = json.loads(file)
                print("data.json найден")
        else:
            to_json = {}
            print("data.json создан")
        numbers_set = []
        for a in range(-20, 20):
            for b in range(-20, 20):
                if a and b:
                    k = 0
                    for i in range(1, int(abs(a - b) ** 0.5)):
                        if abs(a - b) % i == 0:
                            k = i
                    if k:
                        numbers_set.append((k, a, b))
        numbers = numbers_set
        print(len(numbers))
        with open(path, "w") as f:
            to_json["linear1"] = numbers
            json.dump(to_json, f)


if __name__ == "__main__":
    to_debug(0)