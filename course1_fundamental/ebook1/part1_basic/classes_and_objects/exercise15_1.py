from cmath import sqrt
import copy


class Circle:
    """Represents a rectangle.
    attributes: center, radius.
    """


class Point:
    """Represents a point in 2-D space."""


class Rectangle:
    """Represents a rectangle.
    attributes: width, height, corner.
    """


def point_in_circle(circle, point):
    d = sqrt(
        (point.x - circle.center.x) * (point.x - circle.center.x)
        + (point.y - circle.center.y) * (point.y - circle.center.y)
    )
    if d.real <= circle.radius:
        return True
    else:
        return False


def rect_in_circle(circle, rectangle):
    p = copy.copy(rectangle.corner)
    if not point_in_circle(circle, p):
        return False
    p.x += rectangle.width
    if not point_in_circle(circle, p):
        return False
    p.y -= rectangle.height
    if not point_in_circle(circle, p):
        return False
    p.x -= rectangle.width
    if not point_in_circle(circle, p):
        return False
    return True


def rect_circle_overlap(circle, rectangle):
    p = copy.copy(rectangle.corner)
    if point_in_circle(circle, p):
        return True
    p.x += rectangle.width
    if point_in_circle(circle, p):
        return True
    p.y -= rectangle.height
    if point_in_circle(circle, p):
        return True
    p.x -= rectangle.width
    if point_in_circle(circle, p):
        return True
    return False


circle_obj = Circle()
circle_obj.center = Point()
circle_obj.center.x = 150
circle_obj.center.y = 100
circle_obj.radius = 75

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 50.0
box.corner.y = 50.0

new_point = Point()
new_point.x = 100
new_point.y = 125
isCheck = point_in_circle(circle_obj, new_point)
print(rect_in_circle(circle_obj, box))
print(rect_circle_overlap(circle_obj, box))
