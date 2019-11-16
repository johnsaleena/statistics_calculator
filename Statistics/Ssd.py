import random
import statistics
from Calculator.Addition import addition
from Calculator.Division import division
from Calculator.Square import squaree
from Calculator.Square_rot import squar_rot
from Calculator.Subtraction import subtraction
from Statistics.Getsample import getSample
from Statistics.Mean import mean


def ssd(data):
    total = 0
    sample = random.randint(1, len(data))
    new_sample = getSample(data, sample)
    new_mean = mean(new_sample)
    for numb in new_sample:
        result = subtraction(numb, new_mean)
        sq = squaree(result)
        total = addition(total, sq)
    n = len(new_sample)
    d = division(subtraction(1, n), total)
    samp_sd = squar_rot(d)
    # actual_sd = statistics.stdev(new_sample)
    return samp_sd

# def ssd(data,sample_size):
#     total=0
#     sample = getSample(data, sample_size)
#     n = len(sample)
#     new_mean=mean(sample)
#     for numb in sample:
#         result = subtraction(numb, new_mean)
#         sq = squaree(result)
#         total = addition(total, sq)
#     d=division(subtraction(n, 1), total)
#     samp_sd = squar_rot(d)
#     return samp_sd