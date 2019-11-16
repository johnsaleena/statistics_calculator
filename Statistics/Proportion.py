from Calculator.Division import division
from Calculator.Addition import addition


def proportion(data):
    count = 0
    for i in data:
        if (i % 2) == 0:
            count = addition(count, 1)
        prop = division(count, len(data))
    return prop