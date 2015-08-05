
def get_min(items):
    '''
    pluck the min value from the list

    :param items: list of items
    :return: list with min item
    if no min determined an empty list is returned
    '''
    min_result = None
    for item in items:
        if min_result is None:
            # set it
            min_result = item
            continue

        if item < min_result:
            min_result = item
    return [] if min_result is None else [min_result]


def get_max(items):
    '''
    pluck the max value from the list

    :param items: list of items
    :return: list with max item
    if no max determined an empty list is returned
    '''
    max_result = None
    for item in items:
        if max_result is None:
            # set it
            max_result = item
            continue

        if item > max_result:
            max_result = item
    return [] if max_result is None else [max_result]


gt = lambda x,y: x > y
lt = lambda x,y: x < y
default = lambda item: item or 0
gt_comparitor = lambda accum,curr: (gt(accum,curr) and accum) or curr
lt_comparitor = lambda accum,curr: (lt(accum,curr) and accum) or curr
def get_min(items):
    return reduce(
        lt_comparitor,
        items
    )

if __name__ == '__main__':

    print "[ RUNNING ]: get_min tests..."
    assert get_min([0,1,3,5]) == 0
    assert get_min([-100,0,1,2]) == -100
    assert get_min(['a','b','c']) == 'a'
    assert get_min(['\x00','Z','-']) == '\x00'
    assert get_min([]) == []
    print "[ PASSED ]: get_min assertions passed!"

    print "[ RUNNING ]: get_max tests..."
    assert get_max([5,2,0,1]) == 5
    assert get_max([-100,0,1,2]) == 2
    assert get_max(['a','b','c']) == 'c'
    assert get_max(['\x00','Z','-']) == 'Z'
    assert get_max([]) == []
    print "[ PASSED ]: get_max assertions passed!"


