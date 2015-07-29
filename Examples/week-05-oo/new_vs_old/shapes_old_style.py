class Shape():

  def __str__(self):
    return "Shape: {} with width={},height={}".format(
        self.__class__.__name__, 
        self.width, self.height
    )

class Rectangle(Shape):

  def __init__(self, width, height):
    # validate inputs:
    assert(width > 0)
    assert(height > 0)
    self.width = width
    self.height = height

  def area(self):
    """returns the area of this Rectangle"""
    return self.width * self.height

class Square(Rectangle):

  def __init__(self, length):
    self.width = length
    self.height = length

if __name__ == '__main__':
    ten_square = Square(10)
    print ten_square
    assert ten_square.height == 10
    assert ten_square.width == 10
    assert ten_square.area() == 100

    '''
    error_raised = False
    try:
        Square(0)
    except AssertionError:
        error_raised = True
    assert error_raised == True
    print "the assertion for Square(0) passed"
    '''
    
'''
TODO:
1. no object
2. how to reuse validation
3. what can we remove if we call parent?
'''
