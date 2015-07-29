
class ConstrainedInt(int):

    def __new__(cls, value):
        value = value % 256
        self = super( ConstrainedInt, cls ).__new__(cls, value)
        return self


if __name__ == '__main__':
    c = ConstrainedInt( 200 )
    assert c == 200
    c = ConstrainedInt( 257 )
    assert c == 1
