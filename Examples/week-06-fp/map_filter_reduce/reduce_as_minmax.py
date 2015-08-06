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

if __name__ == '__main__':
    assert get_min([1,-100,1e+10,2]) == -100
