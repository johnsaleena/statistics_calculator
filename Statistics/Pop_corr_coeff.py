from Statistics.Mean import mean
from Statistics.Psd import psd
from Calculator.Multiplication import multiplication
from Calculator.Subtraction import subtraction
from Calculator.Division import division
from Calculator.Addition import addition


def Pop_correlation_coefficient(data1, data2):
    data1_mean = mean(data1)
    data2_mean = mean(data2)
    a = []
    b = []
    tot_sum = 0
    x = psd(data1)
    y = psd(data2)

    for i in data1:
        result1 = subtraction(data1_mean, i)
        z1 = division(result1, x)
        a.append(z1)

    for i in data2:
        result2 = subtraction(data2_mean, i)
        z2 = division(result2, y)
        b.append(z2)

    for i in range(len(data1)):
        ab = multiplication(a[i], b[i])
        tot_sum = addition(tot_sum, ab)

    result3 = division(tot_sum, subtraction(1, len(data1)))

    return result3