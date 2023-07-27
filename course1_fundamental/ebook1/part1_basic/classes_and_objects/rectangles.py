import copy

class Point:
    """Represents a point in 2-D space."""

class Rectangle:
    """Represents a rectangle.
    attributes: width, height, corner.
    """

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def distance_between_points(x, y):
    return y-x

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

def move_rectangle(rect, dx, dy):
    new_rect = copy.deepcopy(rect)
    new_rect.corner.x += dx
    new_rect.corner.y += dy
    return new_rect

center = find_center(box)
new_rect = move_rectangle(box, 30.0, 50.0)
print(new_rect.corner.x)
print(new_rect.corner.y)
print(box.corner.x)
print(box.corner.y)