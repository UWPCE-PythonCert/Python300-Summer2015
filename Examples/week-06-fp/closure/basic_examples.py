# source
# http://www.programiz.com/python-programming/closure

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


if __name__ == '__main__':
    times3 = make_multiplier_of(3)
    times5 = make_multiplier_of(5)

    print("\ntimes3(9)", times3(9))
    print("\ntimes5(4)", times5(4))
    print("\ntimes5(times3(2))", times5(times3(2)))

