import sys, traceback

def one():
    one_local_var = "foo"
    two()

def two():
    two_local_var = "foo"
    three()

def three():
    # print the stack
    for num in range(3):
        frame = sys._getframe(num)
        show_frame(num, frame)

    # or
    print "\n"
    traceback.print_stack()

def show_frame(num, frame):
    print "\n"
    print "  frame     = sys._getframe(%s)" % num
    print "  function  = %s()" % frame.f_code.co_name
    print "  file/line = %s:%s" % (frame.f_code.co_filename, frame.f_lineno)
    print "  locals: %s" % frame.f_locals.keys()

if __name__ == '__main__':
    one()
  
'''
NOTE:
1. walk through, what's on the stack, where's top
2. all we did was create a traceback
'''