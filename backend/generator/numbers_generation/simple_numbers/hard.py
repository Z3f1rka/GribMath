import itertools
import json
from .solution import addition_substraction as add
from .solution import multiplication as mult
from .solution import division
from .solution import more_operations
import random
import os


def to_debug(num):
    simple_num_hard(num, r"../../../data.json")


def simple_num_hard(num, path=r"..\data.json"):
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
    problem = set()
    numbers = {}
    if num % 5 == 0:
        to_type = num // 5
    else:
        to_type = num // 5 + 1

    to_iter = []
    to_not_iter = [i for i in range(-12, 13)]
    for i in range(-100, 100):
        if i != 0 and i != 1 and i != -1 and i not in to_not_iter:
            to_iter.append(i)
    random.shuffle(to_iter)
    to_iter = to_iter[:40]
    numbers_set = list(itertools.combinations(to_iter, 4))
    random.shuffle(numbers_set)
    c = 0
    while c != to_type:
        pair = numbers_set.pop()
        example = (*more_operations(*pair, mode=0), 3)
        problem.add(example)
        c += 1
    if len(numbers_set) > 50000:
        numbers_set = numbers_set[:50000]
    numbers["more_operations: mode0"] = numbers_set

    to_iter = []
    to_not_iter = [i for i in range(-12, 13)]
    for i in range(-100, 100):
        if i != 0 and i != 1 and i != -1 and i not in to_not_iter:
            to_iter.append(i)
    random.shuffle(to_iter)
    to_iter = to_iter[:40]
    numbers_set = list(itertools.combinations(to_iter, 3))
    random.shuffle(numbers_set)
    c = 0
    while c != to_type:
        pair = numbers_set.pop()
        example = (*more_operations(*pair, mode=1), 3)
        problem.add(example)
        c += 1
    if len(numbers_set) > 50000:
        numbers_set = numbers_set[:50000]
    numbers["more_operations: mode1"] = numbers_set

    to_iter = []
    to_not_iter = [i for i in range(-100, 100)]
    for i in range(-1000, 1000):
        if i != 0 and i != 1 and i != -1 and i not in to_not_iter:
            to_iter.append(i)
    random.shuffle(to_iter)
    to_iter = to_iter[:400]
    numbers_set = list(itertools.combinations(to_iter, 2))
    random.shuffle(numbers_set)
    c = 0
    while c != to_type:
        pair = numbers_set.pop()
        example = (*add(*pair), 3)
        problem.add(example)
        c += 1
    if len(numbers_set) > 50000:
        numbers_set = numbers_set[:50000]
    numbers["addition"] = numbers_set

    to_iter = []
    to_not_iter = [i for i in range(-12, 13)]
    for i in range(-100, 100):
        if i != 0 and i != 1 and i != -1 and i not in to_not_iter:
            to_iter.append(i)
    random.shuffle(to_iter)
    to_iter = to_iter
    numbers_set = list(itertools.combinations(to_iter, 2))
    random.shuffle(numbers_set)
    c = 0
    while c != to_type:
        pair = numbers_set.pop()
        example = (*mult(*pair), 3)
        problem.add(example)
        c += 1
    if len(numbers_set) > 50000:
        numbers_set = numbers_set[:50000]
    numbers["multiplication"] = numbers_set

    numbers_set = list(itertools.combinations(to_iter, 2))
    random.shuffle(numbers_set)
    c = 0
    while c != to_type:
        pair = numbers_set.pop()
        example = (*division(*pair), 3)
        problem.add(example)
        c += 1
    if len(numbers_set) > 50000:
        numbers_set = numbers_set[:50000]
    numbers["division"] = numbers_set
    problem = set(list(problem)[:num])

    with open(path, "w") as f:
        to_json["simple_num_hard"] = numbers
        json.dump(to_json, f)
    return problem


if __name__ == "__main__":
    to_debug(5000)