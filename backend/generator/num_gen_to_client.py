import json
import pprint
from data import db_session
from data.examples import Example
from numbers_generation.simple_numbers.solution import addition_substraction as add
from numbers_generation.simple_numbers.solution import multiplication as mult
from numbers_generation.simple_numbers.solution import division
from numbers_generation.simple_numbers.solution import more_operations
from numbers_generation.decimals.solution import Rational
from numbers_generation.decimals.solution import multiplication as mult_dec
from numbers_generation.decimals.solution import addition_or_substraction as add_sub_dec
from numbers_generation.decimals.solution import division as division_dec
from numbers_generation.decimals.solution import templates as decimals_temp
from numbers_generation.equations.solution import linear1
from numbers_generation.equations.solution import linear2
from numbers_generation.equations.solution import linear3

import random
import sys


def make_problem(n, numbers, func, categ):
    c = 0
    problems = set()
    while c != n:
        pair = numbers.pop()
        example = (*func(*pair), categ)
        problems.add(example)
        c += 1
    return problems


def problem(categ):
    db_session.global_init(r"..\db\users.db")
    sess = db_session.create_session()
    problems = set()
    if categ == 1:
        with open(r"..\data.json", "r") as f:
            to_json = json.load(f)
        numbers = to_json["simple_num_easy"]["addition"]
        if len(numbers) > 33:
            problems = problems | make_problem(33, numbers, add, categ)
        elif len(numbers) > 0:
            need = len(numbers)
            problems = problems | make_problem(need, numbers, add, categ)
        to_json["simple_num_easy"]["addition"] = numbers
        numbers = to_json["simple_num_easy"]["multiplication"]
        if len(numbers) > 33:
            problems = problems | make_problem(33, numbers, mult, categ)
        elif len(numbers) > 0:
            need = len(numbers)
            problems = problems | make_problem(need, numbers, mult, categ)
        to_json["simple_num_easy"]["multiplication"] = numbers
        numbers = to_json["simple_num_easy"]["division"]
        if len(numbers) > 33:
            problems = problems | make_problem(33, numbers, division, categ)
        elif len(numbers) > 0:
            need = len(numbers)
            problems = problems | make_problem(need, numbers, division, categ)
        to_json["simple_num_easy"]["division"] = numbers
        with open(r"..\data.json", "w") as f:
            json.dump(to_json, f)

    if categ == 2:
        with open(r"..\data.json", "r") as f:
            to_json = json.load(f)
        numbers = to_json["simple_num_normal"]["more_operations: mode0"]
        if len(numbers) > 200:
            c = 0
            while c != 200:
                pair = numbers.pop()
                example = (*more_operations(*pair, mode=0), categ)
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        elif len(numbers) > 0:
            need = len(numbers)
            c = 0
            while c != need:
                pair = numbers.pop()
                example = (*more_operations(*pair, mode=0), categ)
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        to_json["simple_num_normal"]["more_operations: mode0"] = numbers

        numbers = to_json["simple_num_normal"]["more_operations: mode1"]
        if len(numbers) > 200:
            c = 0
            while c != 200:
                pair = numbers.pop()
                example = (*more_operations(*pair, mode=1), categ)
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        elif len(numbers) > 0:
            need = len(numbers)
            c = 0
            while c != need:
                pair = numbers.pop()
                example = (*more_operations(*pair, mode=1), categ)
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        to_json["simple_num_normal"]["more_operations: mode1"] = numbers

        numbers = to_json["simple_num_normal"]["addition"]
        if len(numbers) > 200:
            problems = problems | make_problem(200, numbers, add, categ)
        elif len(numbers) > 0:
            need = len(numbers)
            problems = problems | make_problem(need, numbers, add, categ)
        to_json["simple_num_normal"]["addition"] = numbers

        numbers = to_json["simple_num_normal"]["multiplication"]
        if len(numbers) > 200:
            problems = problems | make_problem(200, numbers, mult, categ)
        elif len(numbers) > 0:
            need = len(numbers)
            problems = problems | make_problem(need, numbers, mult, categ)
        to_json["simple_num_normal"]["multiplication"] = numbers

        numbers = to_json["simple_num_normal"]["division"]
        if len(numbers) > 200:
            problems = problems | make_problem(200, numbers, division, categ)
        elif len(numbers) > 0:
            need = len(numbers)
            problems = problems | make_problem(need, numbers, division, categ)
        to_json["simple_num_normal"]["division"] = numbers

        with open(r"..\data.json", "w") as f:
            json.dump(to_json, f)

    if categ == 3:
        with open(r"..\data.json", "r") as f:
            to_json = json.load(f)
        numbers = to_json["simple_num_hard"]["more_operations: mode0"]
        if len(numbers) > 200:
            c = 0
            while c != 200:
                pair = numbers.pop()
                example = (*more_operations(*pair, mode=0), categ)
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        elif len(numbers) > 0:
            need = len(numbers)
            c = 0
            while c != need:
                pair = numbers.pop()
                example = (*more_operations(*pair, mode=0), categ)
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        to_json["simple_num_hard"]["more_operations: mode0"] = numbers

        numbers = to_json["simple_num_hard"]["more_operations: mode1"]
        if len(numbers) > 200:
            c = 0
            while c != 200:
                pair = numbers.pop()
                example = (*more_operations(*pair, mode=1), categ)
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        elif len(numbers) > 0:
            need = len(numbers)
            c = 0
            while c != need:
                pair = numbers.pop()
                example = (*more_operations(*pair, mode=1), categ)
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        to_json["simple_num_hard"]["more_operations: mode1"] = numbers

        numbers = to_json["simple_num_hard"]["addition"]
        if len(numbers) > 200:
            problems = problems | make_problem(200, numbers, add, categ)
        elif len(numbers) > 0:
            need = len(numbers)
            problems = problems | make_problem(need, numbers, add, categ)
        to_json["simple_num_hard"]["addition"] = numbers

        numbers = to_json["simple_num_hard"]["multiplication"]
        if len(numbers) > 200:
            problems = problems | make_problem(200, numbers, mult, categ)
        elif len(numbers) > 0:
            need = len(numbers)
            problems = problems | make_problem(need, numbers, mult, categ)
        to_json["simple_num_hard"]["multiplication"] = numbers

        numbers = to_json["simple_num_hard"]["division"]
        if len(numbers) > 200:
            problems = problems | make_problem(200, numbers, division, categ)
        elif len(numbers) > 0:
            need = len(numbers)
            problems = problems | make_problem(need, numbers, division, categ)
        to_json["simple_num_hard"]["division"] = numbers

        with open(r"..\data.json", "w") as f:
            json.dump(to_json, f)

    if categ == 4:
        with open(r"..\data.json", "r") as f:
            to_json = json.load(f)
        numbers = to_json["linear1"]
        if len(numbers) > 100:
            problems = problems | make_problem(100, numbers, linear1, categ)
        elif len(numbers) > 0:
            need = len(numbers)
            problems = problems | make_problem(need, numbers, linear1, categ)
        to_json["linear1"] = numbers

        with open(r"..\data.json", "w") as f:
            json.dump(to_json, f)

    if categ == 5:
        with open(r"..\data.json", "r") as f:
            file = f.read()
            to_json = json.loads(file)
        numbers = to_json["linear2"]
        if len(numbers) > 1000:
            problems = problems | make_problem(1000, numbers, linear2, categ)
        elif len(numbers) > 0:
            need = len(numbers)
            problems = problems | make_problem(need, numbers, linear2, categ)
        to_json["linear2"] = numbers

        with open(r"..\data.json", "w") as f:
            json.dump(to_json, f)

    if categ == 6:
        with open(r"..\data.json", "r") as f:
            file = f.read()
            to_json = json.loads(file)
        numbers = to_json["linear3"]
        if len(numbers) > 100:
            try:
                problems = problems | make_problem(100, numbers, linear3, categ)
            except Exception:
                for i in range(100):
                    numbers.pop()
        elif len(numbers) > 0:
            try:
                need = len(numbers)
                problems = problems | make_problem(need, numbers, linear3, categ)
            except Exception:
                for i in range(len(numbers)):
                    numbers.pop()
        to_json["linear3"] = numbers

        with open(r"..\data.json", "w") as f:
            json.dump(to_json, f)


    if categ == 7:
        with open(r"..\data.json", "r") as f:
            to_json = json.load(f)
        numbers = to_json["decimal1"]["addition"]
        if len(numbers) > 100:
            c = 0
            while c != 100:
                pair = numbers.pop()
                try:
                    example = (*add_sub_dec(Rational(pair[0], pair[1]), Rational(pair[2], pair[3])), categ)
                    example = (example[0], str(example[1]), example[2], example[3])
                except Exception:
                    continue
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        elif len(numbers) > 0:
            need = len(numbers)
            c = 0
            while c != need:
                pair = numbers.pop()
                try:
                    example = (*add_sub_dec(Rational(pair[0], pair[1]), Rational(pair[2], pair[3])), categ)
                    example = (example[0], str(example[1]), example[2], example[3])
                except Exception:
                    continue
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        to_json["decimal1"]["addition"] = numbers

        numbers = to_json["decimal1"]["mult"]
        if len(numbers) > 100:
            c = 0
            while c != 100:
                pair = numbers.pop()
                try:
                    example = (*mult_dec(Rational(pair[0], pair[1]), Rational(pair[2], pair[3])), categ)
                    example = (example[0], str(example[1]), example[2], example[3])
                except Exception:
                    continue
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        elif len(numbers) > 0:
            need = len(numbers)
            c = 0
            while c != need:
                pair = numbers.pop()
                try:
                    example = (*mult_dec(Rational(pair[0], pair[1]), Rational(pair[2], pair[3])), categ)
                    example = (example[0], str(example[1]), example[2], example[3])
                except Exception:
                    continue
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        to_json["decimal1"]["mult"] = numbers

        numbers = to_json["decimal1"]["division"]
        if len(numbers) > 100:
            c = 0
            while c != 100:
                pair = numbers.pop()
                try:
                    example = (*division_dec(Rational(pair[0], pair[1]), Rational(pair[2], pair[3])), categ)
                    example = (example[0], str(example[1]), example[2], example[3])
                except Exception:
                    continue
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        elif len(numbers) > 0:
            need = len(numbers)
            c = 0
            while c != need:
                pair = numbers.pop()
                try:
                    example = (*division_dec(Rational(pair[0], pair[1]), Rational(pair[2], pair[3])), categ)
                    example = (example[0], str(example[1]), example[2], example[3])
                except Exception:
                    continue
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        to_json["decimal1"]["division"] = numbers

        with open(r"..\data.json", "w") as f:
            json.dump(to_json, f)

    if categ == 8:
        with open(r"..\data.json", "r") as f:
            to_json = json.load(f)
        numbers = to_json["decimal2"]["addition"]
        if len(numbers) > 100:
            c = 0
            while c != 100:
                pair = numbers.pop()
                try:
                    example = (*add_sub_dec(Rational(pair[0], pair[1]), Rational(pair[2], pair[3])), categ)
                    example = (example[0], str(example[1]), example[2], example[3])
                except Exception:
                    continue
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        elif len(numbers) > 0:
            need = len(numbers)
            c = 0
            while c != need:
                pair = numbers.pop()
                try:
                    example = (*add_sub_dec(Rational(pair[0], pair[1]), Rational(pair[2], pair[3])), categ)
                    example = (example[0], str(example[1]), example[2], example[3])
                except Exception:
                    continue
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        to_json["decimal2"]["addition"] = numbers

        numbers = to_json["decimal2"]["template1"]
        if len(numbers) > 100:
            c = 0
            while c != 100:
                pair = numbers.pop()
                try:
                    example = (*decimals_temp(Rational(pair[0], pair[1]), Rational(pair[2], pair[3]), Rational(pair[4], pair[5]), template=1), categ)
                    example = (example[0], str(example[1]), example[2], example[3])
                except Exception:
                    continue
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        elif len(numbers) > 0:
            need = len(numbers)
            c = 0
            while c != need:
                pair = numbers.pop()
                try:
                    example = (*decimals_temp(Rational(pair[0], pair[1]), Rational(pair[2], pair[3]), Rational(pair[4], pair[5]), template=1), categ)
                    example = (example[0], str(example[1]), example[2], example[3])
                except Exception:
                    continue
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        to_json["decimal2"]["template1"] = numbers

        numbers = to_json["decimal2"]["template2"]
        if len(numbers) > 100:
            c = 0
            while c != 100:
                pair = numbers.pop()
                try:
                    example = (
                    *decimals_temp(Rational(pair[0], pair[1]), Rational(pair[2], pair[3]), Rational(pair[4], pair[5]),
                                   template=2), categ)
                    example = (example[0], str(example[1]), example[2], example[3])
                except Exception:
                    continue
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        elif len(numbers) > 0:
            need = len(numbers)
            c = 0
            while c != need:
                pair = numbers.pop()
                try:
                    example = (
                    *decimals_temp(Rational(pair[0], pair[1]), Rational(pair[2], pair[3]), Rational(pair[4], pair[5]),
                                   template=2), categ)
                    example = (example[0], str(example[1]), example[2], example[3])
                except Exception:
                    continue
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        to_json["decimal2"]["template2"] = numbers

        with open(r"..\data.json", "w") as f:
            json.dump(to_json, f)

    if categ == 9:
        with open(r"..\data.json", "r") as f:
            to_json = json.load(f)
        numbers = to_json["decimal3"]["template3"]
        if len(numbers) > 100:
            c = 0
            while c != 100:
                pair = numbers.pop()
                try:
                    example = (
                    *decimals_temp(Rational(pair[0], pair[1]), Rational(pair[2], pair[3]), Rational(pair[4], pair[5]),
                                   template=3), categ)
                    example = (example[0], str(example[1]), example[2], example[3])
                except Exception:
                    continue
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        elif len(numbers) > 0:
            need = len(numbers)
            c = 0
            while c != need:
                pair = numbers.pop()
                try:
                    example = (*decimals_temp(Rational(pair[0], pair[1]), Rational(pair[2], pair[3]), Rational(pair[4], pair[5]),
                                   template=3), categ)
                    example = (example[0], str(example[1]), example[2], example[3])
                except Exception:
                    continue
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        to_json["decimal3"]["template3"] = numbers

        numbers = to_json["decimal3"]["template1"]
        if len(numbers) > 100:
            c = 0
            while c != 100:
                pair = numbers.pop()
                try:
                    example = (
                    *decimals_temp(Rational(pair[0], pair[1]), Rational(pair[2], pair[3]), Rational(pair[4], pair[5]),
                                   template=1), categ)
                    example = (example[0], str(example[1]), example[2], example[3])
                except Exception:
                    continue
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        elif len(numbers) > 0:
            need = len(numbers)
            c = 0
            while c != need:
                pair = numbers.pop()
                try:
                    example = (
                    *decimals_temp(Rational(pair[0], pair[1]), Rational(pair[2], pair[3]), Rational(pair[4], pair[5]),
                                   template=1), categ)
                    example = (example[0], str(example[1]), example[2], example[3])
                except Exception:
                    continue
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        to_json["decimal3"]["template1"] = numbers

        numbers = to_json["decimal3"]["template2"]
        if len(numbers) > 100:
            c = 0
            while c != 100:
                pair = numbers.pop()
                try:
                    example = (
                        *decimals_temp(Rational(pair[0], pair[1]), Rational(pair[2], pair[3]),
                                       Rational(pair[4], pair[5]),
                                       template=2), categ)
                    example = (example[0], str(example[1]), example[2], example[3])
                except Exception:
                    continue
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        elif len(numbers) > 0:
            need = len(numbers)
            c = 0
            while c != need:
                pair = numbers.pop()
                try:
                    example = (
                        *decimals_temp(Rational(pair[0], pair[1]), Rational(pair[2], pair[3]),
                                       Rational(pair[4], pair[5]),
                                       template=2), categ)
                    example = (example[0], str(example[1]), example[2], example[3])
                except Exception:
                    continue
                if not sess.query(Example).filter(Example.problem == example[0]).all():
                    problems.add(example)
                else:
                    continue
                c += 1
        to_json["decimal3"]["template2"] = numbers

        with open(r"..\data.json", "w") as f:
            json.dump(to_json, f)

    if problems:
        for i in problems:
            save = i[0].split(" ")
            save = "~".join(save)
            sess.add(Example(problem=save,
                             answer=str(i[1]),
                             category_id=i[3],
                             steps=i[2]))
            sess.commit()
        return 0
    else:
        return True


if __name__ == "__main__":
    for i in range(1, 10):
        a = problem(i)