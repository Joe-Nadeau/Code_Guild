# The following code is broken in at least six ways. It is your job to fix it. 
# The program is supposed to take a user entered temperature value, a user entered 
# temperature unit, and a unit to convert to, then output the appropriate 
# conversion. The conversions should be correct, I checked them quickly, but 
# I'm fairly sure they're right. At any rate, the main point is to figure out 
# how the code is broken, and fix it.

# We'll use this code in another exercise.

def convert_to_c(temp_input):
  return ((9 / 5) * temp_input) + 32

def convert_to_f(temp_input):
  return (5 / 9) * (temp_input - 32)

def main():
  
  temp_input = float(input('enter a temperature: '))
  convert_from_unit = input('enter a unit: ')
  convert_to_unit = input('enter a unit to convert to: ')
  converted_temp = ''

  if convert_to_unit in ('c', 'C'):
    converted_temp = convert_to_f(temp_input)
  elif convert_to_unit in ('f', 'F'):
    converted_temp = convert_to_c(temp_input)
  else:
    print('no temp entered')
  
  print(converted_temp)

main()