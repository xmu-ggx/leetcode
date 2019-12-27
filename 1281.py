
class Solution:
    def subtractProductAndSum(self, n):
        product_, sum_ = 1, 0
        for item in [int(x) for x in str(n)]:
            product_ *= item
            sum_ += item
        return product_ - sum_
