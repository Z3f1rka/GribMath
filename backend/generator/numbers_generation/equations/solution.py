#n(ax+ b) + m(px+q)= c
#x = (c - nb - mq) / (na + mp)

def linear1(k, a, b):
    # kx + a = b
    if k == 1:
        if a >= 0:
            return f"x + {a} = {b}", int((b - a) / k), f"Переносим {a} с противоположным знаком"
        else:
            return f"x - {abs(a)} = {b}", int((b - a) / k), f"Переносим {a} с противоположным знаком"
    else:
        if a >= 0:
            return f"{k}x + {a} = {b}", int((b - a) / k), f"Переносим {a} с противоположным знаком;Делим {b} - {a} на {k}"
        else:
            return f"{k}x - {abs(a)} = {b}", int((b - a) / k), f"Переносим {a} с противоположным знаком;Делим {b} + {a} на {k}"


def linear2(m, k, a, n, b):
    # m(kx + a) + n = b
    # x = ((b - n) / m - a) / k
    if a < 0:
        problem = f"{m} * ({k}x - {abs(a)})"
        ans = f"Переносим {a} с противоположным знаком;Делим {b - n} - {abs(a)} на {k}"
    else:
        problem = f"{m} * ({k}x + {a})"
        ans = f"Переносим {a} с противоположным знаком;Делим {b - n} + {a} на {k}"
    if n < 0:
        problem += f" - {abs(n)} = {b}"
        ans = f"Переносим {n} с противоположным знаком;Делим {b + n} на {m};" + ans
    else:
        problem += f" + {abs(n)} = {b}"
        ans = f"Переносим {n} с противоположным знаком;Делим {b - n} на {m};" + ans
    return problem, round(((b - n) / m - a) / k, 2), ans


def linear3(m, k, a, n, p, c, b):
    # m(kx + a) + n(px + c) = b
    # x = (c - nb - mq) / (na + mp)
    if a < 0:
        problem = f"{m} * ({k}x - {abs(a)})"
    else:
        problem = f"{m} * ({k}x + {abs(a)})"
    if n < 0:
        problem = problem + f" - {abs(n)} * ({p}x"
    else:
        problem = problem + f" + {abs(n)} * ({p}x"
    if c < 0:
        problem = problem + f" - {abs(c)}) = {b}"
    else:
        problem = problem + f" + {abs(c)}) = {b}"
    # 1. раскроем скобки 2. переносим с другим знаком 3. складываем иксы
    ans = f"раскроем скобки;переносим {m * a} и {n * c} с противоположным знаком;Складываем {m * k}x и {n * p}x;Делим {(c - m * a - n * c)} на {(m * k + n * p)}"
    return problem, round((b - m * a - n * c) / (m * k + n * p), 2), ans


if __name__ == "__main__":
    print(linear1(4, 8, 9))
    print(linear2(3, -2, -4, 5, -8))
    print(linear3(3, -2, -4, 5, -8, 10, -9))