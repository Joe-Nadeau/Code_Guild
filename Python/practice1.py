# PDX Code Guild
# Practice 1: Fundamentals
# Joey Nadeau

# Problem 1

def is_even(x):

    if x % 2 == 0:
        return True
    elif x % 2 != 0:
        return False

#print(is_even(7))
#print(is_even(8))

# Problem 2

def opposite(a, b):

    if a < 0 and b >= 0:
        return True
    elif a >= 0 and b < 0:
        return True
    else:
        return False

# print(opposite(-1, 2))
# print(opposite(2, -8))
# print(opposite(2, 5))
# print(opposite(-1, -3))

# Problem 3

def near_100(num):

    if num >= 90 and num <= 110:
        return True
    else:
        return False

# print(near_100(10))
# print(near_100(99))
# print(near_100(178))
# print(near_100(110))

# Problem 4

def max_of_three(a, b, c):

    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c

# print(max_of_three(1, 3, 8))
# print(max_of_three(8, 3, 1))
# print(max_of_three(1, 8, 3))

# Problem 5

def power_of_2(a):

    power = 0
    while (power) < 21:
        print(a**(power))
        power += 1
    
        
print(power_of_2(2))