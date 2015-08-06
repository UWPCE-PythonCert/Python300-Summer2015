#
#  project items in a list
#  to a new value
#
def stringify(items):
    results = []
    for item in items:
        results.append(str(item))
    return results

def ordinalfy(items):
    results = []
    for item in items:
        results.append(ord(item))
    return results

assert stringify([0,1,2]) == ['0','1','2']
assert ordinalfy(['a','b','c']) == [97,98,99]



#
#  interleave items from two arrays
#
def zipper(first_items,second_items):
    results = []
    for index, item in enumerate(first_items):
        results.append((item,second_items[index]))
    return results

assert zipper([0,1,2],[3,4,5]) == [(0,3),(1,4),(2,5)]



#
#  filtering
#
def comp(item):
    return item > 25

def zfilter(comparitor,items):
    results = []
    for item in items:
        if comparitor(item) is True:
            results.append(item)
    return results

assert zfilter(comp,[1,200,25]) == [200]



#
#  summing things up
#
def summer(items):
    result = 0
    for item in items:
        result += item
    return result

assert summer([0,1,2,3,4]) == 10



#
#  get the min or max item
#
def get_min(items):
    temp_min = items[0]
    current = None
    for item in items:
        current = item
        if current < temp_min:
            temp_min = current
    return temp_min
assert get_min([1,-100,1e+10,2]) == -100


#
#  use case
#
# import string
# import random
#
# def create():
#     while True:
#         yield ''.join(random.choice(string.ascii_uppercase) for i in range(12))
#
# def insertion_sort(items):
#     results = [0 for i in range(len(items))]
#     for i in range(1, len(items)):
#         j = i
#         while j > 0 and items[j-1] > items[j]:
#             # update results
#             results[j], results[j-1] = items[j-1], items[j]
#             # then update iterable inplace
#             items[j], items[j-1] = items[j-1], items[j]
#             j -= 1
#     return results
# x = [1,-100,2,-5]
# insertion_sort(x)
# print x

# for s in create():
#     print "[ BEFORE ]: %s" % s
#     print insertion_sort(list(s))
#     print "[ AFTER ]: %s" % s
