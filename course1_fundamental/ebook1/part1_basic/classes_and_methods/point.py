class Point:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    
    # def __add__(self, other):
    #     new_point = Point()
    #     new_point.x = self.x + other.x
    #     new_point.y = self.y + other.y
    #     return new_point

    def __add__(self, other):
        new_point = Point()
        if isinstance(other, Point):
            new_point.x = self.x + other.x
            new_point.y = self.y + other.y
            return new_point
        elif isinstance(other, tuple):
            new_point.x = self.x + other[0]
            new_point.y = self.y + other[1]
            return new_point

    def print_point(self):
        print("({0}, {1})".format(self.x, self.y))

new_point = Point(3, 5)
other_point = Point(5, 5)
tuple_point = (5, 1)
print("new_point + other_point: {0}".format(new_point + other_point))
print("new_point + tuple_point: {0}".format(new_point + tuple_point))