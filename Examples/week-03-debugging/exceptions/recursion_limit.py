import sys; sys.setrecursionlimit(100)

i = 0
def recurse():
    global i
    i += 1
    print i
    recurse()

try:
    recurse()
except:
    pass
