
def running_sum(start,numbers):
    '''
    return the sum of the numbers list

    >>> running_sum(0,[0,1,2,3])
    6
    >>> running_sum(1,[0,1,2,3])
    7

    :param total:
    :param numbers:
    :return: summed integer
    '''
    total = start + numbers[0]
    for current_index,value in enumerate(numbers,1):
        if current_index == len(numbers):
            return total
        total += numbers[current_index]

if __name__ == '__main__':
    assert running_sum(0,range(11)) == sum(range(11),0)
    assert running_sum(1,range(4))  == sum(range(4),1)
    assert running_sum(0,range(1))  == sum(range(1),0)
    print "[ PASSED ]: all assertions met..."