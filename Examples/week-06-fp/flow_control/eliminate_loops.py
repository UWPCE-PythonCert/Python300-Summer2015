
def running_sum(total,numbers):
    total = total + numbers[0]
    for current_index,value in enumerate(numbers,1):
        if current_index == len(numbers):
            return total
        total += numbers[current_index]

if __name__ == '__main__':
    final = running_sum(0,range(11))
    print "[ FINAL VALUE ]: %s" % final
    assert running_sum(0,range(11)) == sum(range(11))