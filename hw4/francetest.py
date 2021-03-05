import unittest

from france import France
from france import Country

class FranceTest(unittest.TestCase):
    def testCountry(self):
        GDP : int= 170000000
        continent : str = "Europe"
        govtype : str = "facist dictatorship"
        head : str = "mlp"
        population : int = 6000000
        year : int = 1945
        country : France = France(continent, GDP, govtype, head, population, year)

        self.assertEqual(country.continent,continent)
        self.assertEqual(country.GDP,GDP)


    def testDefaultFrance(self):
        GDP : float = 170000000
        continent : str = "Europe"
        govtype : str = "facist dictatorship"
        head : str = "mlp"
        population : int = 6000000
        year : int = 1945
        france : France = France(continent, GDP, govtype, head, population, year)
        self.assertEqual(france.govtype,govtype)
        self.assertEqual(france.population,population)
        self.assertEqual(france.year,year)
    def testYear(self):
        GDP : float = 170000000
        continent : str = "Europe"
        govtype : str = "facist dictatorship"
        head : str = "mlp"
        population : int = 6000000
        year : int = 1945
        france : France = France(continent, GDP, govtype, head, population, year)
        self.assertEqual(france.govtype,govtype)
        self.assertEqual(france.head,head)
        self.assertEqual(france.population,population)
        self.assertEqual(france.year,year)
        france.newYear()
        self.assertEqual(france.year,year+1)
        self.assertEqual(france.population,population*1.14)

if __name__ == '__main__':
    unittest.main()


