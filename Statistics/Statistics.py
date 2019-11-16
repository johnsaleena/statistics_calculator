from Calculator.Calculator import Calculator
from Statistics.Confidence_interval import confidence_interval
from Statistics.Mean import mean
from Statistics.P_value import P_value
from Statistics.Pop_corr_coeff import Pop_correlation_coefficient
from Statistics.Proportion import proportion
from Statistics.SampleMean import sample_mean
from Statistics.Median import median
from Statistics.Mode import mod
from Statistics.Psd import psd
from Statistics.Ssd import ssd
from Statistics.Vp import vp
from Statistics.Vpp import var_pop_prop
from Statistics.Vsp import var_samp_prop
from Statistics.Zscore import zscore
# from Statistics.Ssd import ssd
from CsvReader.CsvReader import CsvReader


class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader(filepath)
        super().__init__()

    def mean(self, m):
        self.result = mean(m)
        return self.result

    def sample_mean(self, sample_size):
        self.result = sample_mean(self.data, sample_size)
        return self.result

    def median(self, me):
        self.result = median(me)
        return self.result

    def mod(self, mo):
        self.result = mod(mo)
        return self.result

    def psd(self, po):
        self.result = psd(po)
        return self.result

    def sample_sd(self, a):
        self.result = ssd(a)
        return self.result

    def vp(self, vp1):
        self.result = vp(vp1)
        return self.result

    def z_score(self, a):
        self.result = zscore(a)

    def proportion(self, a):
        self.result = proportion(a)
        return self.result

    def var_pop_proportion(self, a):
        self.result = var_pop_prop(a)
        return self.result

    def popcorcoeff(self, a, b):
        return Pop_correlation_coefficient(a, b)

    def conf_interval(self, a):
        self.result = confidence_interval(a)
        return self.result

    def variance_sample_proportion(self, a):
        self.result = var_samp_prop(a)
        return self.result

    def p_value(self, a):
        return P_value(a)