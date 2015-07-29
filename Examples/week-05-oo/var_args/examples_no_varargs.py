#
#  examples without varargs in method signature
#
def positional_func(name,age,height):
    return "name={} age={} height={}".format(name,age,height)

def keyword_func(name=None,age=None,height=None):
    return "name={} age={} height={}".format(name,age,height)

def positional_and_keyword_func(name,age,height=None):
    return "name={} age={} height={}".format(name,age,height)


if __name__ == '__main__':
    expected_output = "name=greg age=20 height=6.4"

    # --------------------------------------------------------------
    # normal way
    assert positional_func("greg",20,6.4) == expected_output

    # keyword arguments can cover positional arguments
    assert positional_func(name="greg",age=20,height=6.4) == expected_output

    # tuples and lists can cover positional arguments
    # if we use *args syntax
    assert positional_func(*("greg",20,6.4)) == expected_output

    # dictionaries can cover positional arguments
    # if we use **kwargs syntax
    assert positional_func(**{"name":"greg","age":20,"height":6.4}) == expected_output

    # ----------------------------------------------------------------------
    # normal way
    assert keyword_func(name="greg",age=20,height=6.4) == expected_output

    # positional arguments can cover keyword arguments
    assert keyword_func("greg",20,6.4) == expected_output

    # tuples and lists can cover keyword arguments
    # if we use *args syntax
    assert keyword_func(*("greg",20,6.4)) == expected_output

    # dictionaries can cover keyword arguments
    # if we use **kwargs syntax
    assert keyword_func(**{"name":"greg","age":20,"height":6.4}) == expected_output

    # ----------------------------------------------------------------------
    # normal way
    assert positional_and_keyword_func("greg",20,height=6.4) == expected_output

    # positional arguments can cover ALL arguments
    assert positional_and_keyword_func("greg",20,6.4) == expected_output

    # tuples and lists can cover ALL arguments
    # if we use *args syntax
    assert positional_and_keyword_func(*("greg",20,6.4)) == expected_output

    # dictionaries can cover keyword arguments
    # if we use **kwargs syntax
    assert positional_and_keyword_func(**{"name":"greg","age":20,"height":6.4}) == expected_output

