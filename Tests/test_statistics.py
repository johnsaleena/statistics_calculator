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
        answers = CsvReader("/Tests/Data/answers.csv").data
        values = fetchRawdata(test_data, 'value')
        x = self.statistics.sample_sd(values)
        # x, z = self.statistics.sample_sd(values)
        # x = round(x, 3)
        # z = round(z, 3)
        # self.assertEqual(x, z)
        x = round(x, 3)
        for column in answers:
            self.assertEqual(x, float((column['SD'])))
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
            self.assertEqual(self.statistics.z_score(values), float((column['zscore'])))

    if __name__ == '__main__':
        unittest.main()