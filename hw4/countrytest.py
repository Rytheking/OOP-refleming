import unittest

from france import Country

class CountryTest(unittest.TestCase):
    def testCountry(self):
        GDP : float = 170000000
        continent : str = "Europe"
        country : Country = Country(continent, GDP)

        self.assertEqual(country.continent,continent)
        self.assertEqual(country.GDP,GDP)

        
if __name__ == '__main__':
    unittest.main()