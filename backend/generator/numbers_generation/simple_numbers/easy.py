import json
import itertools
from .solution import addition_substraction as add
from .solution import multiplication as mult
from .solution import division
import sys
sys.path.append(r"../data")
import random
import os


def to_debug(num):
    simple_num_easy(num, r"../../../data.json")


def combinations(a: list):
    ans = []
    for i in a:
        for j in a:
            ans.append((i, j))
    return ans


def simple_num_easy(num, path=r"..\data.json"):
    """max: 1452"""
    if num:
        if os.path.exists(path):
            with open(path, "r") as f:
                file = f.read()
                to_json = json.loads(file)
                print("data.json найден")
        else:
            to_json = {}
            print("data.json создан")
        problems = set()
        if num % 3 == 0:
            to_type = num // 3
        else:
            to_type = num // 3 + 1

        to_iter = []
        for i in range(-20, 21):
            if i != 1 and i != 0 and i != -1:
                to_iter.append(i)
        numbers_set = list(itertools.product(to_iter, repeat=2))
        random.shuffle(numbers_set)
        c = 0
        while c != to_type:
            pair = numbers_set.pop()
            example = (*add(*pair), 1)
            problems.add(example)
            c += 1
        numbers = {}
        if len(numbers_set) > 50000:
            numbers_set = numbers_set[:50000]
        numbers["addition"] = list(set(numbers_set))

        to_iter = []
        for i in range(-12, 13):
            if i != 1 and i != 0 and i != -1:
                to_iter.append(i)
        numbers_set = list(itertools.product(to_iter, repeat=2))
        random.shuffle(numbers_set)
        c = 0
        while c != to_type:
            pair = numbers_set.pop()
            example = (*mult(*pair), 1)
            problems.add(example)
            c += 1
        if len(numbers_set) > 50000:
            numbers_set = numbers_set[:50000]
        numbers["multiplication"] = list(set(numbers_set))

        numbers_set = list(itertools.product(to_iter, repeat=2))
        random.shuffle(numbers_set)
        c = 0
        while c != to_type:
            pair = numbers_set.pop()
            example = (*division(*pair), 1)
            problems.add(example)
            c += 1
        if len(numbers_set) > 50000:
            numbers_set = numbers_set[:50000]
        numbers["division"] = list(set(numbers_set))
        problems = set(list(problems)[:num])

        with open(path, "w") as f:
            to_json["simple_num_easy"] = numbers
            json.dump(to_json, f)
        return problems
    else:
        numbers = {}
        numbers_set = list(itertools.product([i for i in range(-20, 20)], repeat=2))
        numbers["addition"] = list(set(numbers_set))

        to_iter = []
        for i in range(-12, 13):
            if i != 1 and i != 0 and i != -1:
                to_iter.append(i)
        numbers_set = list(itertools.product(to_iter, repeat=2))
        numbers["division"] = list(set(numbers_set))
        numbers["multiplication"] = list(set(numbers_set))
        with open(path, "w") as f:
            to_json = {}
            to_json["simple_num_easy"] = numbers
            json.dump(to_json, f)


if __name__ == "__main__":
    to_debug(800)