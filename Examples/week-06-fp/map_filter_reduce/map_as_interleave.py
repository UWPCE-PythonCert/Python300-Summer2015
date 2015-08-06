#
#  interleave items from two arrays
#
def zipper(first_items,second_items):
    results = []
    for index, item in enumerate(first_items):
        results.append((item,second_items[index]))
    return results

if __name__ == '__main__':
    assert zipper([0,1,2],[3,4,5]) == [(0,3),(1,4),(2,5)]