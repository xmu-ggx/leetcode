
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        cur, distance = 0, []

        for item in flowerbed:
            if item == 0:
                cur += 1
            if item == 1:
                distance.append(cur)
                cur = 0
        
        distance.append(cur)
        if not flowerbed[0]: distance[0]+=1
        res = sum(self.getPlacesNum(item) for item in distance)
        print(res)
        print(distance)
        return res >= n

    def getPlacesNum(self,n):
        if n <= 1:return 0
        return n//2-1 if not n%2 else n//2



if __name__ == '__main__':
    test = [0,0,0,1,1,0,0,0]
    print(Solution().canPlaceFlowers(test,2))

