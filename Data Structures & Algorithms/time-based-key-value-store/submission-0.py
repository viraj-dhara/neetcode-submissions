class TimeMap:

    def __init__(self):
        self.timestamps = defaultdict(list)
        self.values = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[(key, timestamp)] = value
        self.timestamps[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if (key,timestamp) in self.values : return self.values[(key, timestamp)]

        if self.timestamps[key] == [] : return ""
        else :
            # simple binary search:

            result = "" # to replace with -- self.values[(key,self.timestamps[key][i])]

            start = 0
            end = len(self.timestamps[key]) - 1

            while start <= end :
                mid = (start + end) // 2

                if self.timestamps[key][mid] < timestamp :
                    result = self.values[(key, self.timestamps[key][mid])]
                    start = mid + 1
                elif self.timestamps[key][mid] > timestamp :
                    end = mid - 1

            return result

        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)