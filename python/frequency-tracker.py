class FrequencyTracker:

    def __init__(self):
        self.tracker = {}
        

    def add(self, number: int) -> None:
        if number not in self.tracker:
            self.tracker[number] = 1
        else:
            self.tracker[number] += 1

    def deleteOne(self, number: int) -> None:

        freq = self.tracker.get(number, 0)
        if not freq:
            return
        if freq == 1:
            del self.tracker[number]
        elif freq > 1:
            self.tracker[number] -= 1

    def hasFrequency(self, frequency: int) -> bool:
        for value in self.tracker.values():
            if value == frequency:
                return True
            
        return False