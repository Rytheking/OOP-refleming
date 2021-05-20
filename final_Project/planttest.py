import unittest

from plant import Cultivar, CannabisPlant
from datetime import datetime, date, timedelta
class PlantTest(unittest.TestCase):

    def testCultivar(self):
        name = "Tyrian Kush"
        genetics= "25% Sativa 75% Indica"
        terps = ["sweet", "berry", "spice", "fuel undertones"]
        floweringtime = 63

        Tyrian_Kush = Cultivar("Tyrian Kush", "25% Sativa 75% Indica", None, None, ["sweet", "berry", "spice", "fuel undertones"], 63, False, False)
        
        self.assertEqual(Tyrian_Kush._name,name)
        self.assertEqual(Tyrian_Kush._genetics,genetics)
        self.assertEqual(Tyrian_Kush._terp_profile,terps)
        self.assertEqual(Tyrian_Kush._floweringTime,floweringtime)

    def testCannabisPlant(self):
        cultivar = Cultivar("Tyrian Kush", "25% Sativa 75% Indica", None, None, ["sweet", "berry", "spice", "fuel undertones"], 63, False, False)
        method = "Seed"
        
        startDate = datetime.strptime("01/19/21","%m/%d/%y")
        TK_Seed_Test = CannabisPlant(cultivar, method,  "veg", startDate,"soil", "")

        self.assertEqual(TK_Seed_Test._cultivar,cultivar)
        self.assertEqual(TK_Seed_Test._spawn, method)
        self.assertEqual(TK_Seed_Test._state,"veg")
        self.assertEqual(TK_Seed_Test._planted ,startDate)
        self.assertEqual(TK_Seed_Test._age.days,(datetime.today()-startDate).days)

        
if __name__ == '__main__':
    unittest.main()