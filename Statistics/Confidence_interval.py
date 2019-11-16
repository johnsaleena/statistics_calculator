from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Division import division
from Calculator.Multiplication import multiplication
from Calculator.Square_rot import squar_rot
from Statistics.Mean import mean
from Statistics.Psd import psd


def confidence_interval(data):
    x = mean(data)
    dev = psd(data)
    z = 1.96  # for 95% confidence

    standard_error = division(dev, squar_rot(len(data)))
    conf_upper_level = round(addition(x, multiplication(z, standard_error)), 2)
    conf_lower_level = round(subtraction(multiplication(z, standard_error), x), 2)
    return conf_upper_level, conf_lower_level