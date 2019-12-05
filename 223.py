import sys

class Solution:

    @classmethod
    def computerArea(cls,A,B,C,D,E,F,G,H):
        x = min(C,G) - max(A,E)
        y = min(D,H) - max(B,F)
        covered_area = 0 if x<0 or y<0 else x*y
        area1 = (C-A)*(D-B)
        area2 = (G-E)*(H-F)
        return area1 + area2 -covered_area

if __name__ == '__main__':
    A,B,C,D,E,F,G,H = map(int,sys.argv[1:])
    print(sys.argv[1:])
    print(Solution.computerArea(A,B,C,D,E,F,G,H))
