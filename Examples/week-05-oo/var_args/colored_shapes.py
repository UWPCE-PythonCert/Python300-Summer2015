
class Shape(object):
    def __init__(self, shapename):
        self.shapename = shapename
        super(Shape, self).__init__()

class ColoredShape(Shape):
    def __init__(self, color, **kwargs):
        self.color = color
        super(ColoredShape, self).__init__()

if __name__ == '__main__':
    cs = ColoredShape(color='red', shapename='circle')


'''
NOTE:
0. show pitfalls and bad errors
1. what other options do we have?
'''
