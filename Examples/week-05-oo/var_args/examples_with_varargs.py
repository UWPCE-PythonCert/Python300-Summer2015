#
#  examples using varargs in method signatures
#
def positional_vararg_func(*args):
    return "args={}".format(args)

def keyword_vararg_func(**kwargs):
    return "kwargs={}".format(sorted(kwargs.items(),key=lambda tup: tup[0]))

def both_vararg_func(*args,**kwargs):
    return "args={}".format(args) + " " + "kwargs={}".format(sorted(kwargs.items(),key=lambda tup: tup[0]))

if __name__ == '__main__':

    # --------------------------------------------------------------
    # normal way
    expected_output = "args=('greg', 20, 6.4)"
    assert positional_vararg_func("greg",20,6.4) == expected_output

    # tuples and lists can cover positional varargs
    # if we use *args syntax
    assert positional_vararg_func(*("greg",20,6.4)) == expected_output

    # note that we can pass nothing with the *args and **kwargs syntax
    assert positional_vararg_func(*()) != expected_output
    assert positional_vararg_func(**{}) != expected_output


    # ----------------------------------------------------------------------
    # normal way
    expected_output = "kwargs=[('age', 20), ('height', 6.4), ('name', 'greg')]"
    assert keyword_vararg_func(name="greg",age=20,height=6.4) == expected_output

    # dictionaries can cover keyword arguments
    # if we use **kwargs syntax
    assert keyword_vararg_func(**{"name":"greg","age":20,"height":6.4}) == expected_output

    # note that we can pass nothing with the *args and **kwargs syntax
    assert keyword_vararg_func(*()) != expected_output
    assert keyword_vararg_func(**{}) != expected_output

    # ----------------------------------------------------------------------
    # normal way
    expected_output = "args=('greg', 20) kwargs=[('height', 6.4)]"
    assert both_vararg_func("greg",20,height=6.4) == expected_output

    # positional arguments can cover ONLY the positional parts. Be careful
    expected_output = "args=('greg', 20, 6.4) kwargs=[]"
    assert both_vararg_func("greg",20,6.4) == expected_output

    # tuples and lists can cover ONLY the positional parts. Be careful
    expected_output = "args=('greg', 20, 6.4) kwargs=[]"
    assert both_vararg_func(*("greg",20,6.4)) == expected_output

    # dictionaries can cover only the keyword parts
    expected_output = "args=() kwargs=[('age', 20), ('height', 6.4), ('name', 'greg')]"
    assert both_vararg_func(**{"name":"greg","age":20,"height":6.4}) == expected_output

    # note that we can pass nothing with the *args and **kwargs syntax
    assert keyword_vararg_func(*(),**{}) != expected_output
    assert keyword_vararg_func(**{}) != expected_output
