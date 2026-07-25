class TimeMap:

    def __init__(self):
        self.dict1 = defaultdict(dict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict1[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        i = timestamp
        if key not in self.dict1:
            return ""
        while i>0 and i not in self.dict1[key]:
            i-= 1
        return self.dict1[key].get(i,"")
