class UndergroundSystem:

    def __init__(self):
        self.travelDetails = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travelDetails[id] = {
            'startStation': stationName,
            'checkInTime': t 
        }
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:

        startStation, checkInTime = self.travelDetails[id]['startStation'], self.travelDetails[id]['checkInTime']

        journey = (startStation, stationName)

        if journey not in self.travelDetails:
            self.travelDetails[journey] = {'totalTime': 0, 'count': 0}

        self.travelDetails[journey]['totalTime'] += (t - checkInTime)
        self.travelDetails[journey]['count'] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        journey = (startStation, endStation)
        if journey in self.travelDetails:
            return self.travelDetails[journey]['totalTime'] / self.travelDetails[journey]['count']
        else:
            return None
