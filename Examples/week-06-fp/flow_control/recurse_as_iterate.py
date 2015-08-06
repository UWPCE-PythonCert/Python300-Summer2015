
def running_sum(numbers, start=0):
    if len(numbers) == 0:
        return
    total = numbers[0] + start
    print "{}".format(total)
    total = running_sum(numbers, total)
    return total

if __name__ == '__main__':
    final = running_sum([0,1,2,3,4])
    print final