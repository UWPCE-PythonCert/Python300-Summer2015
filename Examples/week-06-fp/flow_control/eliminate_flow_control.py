
def multiples(n):
    '''
    take an int and return product of itself

    :param n: int
    :return: int product or 0 if falsey
    '''
    if n is None:
        n = 0
    return n*n

if __name__ == '__main__':

    print "[ RUNNING ]: multiples tests..."
    assert multiples(-1) == 1
    assert multiples(0) == 0
    assert multiples(-4) == 16
    assert multiples(4) == 16
    assert multiples(None) == 0
    print "[ PASSED ]: multiples tests passed!"


