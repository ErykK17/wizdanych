class Point:
    counter = []

    def __init__(self, x=0, y=0):
        """Konstruktor punktu."""
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)

p1 = Point(0,0)
p2 = Point(1,1)
p3 = Point(2,7)
p4 = Point(4,8)
p5 = Point(5,1)
p6 = Point(3,6)

print(p1.counter)
print(p2.counter)
p2.update(p4.y)
print(p1.counter)
print(p2.counter)
p1.update(1)
print(p1.counter)
print(p2.counter)
p1.update(p3.x)
print(p1.counter)
print(p2.counter)