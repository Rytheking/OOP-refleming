import unittest

from france import France

class FranceTest(unittest.TestCase):
    def testDefaultFrance(self):
        govtype : str = "facist dictatorship"
        head : str = "mlp"
        population : int = 6000000
        year : int = 1945
        France : France = France(govtype, head, population, year)
        self.assertEqual(France.govtype,govtype)
        self.assertEqual(France.head,head)
        self.assertEqual(France.population,population)
        self.assertEqual(France.year,year)
    def testYear(self):
        govtype : str = "facist dictatorship"
        head : str = "mlp"
        population : int = 6000000
        year : int = 1945
        France : France = France(govtype, head, population, year)
        self.assertEqual(France.govtype,govtype)
        self.assertEqual(France.head,head)
        self.assertEqual(France.population,population)
        self.assertEqual(France.year,year)
        France.newYear()
        self.assertNotEqual(France.year,year+1)


