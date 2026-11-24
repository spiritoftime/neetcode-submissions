class TimeMap:
    def __init__(self):
        self.keyStore= {} #key: key, value:[value,timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyStore[key] = self.keyStore.get(key,[]) + [[value,timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.keyStore.get(key,[])
        l,r = 0,len(values)-1
        while l <=r:
            m = (l+r)//2
            mid_timestamp = values[m][1]
            if mid_timestamp == timestamp:
                res = values[m][0]
                break
            elif mid_timestamp < timestamp:
                l = m+1
                res = values[m][0]

            else:r=m-1
        return res
