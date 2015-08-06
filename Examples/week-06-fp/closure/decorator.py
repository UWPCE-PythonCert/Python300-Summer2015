# source:
# http://stackoverflow.com/questions/2796855/python-closures-example-code


def decorate(f):
    def wrapped_function():
        print("Function is being called")
        f()
        print("Function call is finished")
    return wrapped_function


@decorate
def my_function():
    print("Hello world")


if __name__ == '__main__':
    my_function()
