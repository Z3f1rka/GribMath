import itertools
import json
from .solution import linear2
import random
import os


def to_debug(num):
    equations_linear2(num, path=r"../../../data.json")


def equations_linear2(num, path=r"..\data.json"):
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
        with open(path, "r") as f:
            file = f.read()
            to_json = json.loads(file)
            print("data.json найден")
    else:
        to_json = {}
        print("data.json создан")
    numbers = {}
    problems = set()

    to_iter = []
    for i in range(-30, 30):
        if i != 0 and i != -1 and i != 1:
            to_iter.append(i)
    random.shuffle(to_iter)
    to_iter = to_iter[:30]
    numbers_set = list(itertools.combinations(to_iter, 5))
    random.shuffle(numbers_set)
    c = 0
    while c != num:
        pair = numbers_set.pop()
        example = (*linear2(*pair), 5)
        problems.add(example)
        c += 1
    if len(numbers_set) > 50000:
        numbers_set = numbers_set[:50000]
    numbers = numbers_set
    problems = set(list(problems)[:num])

    with open(path, "w") as f:
        to_json["linear2"] = numbers
        json.dump(to_json, f)
    return problems


if __name__ == "__main__":
    to_debug(800)