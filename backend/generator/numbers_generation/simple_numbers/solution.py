import random
# приоритетная очередь queue


def is_digit(i: str):
    try:
        if i.isdigit():
            return True
        elif i[0] == "-" and i[1:].isdigit():
            return True
        else:
            return False
    except Exception as ex:
        if type(ex).__name__ == "ValueError":
            return False
        elif type(ex).__name__ == "TypeError":
            return False
        else:
            print("отдать на тестировку")


def to_postfix(ex: str):
    ex = ex.split()
    stack = list()
    queue = list()
    postfix = list()
    priority = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "**": 3,
    }

    for i in ex:
        if is_digit(i):
            queue.append(i)
        elif i in priority.keys():
            if not stack or stack[-1] == "(":
                stack.append(i)
            elif priority[stack[-1]] < priority[i]:
                stack.append(i)
            elif priority[stack[-1]] >= priority[i]:
                while priority[stack[-1]] >= priority[i] or stack[-1] == "(":
                    queue.append(stack.pop())
                    if not stack:
                        break
                stack.append(i)
        elif i == "(":
            stack.append("(")
        elif i == ")":
            while stack[-1] != "(":
                queue.append(stack.pop())
            stack.pop()
    while stack:
        queue.append(stack.pop())
    return queue


def to_solve_postfix(ex: list):
    stack = []
    s = ""
    for i in ex:
        if is_digit(i):
            stack.append(int(i))
            continue
        num1 = stack.pop()
        num2 = stack.pop()
        if i == "+":
            num3 = num1 + num2
            s += f"Складываем {num1} и {num2};"
        elif i == "-":
            s += f"Вычитаем {num1} из {num2};"
            num3 = num2 - num1
        elif i == "*":
            s += f"Перемножаем {num1} и {num2};"
            num3 = num2 * num1
        elif i == "/":
            s += f"Делим {num2} на {num1};"
            num3 = num2 / num1
        stack.append(int(num3))
    return round(num3), s


def ans_to_more_op(ex: str):
    a = to_postfix(ex)
    return to_solve_postfix(a)


def addition_substraction(a, b):
    if b < 0:
        return f"{a} - {abs(b)}", a + b, f"Посчитать {a} - {abs(b)}"
    else:
        return f"{a} + {b}", a + b, f"Посчитать {a} + {b}"


def multiplication(a, b):
    return f"{a} * {b}", a * b, f"Посчитать {a} * {b}"


def division(a, b):
    return f"{a * b} / {a}", b, f"Посчитать {a * b} / {a}"


def hooks(args: tuple):
    act_available = ["+", "-", "*", "/"]
    act = random.choice(act_available)
    if act == "/":
        if args[0] * args[1] < 0 and args[1] < 0:
            num = f"( {abs(args[0] * args[1])} / {abs(args[1])} )"
        else:
            num = f"( {args[0] * args[1]} / {args[1]} )"
    else:
        if args[1] < 0:
            if act == "+":
                num = f"( {args[0]} - {abs(args[1])} )"
            elif act == "-":
                num = f"( {args[0]} + {abs(args[1])} )"
            else:
                num = f"( {args[0]} {act} {args[1]} )"
        else:
            num = f"( {args[0]} {act} {args[1]} )"
    if eval(num) == 0:
        num = num.split(" ")
        num[-2] = str(args[1] + random.randint(1, 5))
        num = " ".join(num)
    return num


def more_operations(*args, mode=0):
    if mode == 0:
        args = list(args)
        act_available = ["+", "-", "*", "/"]
        s = list()
        s.append(str(args.pop()))
        while args:
            if not args:
                break
            s.append(random.choice(act_available))
            if s[-1] == "/":
                denominator = args.pop()
                s[-2] = str(denominator * int(s[-2]))
                s.append(str(denominator))
                act_available.remove("/")
                act_available.remove("*")
                if int(s[-1]) < 0 and int(s[-3]) < 0:
                    s[-1] = s[-1][1:]
                    s[-3] = s[-3][1:]
            elif s[-1] == "*":
                s.append(str(args.pop()))
                act_available.remove("/")
                act_available.remove("*")
            else:
                s.append(str(args.pop()))
                if not "/" in act_available:
                    act_available.append("/")
                    act_available.append("*")
                if int(s[-1]) < 0:
                    if s[-2] == "-":
                        s[-1] = s[-1][1:]
                    if s[-2] == "+":
                        s[-2] = "-"
                        s[-1] = s[-1][1:]
        s = " ".join(s)
        return s, *ans_to_more_op(s)
    elif mode == 1:
        args = list(args)
        act_available = ["+", "-", "*", "/"]
        num_available = ["n", "()"]
        s = list()
        hooks_not_used = True
        if random.choice(num_available) == "()":
            s.append(hooks((args.pop(), args.pop())))
            hooks_not_used = False
        else:
            s.append(str(args.pop()))
        while args:
            if len(args) == 1:
                num_available.remove("()")
            elif len(args) == 2 and hooks_not_used:
                num_available.remove("n")
            s.append(random.choice(act_available))
            if s[-1] == "/":
                act_available.remove("/")
                act_available.remove("*")
                if random.choice(num_available) == "()":
                    denominator = hooks((args.pop(), args.pop()))
                    hooks_not_used = False
                else:
                    denominator = args.pop()
                if type(denominator) == str and not is_digit(s[-2]):
                    s[-2] = f"{round(eval(denominator))} * " + s[-2]
                elif type(denominator) == str and is_digit(s[-2]):
                    s[-2] = str(round(round(eval(denominator)) * int(s[-2])))
                elif type(denominator) == int and not is_digit(s[-2]):
                    s[-2] = f"{denominator} * " + s[-2]
                elif type(denominator) == int and is_digit(s[-2]):
                    s[-2] = str(round(denominator * int(s[-2])))
                s.append(str(denominator))

                if is_digit(s[-1]) and is_digit(s[-3]):
                    if int(s[-1]) < 0 and int(s[-3]) < 0:
                        s[-1] = s[-1][1:]
                        s[-3] = s[-3][1:]
            elif s[-1] == "*":
                if random.choice(num_available) == "()":
                    n = hooks((args.pop(), args.pop()))
                    hooks_not_used = False
                else:
                    n = args.pop()
                s.append(str(n))
                act_available.remove("/")
                act_available.remove("*")
            else:
                if random.choice(num_available) == "()":
                    n = hooks((args.pop(), args.pop()))
                    hooks_not_used = False
                else:
                    n = args.pop()
                s.append(str(n))
                if not "/" in act_available:
                    act_available.append("/")
                    act_available.append("*")
                if is_digit(s[-1]):
                    if int(s[-1]) < 0:
                        if s[-2] == "-":
                            s[-1] = s[-1][1:]
                        if s[-2] == "+":
                            s[-2] = "-"
                            s[-1] = s[-1][1:]
        s = " ".join(s)
        try:
            return s, *ans_to_more_op(s)
        except Exception as ex:
            print(type(ex).__name__, s)


if __name__ == "__main__":
    pass