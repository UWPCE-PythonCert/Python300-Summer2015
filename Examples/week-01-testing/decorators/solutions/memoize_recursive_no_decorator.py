
memo = { 0:0, 1:1 }
def fib(n): 
    if n not in memo:
        print "calling fib({})".format(n)
        memo[n] = fib(n - 1) + fib(n - 2)
    print "memo = {}".format(memo)
    return memo[n]

if __name__ == '__main__':
    # NOTE: the output is interesting
    print fib(10)
