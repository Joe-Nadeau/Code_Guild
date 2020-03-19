#PDX Code Guild
#Lab 15
#Number to Phrase
#Joey Nadeau

import string

def main():

    def num_transmuter(user_number):
        box_1 = ()
        box_2 = ()

        if user_number in range(0, 9):
            return ones_dict.get(user_number)
        elif user_number in range(10, 19):
            return teens_dict.get(user_number)
        elif user_number in range(20, 99):
            tens_place = (user_number // 10) * 10
            ones_place = user_number % 10
            out_num = [tens_dict.get(tens_place),ones_dict.get(ones_place)]
            return "- ".join(out_num)
        elif user_number in range(100, 109):
            hundreds_place = (user_number // 100) * 100
            tens_place = ((user_number - hundreds_place) // 10) * 10
            if tens_place == None:
                tens_place = 0
            ones_place = user_number % 10
            out_num = [hundreds_dict.get(hundreds_place), tens_dict.get(tens_place), ones_dict.get(ones_place)]
            return " ".join(out_num)
        elif user_number in range(110,120):
            hundreds_place = (user_number // 100) * 100
            teens_place = (user_number % 100)
            out_num = [hundreds_dict.get(hundreds_place), teens_dict.get(teens_place)]
            return " ".join(out_num)
        elif user_number in range(120,1000):
            hundreds_place = (user_number // 100) * 100
            tens_place = ((user_number - hundreds_place) // 10) * 10
            if tens_place == None:
                tens_place = 0
            ones_place = user_number % 10
            out_num = [hundreds_dict.get(hundreds_place), tens_dict.get(tens_place), ones_dict.get(ones_place)]
            return " ".join(out_num)

    user_number = int(input('Enter a 1 or 2 digit number with the number keys: '))

    ones_dict = {0: "zero", 1: "one ", 2: "two ", 3: "three ", 4: "four ", 5: "five ", 6: "six ", 7: "seven ", 8: "eight ", 9: "nine "}
    teens_dict = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"} 
    tens_dict = {0: "", 20: "twenty ", 30: "thirty ", 40: "forty ", 50: "fifty ", 60: "sixty ", 70: "seventy ", 80: "eighty ", 90: "ninety "}
    hundreds_dict = {100: "one hundred", 200: "two hundred", 300: "three hundred", 400: "four hundred", 500: "five hundred", 600: "six hundred", 700: "seven hundred", 800: "eight hundred", 900: "nine hundred"}
    print(f'The number/s you entered is/are spelled out like this:{num_transmuter(user_number)}')

main()


