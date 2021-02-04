import random

class France:
    r = "republic"
    m = "monarchy"
    f = "facist dictatorship"
    em = "Emmanuel Macron"
    mlp = "Marie la Pen"
    lxxb = "Louis XX Bourbon"
    def __init__(self,govtype : str,year: int, head : str, population: int) -> None:
        self._govtype : str = govtype
        self._year : int = year
        self._head : str = head
        self._population : str = population
    
    def revolution()
    {
        a :int = randrange(3)
        if(a==1)
        {
            self._govtype : str = monarchy
            self._head : str = lxxb
        }
        else if(a==2)
        {
            self._govtype : str = f
            self._head : str = mlp
        }
        else if(a==3)
        {
            self._govtype :str = r
            self._head : str = em
        }
    }

    @property
        def phase(self):
        return self._phase