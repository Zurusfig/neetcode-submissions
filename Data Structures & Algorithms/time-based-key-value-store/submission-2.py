class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = [(timestamp, value)]
        else:
            self.timeMap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        timeline = self.timeMap[key]
        idx = 0
        if timeline[idx][0] > timestamp:
            return ""
        l,r = 0, len(timeline) - 1
        while l <= r:
            m = l + ((r-l) // 2)
            tm, val = timeline[m]
            if tm == timestamp:
                return val
            if tm > timestamp:
                r = m - 1
            else:
                l = m + 1
                idx = m
        return timeline[idx][1]
        
