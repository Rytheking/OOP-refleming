  
import unittest

from france import Country

class CountryTest(unittest.TestCase):
    def testCountry(self):
        GDP : float = 170000000
        continent : str = "Europe"
        Country : Country = Country(continent, GDP)

        self.assertEqual(Country.continent,continent)
        self.assertEqual(Country.GDP,GDP)

        
if __name__ == '__main__':
    unittest.main()