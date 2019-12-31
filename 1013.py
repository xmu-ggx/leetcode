
class Solution:
    def canThreePartsEqualSum(self, A):
        if sum(A)%3:
            return False

        part_sum = int(sum(A) / 3)
        count_part = 0
        curr_sum = 0

        for i in range(len(A)):
            curr_sum += A[i]
            if curr_sum == part_sum:
                count_part += 1
                curr_sum = 0

        if count_part == 3 and i == len(A)-1:
            return True
        else:
            return False
            

