import random

class France:
    r = "republic"
    m = "monarchy"
    f = "facist dictatorship"
    em = "Emmanuel Macron"
    mlp = "Marie la Pen"
    lxxb = "Louis XX Bourbon"

    def __init__(self,govtype : str, head : str, population: int,year: int) -> None:
        self._govtype : str = govtype
        self._head : str = head
        self._population : str = population
        self._year : int = year
    
    def newYear() -> None:
        self._year+=1
        temp : int = randrange(5)
        if(temp==1):
            revolution

    def announcement() -> str:
        temp : str = "A revolution has happened! " +self.head+" is now in power!"
        return temp

    def revolution() -> None:
        a :int = randrange(3)
        if(a==1):
            if(self.govtype!=m):
                self._govtype : str = m
                self._head : str = lxxb
                print(announcement())
        if(a==2):
            if(self.govtype!=f):
                self._govtype : str = f
                self._head : str = mlp
                print(announcement())
        if(a==3):
            if(self.govtype!=r):
                self._govtype :str = r
                self._head : str = em
                print(announcement())
    

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