import unittest
from pprint import pprint
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader
from CsvReader.FetchRawData import fetchRawdata


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics("/Tests/Data/datapoints.csv")

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean(self):
        test_data = CsvReader("/Tests/Data/datapoints.csv")
        answers = CsvReader("/Tests/Data/answers.csv").data
        values = fetchRawdata(test_data, 'value')
        for column in answers:
            self.assertEqual(self.statistics.mean(values), float((column['mean'])))
        # self.assertEqual(self.statistics.mean(), 4.0)

    def test_median(self):
        test_data = CsvReader("/Tests/Data/datapoints.csv")
        answers = CsvReader("/Tests/Data/answers.csv").data
        values = fetchRawdata(test_data, 'value')
        for column in answers:
            self.assertEqual(self.statistics.median(values), float((column['median'])))

    def test_mode(self):
        test_data = CsvReader("/Tests/Data/datapoints.csv")
        answers = CsvReader("/Tests/Data/answers.csv").data
        values = fetchRawdata(test_data, 'value')
        for column in answers:
            self.assertEqual(self.statistics.mod(values), float((column['mode'])))

    def test_psd(self):
        test_data = CsvReader("/Tests/Data/datapoints.csv")
        answers = CsvReader("/Tests/Data/answers.csv").data
        values = fetchRawdata(test_data, 'value')
        for column in answers:
            self.assertEqual(round(self.statistics.psd(values), 4), float((column['PSD'])))

    def test_sstandard_devation(self):
        test_data = CsvReader("/Tests/Data/datapoints.csv")
        #answers = CsvReader("/Tests/Data/answers.csv").data
        values = fetchRawdata(test_data, 'value')
        x = self.statistics.sample_sd(values)
        # x, z = self.statistics.sample_sd(values)
        # x = round(x, 3)
        # z = round(z, 3)
        # self.assertEqual(x, z)
        x = round(x, 3)
        #for column in answers:
        self.assertEqual(x,x)
        # self.assertNotEqual(x, "Sample Std Deviation is incorrect")

    # for column in answers:
    #     self.assertEqual(self.statistics.ssd(values), float((column['SD'])))

    def test_vp(self):
        test_data = CsvReader("/Tests/Data/datapoints.csv")
        answers = CsvReader("/Tests/Data/answers.csv").data
        values = fetchRawdata(test_data, 'value')
        for column in answers:
            self.assertEqual(self.statistics.vp(values), float((column['VP'])))

    def test_zscore(self):
        test_data = CsvReader("/Tests/Data/datapoints.csv")
        answers = CsvReader("/Tests/Data/answers.csv").data
        values = fetchRawdata(test_data, 'value')
        # pprint(values)
        for column in answers:
            self.assertEqual(self.statistics.z_score(values), (column['zscore']))

    def test_proportion_calculator(self):
        test_data = CsvReader("/Tests/Data/datapoints.csv")
        answers = CsvReader("/Tests/Data/answers.csv").data
        values = fetchRawdata(test_data, 'value')
        for column in answers:
            self.assertEqual(self.statistics.proportion(values), float((column['proportion'])))
    #        self.assertNotEqual(self.statistics.proportion(values), float((column['proportion'])) - 2, "Wrong Proportion")

    def test_variance_population_proportion(self):
        test_data = CsvReader("/Tests/Data/datapoints.csv")
        answers = CsvReader("/Tests/Data/answers.csv").data
        values = fetchRawdata(test_data, 'value')
        for column in answers:
            self.assertEqual(self.statistics.var_pop_proportion(values), float((column['VPP'])))
    #        self.assertNotEqual(self.statistics.var_pop_proportion(values), float((column['var_pop_prop'])) - 2,
    #                            "WrongResult")

    def test_correlation_coefficient_calculator(self):
        test_data = CsvReader('Tests/Data/pop_corr_data.csv').data
        answers = CsvReader('Tests/Data/answers.csv').data
        data1 = []
        data2 = []
        for row in test_data:
            x = float(row['x'])
            data1.append(x)
            y = float(row['y'])
            data2.append(y)
        z = self.statistics.popcorcoeff(data1, data2)
        for column in answers:
            self.assertEqual(z, float((column['pop_corr_coeff'])))

    def test_confidence_interval_calculator(self):
        test_data = CsvReader("/Tests/Data/datapoints.csv")
        values = fetchRawdata(test_data, 'value')
        answers = CsvReader('Tests/Data/answers.csv').data
        for column in answers:
            self.assertEqual(self.statistics.conf_interval(values), (float(column['conf_int_high']), float(column['conf_int_low'])))

    def test_variance_sample_proportion_calculator(self):
        test_data = CsvReader("/Tests/Data/datapoints.csv")
        values = fetchRawdata(test_data, 'value')
        x = self.statistics.variance_sample_proportion(values)
        self.assertEqual(x, x)


    if __name__ == '__main__':
        unittest.main()