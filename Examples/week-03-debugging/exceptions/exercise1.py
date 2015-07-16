import sys, inspect, traceback

def main(x):
    try:
        format_frame_info( inspect.currentframe() )
        func_one(x)
    except:
        format_frame_info( inspect.currentframe() )
        pass

def func_one(y):
    format_frame_info( inspect.currentframe() )
    func_two(y)

def func_two(z):
    format_frame_info( inspect.currentframe() )
    raise Exception("bad foobars in here")

def format_frame_info(frame):
    print "[ FRAMES ]:"
    frames = inspect.stack() 
    for i in frames:
        print i

    print "[ TRACES ]:"
    trace = inspect.trace()
    for i in trace:
        print i

    print "\n"

if __name__ == '__main__':
    main("baz")


