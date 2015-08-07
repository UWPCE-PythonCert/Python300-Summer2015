
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
gt_comparitor = lambda accum,curr: (gt(accum,curr) and accum) or curr
lt_comparitor = lambda accum,curr: (lt(accum,curr) and accum) or curr
def get_max(items):
    return [reduce(
        gt_comparitor,
        items or []
    )]


if __name__ == '__main__':

    print "[ RUNNING ]: get_max tests..."
    assert get_max([5,2,0,1]) == [5]
    assert get_max([-100,0,1,2]) == [2]
    assert get_max(['a','b','c']) == ['c']
    assert get_max(['\x00','Z','-']) == ['Z']
    print "[ PASSED ]: get_max assertions passed!"


