import math
import random


def test() -> list:
    values = []
    for i in range(100):
        # values.append(abs(random.gauss(0, 1)))
        values.append(abs(random.normalvariate(0, 2)))
    return values


t = test()
t.sort()
mi = t[0]
ma = t[-1]

print(t[0])
print(t[-1])


def scale(value, min_a, max_a, min_b, max_b):
    return (((value - min_a) / (max_a - min_a)) * (max_b - min_b)) + min_b


v = [math.floor(scale(v, mi, ma, 0, 100)) for v in t]
print(v)
