from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Square import squaree
from Calculator.Subtraction import subtraction
from Statistics.Mean import mean


def vp(numbers):
    num_values = len(numbers)

    result = mean(numbers)
    total = 0
    for numb in numbers:
        result2 = subtraction(numb, result)
        sq = squaree(result2)
        total = addition(total, sq)
    return division(num_values, total)