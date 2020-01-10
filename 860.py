
class Solution:
    def __init__(self):
        self.num5 = 0
        self.num10 = 0
        self.num20 = 0

    def lemonadeChange(self, bills):
        for bill in bills:
            if bill == 5:
                self.num5 += 1

            elif bill == 10:
                if self.num5 == 0:
                    return False
                else:
                    self.num5 -= 1
                    self.num10 += 1

            else:
                if self.num10 >= 1 and self.num5 >= 1:
                    self.num10 -= 1
                    self.num5 -= 1
                    self.num20 += 1

                elif self.num5 >= 3:
                    self.num5 -= 3
                    self.num20 += 1
                    
                else:
                    return False

        return True
                
