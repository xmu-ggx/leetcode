
class Solution:
    def checkStraightLine(self, coordinates):
        if coordinates[0][0] == coordinates[1][0]:
            for item in coordinates:
                if item[0] != coordinates[0][0]:
                    return False
            return True
        else:
            k = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
            for i in range(1, len(coordinates)):
                temp = (coordinates[i][1] - coordinates[0][1]) / (coordinates[i][0] -coordinates[0][0])
                if temp != k:
                    return False
            return True

