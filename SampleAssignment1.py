import re

hand = open('regex_sum_42.txt')
digit_Finder = []
total_Sum = 0

for line in hand:
    line = line.rstrip()
    y = re.findall('[0-9]+',line)
    if(y != []):
        digit_Finder.append(y)

for sum_Finder in digit_Finder:
    for iterator in range(0,len(sum_Finder)):
        total_Sum += int(sum_Finder[iterator])

print (total_Sum)
