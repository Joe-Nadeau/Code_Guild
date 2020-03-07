# PDX Code Guild
# Lab 9
# Unit Converter
# Joey Nadeau

def main():

    print('This program will convert units of measure for you.')
    
    def feet_to_meters():
        
        dist_feet = float(input('Enter the distance in feet:  '))
        dist_meters = dist_feet * 0.3048
        print(f"{dist_feet} feet is {dist_meters} meters.")

    feet_to_meters()

main()