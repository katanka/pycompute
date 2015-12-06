from Units import Units

class Constant(object):
    """A constant

    Attributes:
        name: A string representing the constant's name.
        value: A number or fraction which represents the constant's value.
        units: A string which represents the units of the constant.
    """

    def __init__( self, name, value, units=Units() ):
        self.name = name
        self.value = value
        self.units = units

    @staticmethod
    def getInstanceFromString( string ):
        parts = string.split( '\t' )

        if len(parts) != 2 and len(parts) != 3:
            raise ValueError( 'malformed input string, actual length ' + `len(parts)` )

        name = parts[0]
        value_str = parts[1]
        
        if len( parts ) == 3:
            units = Units( parts[2] )
        else:
            units = Units()

        return Constant(name, value_str, units)

