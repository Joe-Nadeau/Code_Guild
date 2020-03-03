# PDX Code Guild
# Lab 5
# Emoticon generator

import random

eyeses = ['B', '8', ':', ';', 'X']
noses = ['C', '3', 'o','0', 'O', '>', '<']
mouths = ['D', '(', ')', ']', '[', 'O', 'P', 'b']
x = 0

while x < 5:
    
    print(random.choice(eyeses) + random.choice(noses) + random.choice(mouths) )
    x += 1

