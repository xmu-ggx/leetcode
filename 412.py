
class Solution:
    def fizzBuzz(self, n:int):
        res = []
        for i in range(1, n+1):
            res.append(self.replace_Rule(i))
        return res

    def replace_Rule(self, num):
        if num % 3 == 0 and num % 5 ==0:
            return "FizzBuzz"
        elif num % 5 == 0:
            return "Buzz"
        elif num % 3 ==0:
            return "Fizz"
        else:
            return str(num)

if __name__ == '__main__':
    print(Solution().fizzBuzz(15))

