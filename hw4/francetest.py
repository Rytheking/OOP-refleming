import unittest

from france import France

class FranceTest(unittest.TestCase):
    def testDefaultFrance(self):
        govtype : str = "facist dictatorship"
        head : str = "mlp"
        population : int = 6000000
        year : int = 1945
        france : France = France(govtype, head, population, year)
        self.assertEqual(france.govtype,govtype)
        self.assertEqual(france.population,population)
        self.assertEqual(france.year,year)
    def testYear(self):
        govtype : str = "facist dictatorship"
        head : str = "mlp"
        population : int = 6000000
        year : int = 1945
        france : France = France(govtype, head, population, year)
        self.assertEqual(france.govtype,govtype)
        self.assertEqual(france.head,head)
        self.assertEqual(france.population,population)
        self.assertEqual(france.year,year)
        france.newYear()
        self.assertEqual(france.year,year+1)
        self.assertEqual(france.population,population*1.14)

if __name__ == '__main__':
    unittest.main()


