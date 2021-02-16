import random

r = "republic"
m = "monarchy"
f = "facist dictatorship"
em = "Emmanuel Macron"
mlp = "Marie la Pen"
lxxb = "Louis XX Bourbon"

class France:

    def __init__(self,govtype : str, head : str, population: int,year: int) -> None:
        self._govtype : str = govtype
        self._head : str = head
        self._population : str = population
        self._year : int = year
    
    def newYear(self) -> None:
        self._year = self._year + 1
        self._population = self._population*1.14

    @property
    def govtype(self):
        return self._govtype
        
    @property
    def head(self):
        return self._head

    @property
    def year(self):
        return self._year

    @property
    def population(self):
        return self._population