
class MapSum:
    def __init__(self):
        self.hashtable = {}

    def insert(self, key, val):
        self.hashtable[key] = val

    def sum(self, prefix):
        sum_ = 0
        for key in self.hashtable:
            if key.startswith(prefix):
                sum_ += self.hashtable[key]
        return sum_
