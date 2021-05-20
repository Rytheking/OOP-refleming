import sqlite3
from typing import get_type_hints
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from datetime import datetime, date, timedelta, timezone


class Graph:
    def __init__(self, xData, yData, title, yLabel, xLabel, yMin, yMax):
        self._xData = xData
        self._yData = yData
        self._title = title
        self._yLabel = yLabel
        self._xLabel = xLabel
        self._yMin = yMin
        self._yMax = yMax

    def getHistData(self,rangeStart, rangeEnd):
        conn = sqlite3.connect('../sensorsData.db')
        curs = conn.cursor()
        query = "SELECT * FROM tentData WHERE timestamp < '"+datetime.strftime(rangeEnd, '%Y-%m-%d' )+"' AND timestamp<= '"+datetime.strftime(rangeStart, '%Y-%m-%d')+"' ORDER BY timestamp "
        #print(query)
        curs.execute(query)
        data = curs.fetchall()
        dates = []
        temps = []
        hums = []
        vpds = []
        for row in reversed(data):
            dates.append(
                datetime.strptime(str(row[0]), '%Y-%m-%d %X').replace(tzinfo=timezone.utc).astimezone(tz=None)),
            temps.append(row[1])
            hums.append(row[2])
            vpds.append(row[3])
        conn.close()
        return dates, temps, hums, vpds
    
    def savePicture(self,filename):
        plt.clf()
        plt.plot(self._xData, self._yData)
        plt.xlabel(self._xLabel)
        plt.ylabel(self._yLabel)
        plt.title(self._title)
        plt.ylim(self._yMin, self._yMax)
        plt.xticks(rotation=30)
        plt.savefig(filename)


class tempPlot(Graph):
    def __init__(self, filename, rangeStart, rangeEnd):
        self._filename = filename
        self._rangeStart = rangeStart
        self._rangeEnd = rangeEnd
        times, temps, hums, vpds = self.getHistData(rangeStart, rangeEnd)
        Graph.__init__(self,times, temps, "Temperature over Time","Temperature (F)", "Time", 50, 100)

class humPlot(Graph):
    def __init__(self, filename, rangeStart, rangeEnd):
        self._filename = filename
        self._rangeStart = rangeStart
        self._rangeEnd = rangeEnd
        times, temps, hums, vpds = self.getHistData(rangeStart, rangeEnd)
        Graph.__init__(self, times, hums, "Humidity over Time","Humdity (RH%)", "Time", 0, 100)
class vpdPlot(Graph):
    def __init__(self, filename, rangeStart, rangeEnd):
        self._filename = filename
        self._rangeStart = rangeStart
        self._rangeEnd = rangeEnd
        times, temps, hums, vpds = self.getHistData(rangeStart, rangeEnd)
        Graph.__init__(self,times, vpds, "Vapor Pressure Deficet over Time","VPD (kPA)", "Time", 0, 3)
    
    def savePicture(self,filename):
        plt.clf()
        plt.plot(self._xData, self._yData)
        plt.xlabel(self._xLabel)
        plt.ylabel(self._yLabel)
        plt.title(self._title)
        plt.ylim(self._yMin, self._yMax)
        plt.axhspan(.9,1.1, color="green", alpha=.5)
        plt.xticks(rotation=30)
        plt.savefig(filename)