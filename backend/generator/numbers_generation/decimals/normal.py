import itertools
import json
from .solution import Rational
from .solution import addition_or_substraction as add
from .solution import templates
import random
import os


def to_debug(num):
    decimal2(num, path=r"../../../data.json")


def decimal2(num, path=r"..\data.json"):
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
    if num % 3 == 0:
        to_type = num // 3
    else:
        to_type = num // 3 + 1

    to_iter = []
    to_not_iter = []
    for i in range(-20, 21):
        to_not_iter.append(i)
    for i in range(-100, 101):
        if i != 1 and i != 0 and i != -1 and  i not in to_not_iter:
            to_iter.append(i)
    random.shuffle(to_iter)
    to_iter = to_iter[:30]
    numbers_set = list(itertools.product(to_iter, repeat=4))
    random.shuffle(numbers_set)
    c = 0
    while c != to_type:
        pair = numbers_set.pop()
        example = (*add(Rational(pair[0], pair[1]), Rational(pair[2], pair[3])), 8)
        problems.add(example)
        c += 1
    if len(numbers_set) > 50000:
        numbers_set = numbers_set[:50000]
    numbers["addition"] = list(set(numbers_set))

    to_iter = []
    for i in range(-30, 31):
        if i != 1 and i != 0 and i != -1:
            to_iter.append(i)
    random.shuffle(to_iter)
    to_iter = to_iter[:30]
    numbers_set = list(itertools.combinations(to_iter, 6))
    random.shuffle(numbers_set)
    c = 0
    while c != to_type:
        pair = numbers_set.pop()
        try:
            example = (*templates(Rational(pair[0], pair[1]), Rational(pair[2], pair[3]),
                                  Rational(pair[4], pair[5]), template=1), 8)
        except Exception:
            continue
        problems.add(example)
        c += 1
    if len(numbers_set) > 50000:
        numbers_set = numbers_set[:50000]
    numbers["template1"] = list(set(numbers_set))

    to_iter = []
    for i in range(-30, 31):
        if i != 1 and i != 0 and i != -1:
            to_iter.append(i)
    random.shuffle(to_iter)
    to_iter = to_iter[:30]
    numbers_set = list(itertools.combinations(to_iter, 6))
    random.shuffle(numbers_set)
    c = 0
    while c != to_type:
        pair = numbers_set.pop()
        try:
            example = (*templates(Rational(pair[0], pair[1]), Rational(pair[2], pair[3]),
                                  Rational(pair[4], pair[5]), template=2), 8)
        except Exception:
            continue
        problems.add(example)
        c += 1
    if len(numbers_set) > 50000:
        numbers_set = numbers_set[:50000]
    numbers["template2"] = list(set(numbers_set))
    problems = set(list(problems)[:num])

    with open(path, "w") as f:
        to_json["decimal2"] = numbers
        json.dump(to_json, f)
    return problems


if __name__ == "__main__":
    pass