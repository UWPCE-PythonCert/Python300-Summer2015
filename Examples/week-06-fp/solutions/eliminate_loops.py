
def running_sum(start,numbers):
    total = start + numbers[0]
    for current_index,value in enumerate(numbers,1):
        if current_index == len(numbers):
            return total
        total += numbers[current_index]

def running_sum(start,current_numbers):
    if len(current_numbers) == 0:
        #print "[ STOP ]: returning %i" % start
        return start
    #print "[ ADDING ]: %i += %i" % (start,current_numbers[0])
    total = start + current_numbers[0]
    #print "[ NEW TOTAL ]: %i" % total
    return running_sum(total, current_numbers[1:])

if __name__ == '__main__':
    assert running_sum(0,range(11)) == sum(range(11),0)
    assert running_sum(1,range(4))  == sum(range(4),1)
    assert running_sum(0,range(1))  == sum(range(1),0)