# 2 Classes "Points" and "Rectangle".
# Store x and y Coordinates.
# __repr__ and __eq__

class Points():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '%s, %s' % (self.x, self.y)

    def __eq__(self, other):
        return ('Point__eq__ called: %r == %r? ') % (self, other)
        return self.value == other

    def distance(self, other):
        return Point(other.x - self.x, other.y - self.y)

    def move(self, x, y):
        self.x += x
        self.y += y


class Rectangle():
    def __init__(self, top_left, width, height):
        self.top_left = top_left
        self.height = height
        self.width = width

    def __repr__(self):
        return 'Width is (%s), Height is (%s), and the Top Left point is, (%s).' % (self.width, self.height, self.top_left)

    def __eq__(self, other):
        print('Point__eq__ called: %r == %r? ') % (self, other)
        return self.value == other

    def center(self, width, height):
        new_point_x = width / 2
        new_point_y = height / 2
        return Points(new_point_x, new_point_y)

    def within(self, point):
        return (self.top_left.x <= point.x <= self.top_left.x + self.width and self.top_left.y <= point.y <= self.top_left.y + self.height)






r = Rectangle(Points(4, 5), 36, 18 )
print(r.within(Points(9,11)))
print(r.center(36, 18))
print(r)
