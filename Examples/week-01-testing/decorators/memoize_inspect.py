import inspect


def memoize(f):
    memo = {}
    def inner(x):
        if x not in memo:
            memo[x] = f(x)

        frame = inspect.currentframe()
        args, varargs, kwargs, values = inspect.getargvalues(frame)
        print "f({}) >>> memo = {}".format(values['x'],memo) 
        return memo[x]
    return inner

@memoize
def fib(n):
    print "calling fib({})".format(n)
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    print fib(10)
