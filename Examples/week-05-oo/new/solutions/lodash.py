class LoDash(str):

    def __new__( cls, value ):
        replaced = value.replace( '_', '_LoDash_' )
        instance = super( LoDash, cls ).__new__( cls, replaced )
        return instance


if __name__ == '__main__':
    assert LoDash( "Bang" ) == "Bang"
    assert LoDash( "Bang_boom" ) == "Bang_LoDash_boom"
    assert LoDash( "Bang_a_rang" ) == "Bang_LoDash_a_LoDash_rang"


