import itertools
import json
from .solution import Rational
from .solution import addition_or_substraction as add
from .solution import multiplication as mult
from .solution import division
import random
import os


def to_debug(num):
    decimal1(num, path=r"../../../data.json")


def decimal1(num, path=r"..\data.json"):
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
    for i in range(-20, 21):
        if i != 1 and i != 0 and i != -1:
            to_iter.append(i)
    numbers_set = list(itertools.product(to_iter, repeat=4))
    random.shuffle(numbers_set)
    c = 0
    while c != to_type:
        pair = numbers_set.pop()
        example = (*add(Rational(pair[0], pair[1]), Rational(pair[2], pair[3])), 7)
        problems.add(example)
        c += 1
    if len(numbers_set) > 50000:
        numbers_set = numbers_set[:50000]
    numbers["addition"] = list(set(numbers_set))

    to_iter = []
    for i in range(-20, 21):
        if i != 1 and i != 0 and i != -1:
            to_iter.append(i)
    numbers_set = list(itertools.product(to_iter, repeat=4))
    random.shuffle(numbers_set)
    c = 0
    while c != to_type:
        pair = numbers_set.pop()
        example = (*mult(Rational(pair[0], pair[1]), Rational(pair[2], pair[3])), 7)
        problems.add(example)
        c += 1
    if len(numbers_set) > 50000:
        numbers_set = numbers_set[:50000]
    numbers["mult"] = list(set(numbers_set))

    to_iter = []
    for i in range(-20, 21):
        if i != 1 and i != 0 and i != -1:
            to_iter.append(i)
    numbers_set = list(itertools.product(to_iter, repeat=4))
    random.shuffle(numbers_set)
    c = 0
    while c != to_type:
        pair = numbers_set.pop()
        example = (*division(Rational(pair[0], pair[1]), Rational(pair[2], pair[3])), 7)
        problems.add(example)
        c += 1
    if len(numbers_set) > 50000:
        numbers_set = numbers_set[:50000]
    numbers["division"] = list(set(numbers_set))
    problems = set(list(problems)[:num])

    with open(path, "w") as f:
        to_json["decimal1"] = numbers
        json.dump(to_json, f)
    return problems

if __name__ == "__main__":
    pass