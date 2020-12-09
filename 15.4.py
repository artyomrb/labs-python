class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distn(self, smth):
        return((self.x - smth.x)**2 + (self.y - smth.y)**2)**0.5


A = Point(0,0)
B = Point(3,4)
print(A.distn(B))
