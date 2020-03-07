# PDX Code Guild
# Lab 9
# Unit Converter
# Joey Nadeau

def main():

    print('This program will convert units of measure for distance into meters for you.')
    
    def feet_to_meters():
        
        dist_feet = float(input('Enter the distance in feet:  '))
        dist_FtM = dist_feet * 0.3048
        print(f"{dist_feet} feet is {dist_FtM} meters.")

    def meters_to_meters():

        dist_meters = float(input('Enter the distance in meters: '))
        dist_MtM = dist_meters * 1
        print(f"{dist_meters} meters is {dist_MtM} meters....seems kind of obvious.")

    def kms_to_meters():

        dist_kilometers = float(input('Enter the distance in kilometers: '))
        dist_KMtoM = dist_kilometers * 1000
        print(f'{dist_kilometers} kilometers is {dist_KMtoM} meters.')

    def miles_to_meters():

        dist_miles = float(input('Enter the distance in miles:  '))
        dist_MitoM = dist_miles * 1609.34
        print(f'{dist_miles} miles is {dist_MitoM} meters.')

    unit_of_measure = input('\n Which unit of measure would you like to convert to meters? The options are: \n feet\n meters\n kilometers\n miles \n').lower()

    if unit_of_measure == 'feet': 
        feet_to_meters()
    elif unit_of_measure == 'meters':
        print('You\'re reall going to make me do this?....ok, here we go')
        meters_to_meters()
    elif unit_of_measure == 'kilometers':
        kms_to_meters()
    elif unit_of_measure == 'miles':
        miles_to_meters()

main()