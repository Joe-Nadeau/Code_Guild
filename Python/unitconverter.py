# PDX Code Guild
# Lab 9
# Unit Converter
# Joey Nadeau

def main():

    print('\n*************************************************************************************************\nThis program will convert units of measure for distance.\n*************************************************************************************************')
    
    def from_units_to_meters(distance, from_units):

        if from_units == 'in':
            return distance * .0254
        elif from_units == 'ft':
            return distance * .3048
        elif from_units == 'yd':
            return distance * .9144
        elif from_units == 'm':
            return distance
        elif from_units == 'km':
            return distance * 1000
        elif from_units == 'mi':
            return distance * 1609.34

    def meters_to_units(x):

        if to_units == 'in':
            return x / .0254
        elif to_units == 'ft':
            return x / .3048
        elif to_units == 'yd':
            return x / .9144
        elif to_units == 'm':
            return x / distance
        elif to_units == 'km':
            return x / 1000
        elif to_units == 'mi':
            return x / 1609.34

    

    from_units = input('What is the input unit? \n in = inches \n ft = feet \n yd = yards \n m = meters \n km = kilometers \n mi = miles \n\n')

    distance = float(input('What is the distance? \n\n'))

    to_units = input('What is the output unit? \n in = inches \n ft = feet \n yd = yards \n m = meters \n km = kilometers \n mi = miles \n\n' )

    x = from_units_to_meters(distance, from_units)
    y = meters_to_units(x)

    print(f'\n{distance} {from_units} is {y} {to_units}\n')

main()