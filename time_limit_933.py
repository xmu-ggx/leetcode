
class RecentCounter:
    def __init__(self):
        self.record = []
    
    def ping(self, t):
        self.record.append(t)
        count = 0
        for i in range(len(self.record)-1,-1,-1):
            if t - self.record[i] <= 3000:
                count += 1
            else:
                break
        return count
