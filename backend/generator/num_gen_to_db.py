import sys
sys.path.append("..")
from numbers_generation.simple_numbers.easy import simple_num_easy
from numbers_generation.simple_numbers.normal import simple_num_normal
from numbers_generation.simple_numbers.hard import simple_num_hard
from numbers_generation.equations.easy import equations_linear1
from numbers_generation.equations.normal import equations_linear2
from numbers_generation.equations.hard import equations_linear3
from numbers_generation.decimals.easy import decimal1
from numbers_generation.decimals.normal import decimal2
from numbers_generation.decimals.hard import decimal3
from data import db_session
from data.main_category import MainCategory
from category_fill import db_cat_fill
from data.examples import Example
from numbers_generation.simple_numbers.solution import more_operations
import argparse
import json
sys.setrecursionlimit(1000000000)


def tilda_save(problems: set, sess):
    for i in problems:
        save = i[0].split(" ")
        save = "~".join(save)
        sess.add(Example(problem=save,
                         answer=str(i[1]),
                         category_id=i[3],
                         steps=i[2]))
        sess.commit()


def save(problems: set, sess):
    for i in problems:
        sess.add(Example(problem=i[0],
                         answer=str(i[1]),
                         category_id=i[3],
                         steps=i[2]))
        sess.commit()


def to_debug():
    pass


def problem(categ, num_examples, sess):
    db_session.global_init(r"..\db\users.db")
    problems = set()
    if not sess.query(MainCategory).all():
        db_cat_fill()
    if categ == 1:
        problems = problems | simple_num_easy(num_examples)
        tilda_save(problems, sess)
    if categ == 2:
        problems = problems | simple_num_normal(num_examples)
        tilda_save(problems, sess)
    if categ == 3:
        problems = problems | simple_num_hard(num_examples)
        tilda_save(problems, sess)
    if categ == 4:
        problems = problems | equations_linear1(num_examples)
        tilda_save(problems, sess)
    if categ == 5:
        problems = problems | equations_linear2(num_examples)
        tilda_save(problems, sess)
    if categ == 6:
        problems = problems | equations_linear3(num_examples)
        tilda_save(problems, sess)
    if categ == 7:
        problems = problems | decimal1(num_examples)
        save(problems, sess)
    if categ == 8:
        problems = problems | decimal2(num_examples)
        save(problems, sess)
    if categ == 9:
        problems = problems | decimal3(num_examples)
        save(problems, sess)


if __name__ == "__main__":
    db_session.global_init(r"..\db\users.db")
    sess = db_session.create_session()
    _parser = argparse.ArgumentParser()
    _parser.add_argument("num", type=int, help="max: 11 000 for all categories; for categories 1, 4 max:1200; for others: 5000), min 27", nargs="?", default=800)
    _parser.add_argument("category", type=int, help="1 <= N <= 9 or -1 to make all categories",
                         default=-1, nargs="?")
    args = _parser.parse_args()
    number_examples = args.num
    try:
        if not 27 <= number_examples <= 11000:
            raise ValueError
        category = args.category
        if category == -1:
            if number_examples % 9:
                num = number_examples // 9
            else:
                num = number_examples // 9 + 1
            for i in range(1, 10):
                problem(i, num, sess)
            while len(sess.query(Example.problem).all()) != number_examples:
                with open(r"..\data.json", "r") as f:
                    to_json = json.load(f)
                numbers = to_json["simple_num_hard"]["more_operations: mode0"]
                c = 0
                problems = set()
                while c != (number_examples - len(sess.query(Example.problem).all())):
                    pair = numbers.pop()
                    example = (*more_operations(*pair, mode=0), 3)
                    if not sess.query(Example).filter(Example.problem == example[0]).all():
                        problems.add(example)
                    else:
                        continue
                    c += 1
                tilda_save(problems, sess)
                to_json["simple_num_hard"]["more_operations: mode0"] = numbers
            print("all category filled")
        elif 1 <= category <= 9:
            if number_examples > 1200 and category == 4:
                raise ValueError
            elif number_examples > 1200 and category == 1:
                raise ValueError
            elif number_examples > 5000:
                raise ValueError
            problem(category, number_examples, sess)
            print(f"{category} category filled")
        else:
            print("Incorrect category")
    except Exception as ex:
        if type(ex).__name__ == "ValueError":
            print("Incorrect number")
        else:
            print(type(ex).__name__)