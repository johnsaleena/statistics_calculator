from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Square import squaree
from Calculator.Square_rot import squar_rot
from Calculator.Subtraction import subtraction
from Statistics.Mean import mean


def psd(numbers):
    num_values = len(numbers)

    result = mean(numbers)
    total = 0
    for numb in numbers:
        result2 = subtraction(numb, result)
        sq = squaree(result2)
        total = addition(total, sq)
        result3 = division(num_values, total)
    return squar_rot(result3)
