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
    print "[ OUTER FRAMES ]:"
    outer = inspect.getouterframes(frame)
    outer.reverse()
    for frame_info in outer:
        frame = frame_info[0]
        args, varargs, kwargs, values = inspect.getargvalues(frame)
        print "{} with {}".format(frame_info[3],dict([(k,values[k]) for k in args]))

    filename, lineno, func_name, context, index = inspect.getframeinfo(frame)
    print "  you are here: file={} line={} function={}".format(filename,lineno,func_name)
        
    exc_type, exc_inst, exc_obj = sys.exc_info()
    if exc_obj is not None:
        print "  [ INNER FRAMES ]:"
        inner = inspect.getinnerframes(exc_obj)
        for frame_info in inner:
            frame = frame_info[0]
            args, varargs, kwargs, values = inspect.getargvalues(frame)
            print "  {} with {} @context {}".format(frame_info[3],dict([(k,values[k]) for k in args]),frame_info[4][0].strip())

        # the inner frames look exactly like this
        print traceback.format_exc()
    print "\n"
    

if __name__ == '__main__':
    #
    #  we can assume ( based on the call order )
    #  that the stack will look this from the 
    #  perspective of func_two
    #
    #  <module>
    #  <main>
    #  <func_one>
    #  <func_two>
    #
    main("baz")

'''
NOTE:
0. nicer api
1. frame information is available in all funcs
2. outer versus inner
3. outer
3. exception bubbling
4. innert
5. same as traceback
'''

