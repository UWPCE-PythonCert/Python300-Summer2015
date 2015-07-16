class CountToTen(object):
      """an iterator which returns integers from 0 to 9, inclusive"""

      def __init__(self):
          self.data = range(10)

      def __iter__(self):
          #print "__iter__" 
          return self

      def next(self):
          #print "next"
          try:
              return self.data.pop(0)
          except IndexError:
              raise StopIteration

if __name__ == '__main__':
    for x in CountToTen():
      print x

    # or consume the whole thing at once by converting to a list:
    print list(CountToTen())
