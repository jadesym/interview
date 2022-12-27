class UndergroundSystem:

    def __init__(self):
        # key: customer
        # value: (startStation, time)
        self.startTimes = {}
        # key: (startStation, endStation)
        # value: (totalTimes, numTimes)
        self.stationTimes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.startTimes: return
        self.startTimes[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.startTimes: return
        startStation, startTime = self.startTimes[id]
        del self.startTimes[id]

        station_tuples = (startStation, stationName)

        if station_tuples not in self.stationTimes:
            self.stationTimes[station_tuples] = (0, 0)
        originalTotalTimes, originalNumTimes = self.stationTimes[station_tuples]

        self.stationTimes[station_tuples] = (
            originalTotalTimes + t - startTime,
            originalNumTimes + 1
        )

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTimes, numTimes = self.stationTimes[(startStation, endStation)]
        return totalTimes / numTimes


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)