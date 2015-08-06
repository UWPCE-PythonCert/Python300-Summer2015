#
#  filtering
#
def zfilter(items):
    results = []
    for item in items:
        if item > 25:
            results.append(item)
    return results

if __name__ == '__main__':
    assert zfilter([1,200,25]) == [200]