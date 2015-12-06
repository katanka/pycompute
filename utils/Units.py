from collections import defaultdict
import re

class Units(object):

    def __init__(self, string=''):

        if len(string) > 0 and ( string[0] in {'*', '/', '^'} or string[-1] in {'*', '/', '^'} ):
            raise ValueError( 'invalid unit string \'' + string + '\'' )

        # explode exponents
        exponents = re.findall('[^/\*]\^-?[0-9]+', string)
        for exp in exponents:
            arr = exp.split( '^' )
            unit = arr[0]
            power = int(arr[1])
            if power > 0:
                string = string.replace( exp, '*'.join( unit for _ in range(power) ) )
            elif power < 0:
                string = string.replace( exp, unit + '/' + '/'.join( unit for _ in range(-power+1) ) )
            else:
                string = string.replace( exp, '' )

        self.units = defaultdict(int)

        first_split = string.split('*')
        mult = []
        div = []

        for x in first_split:
            second_split = x.split('/')
            mult += second_split[0]
            div += second_split[1:]

        for unit in mult: self.units[unit] += 1
        for unit in div: self.units[unit] -= 1

        self.units = {k:v for (k,v) in self.units.iteritems() if v != 0}


    def __str__(self):
        return ' * '.join('%s^%d' % (key, value) for key, value in self.units.iteritems())