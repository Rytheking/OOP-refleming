from datetime import date, datetime, timedelta

class Plant:
    pass

class Cultivar:
    pass

class Cultivar:
    def __init__(self, name : str, genetics : str, parent1 : Cultivar, parent2 : Cultivar, terp_profile : list, floweringTime : int, autoflower : bool, landrace : bool):
            self._name = name
            self._genetics = genetics
            self._parent1 = parent1
            self._parent2 = parent2
            self._terp_profile = terp_profile
            self._floweringTime = floweringTime
            self._autoflower = autoflower
            self._landrace = landrace

class CannabisPlant(Cultivar, Plant):   
    def __init__(self, cultivar : Cultivar, spawn : str, state : str, planted : date, growingmedium : str, notes : str)-> None:
        self._cultivar = cultivar
        self._spawn = spawn
        self._planted = planted
        self._state= state
        self._age = datetime.today()-planted
        if(self._state=="veg"):
            self._switchDate=self._planted
            self._days_in_state=self._age
            self._harvestDate=None
        else:
            self._switchDate= datetime.strptime(input("When did you start flower?\n"), "%m/%d/%y")
            self._days_in_state=datetime.today()-self._switchDate
            self._harvestDate=self._switchDate+timedelta(days=self._floweringTime)
        self._growingmedium = growingmedium
        self._notes = notes
        self._events = []

    def flip(self) -> None:
        if(self._state=="veg"):
            self._state="flower"
            self._switchDate = date.today()
            self._days_in_state = date.today()-self._switchDate
            self._harvestDate=self._switchDate+timedelta(days=self._floweringTime)
        elif(self._state=="flower"):
            self._state="veg"
        else:
            pass
        self._switchDate = date.today()

    @property
    def cultivar(self) -> str:
        return self._cultivar._name

    @property
    def spawn(self) -> str:
        return self._spawn

    @property
    def planted(self) -> str:
        return self._planted
    
    @property
    def state(self) -> str:
        return self._state

    @property
    def age(self) -> int:
        return self._age.days
    
    @property
    def switchDate(self) -> date:
        return self._switchDate

    @property
    def days_in_state(self) -> int:
        return self._days_in_state

    @property
    def growingmedium(self) -> str:
        return self._growingmedium

    @property
    def notes(self) -> str:
        return self._notes

class carrots(Plant):
    pass


Tyrian_Kush = Cultivar("Tyrian Kush", "25% Sativa 75% Indica", None, None, ["sweet", "berry", "spice", "fuel undertones"], 63, False, False)
TK_Seed_3 = CannabisPlant(Tyrian_Kush,"Seed","veg", datetime.strptime("01/19/21","%m/%d/%y"), "soil", "")