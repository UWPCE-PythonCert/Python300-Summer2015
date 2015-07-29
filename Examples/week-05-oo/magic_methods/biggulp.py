import inspect

class BigGulp( object ):
    '''
    this is fun and evil. you will get fired 
    if you do things like this at work. only
    for illustrative purposes
    '''

    def slurpee( self, instance ):

        for name, obj in inspect.getmembers( instance ):
            if name.startswith( '__' ) or name.startswith( '_' ):
                continue

            if not inspect.isfunction( obj ) and not inspect.ismethod( obj ):
                # assume attributes, consume them
                setattr( self, name, obj )
            else:
                # consume and rebind methods to BigGulp instance
                setattr( self, name, obj.im_func.__get__( self, BigGulp ) )

        return self


    def __getattr__(self,lookup):
        print "__getattr__ on {}".format(lookup)

    def __getattribute__(self,lookup):
        print "__getattribute__ on {}".format(lookup)
        return super( BigGulp, self ).__getattribute__(lookup)

class PlainClass( object ):

    def __init__( self ):
        self.name = 'bang'
        self.description = 'sudobangbang!!'

    def get_name( self ):
        return "my name -- {}".format(self.name)
    
    def get_desc( self ):
        return "my description -- {}".format(self.description)


if __name__ == '__main__':

    plain = PlainClass() 
    
    #gulp = BigGulp().slurpee( plain )
    #print gulp.get_name()
    #print gulp.get_desc()

