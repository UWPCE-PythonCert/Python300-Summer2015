
class FibIter(object):
    """
    TODO: this isn't a real iterable
    """

    def __init__(self,N):
        # TODO: what goes here? 
        self.N = N

    def __iter__(self): 
        # TODO: what goes here?
        return self

    def run(self):
        """
        TODO: how can we refactor
        the below code 
        and the function signature
        to be a useful iterable?
        """
        a, b = 0, 1
        for i in range(0, self.N):
            print a,b
            a, b = b, a + b
        return a

if __name__ == '__main__':
    f = FibIter(10)
    print f
    print f.run()
    
