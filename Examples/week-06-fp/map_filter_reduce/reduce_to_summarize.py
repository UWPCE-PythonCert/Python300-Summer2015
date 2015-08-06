#
#  summing things up
#
def summer(items):
    result = 0
    for item in items:
        result += item
    return result

if __name__ == '__main__':
    assert summer([0,1,2,3,4]) == 10
