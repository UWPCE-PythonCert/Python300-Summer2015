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



if __name__ == '__main__':
    assert stringify([0,1,2]) == ['0','1','2']

    assert ordinalfy(['a','b','c']) == [97,98,99]
