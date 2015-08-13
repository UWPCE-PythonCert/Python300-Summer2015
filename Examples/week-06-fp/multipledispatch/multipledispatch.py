# An exploration of the multipledispatch module.
#
# http://multiple-dispatch.readthedocs.org/
# https://github.com/mrocklin/multipledispatch

from multipledispatch import dispatch


@dispatch(int, int)
def add(x, y):
    return x + y


@dispatch(object, object)
def add(x, y):
    return "%s + %s" % (x, y)


if __name__ == '__main__':
    # print("Adding two integers: "
    add(2, 2)
    add(3, "me")
