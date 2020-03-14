#PDX Code Guild
#Lab 13
#ROT13
#Joey Nadeau

import string

def main():

    user_string = input("Write a message that you wan't encrypted with a cypher: ")
    rotation = int(input("How much spice do you want on that dice?....How much rotation do you want to add to your cipher?:"))
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    #rot_13_var = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
    cyphered_string = ''
    cy_list = []
    
    def ROT13_func(cyphered_string):

        #for each character in the user's string
        for char in user_string:

            if char in lower_case:
                #looks for the character from the user's string and matches it to the corresponding character in ascii_letters. Then it stores that letter's indice in the variable to_be_replaced and adds 13 to that indice
                to_be_replaced = (lower_case.find(char) + rotation) % 26
                #looks at the indice stored in to_be_replaced, matches it to the same indice in rot_13_var and adds the character associated with that indice to cy_list.
                cy_list.append(lower_case[to_be_replaced])
            
            elif char in upper_case:
                
                to_be_replaced = (upper_case.find(char) + rotation) % 26

                cy_list.append(upper_case[to_be_replaced])

            else:
                cy_list.append(char)
        #prints cy_list as a joined string.
        print(cyphered_string.join(cy_list))
    #calls ROT13_func to run.
    ROT13_func(cyphered_string)

main()




#string.find