# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math

user_input = input()
a, b = user_input.split()
a = int(a)
b = int(b)
c1 = a/b
c2 = a%b

#print(c1)
#print(c2)

#3
#6
#9
#12

#3
#5
#7
#9

#올림 3
#b+(b+1)

d_before = (a-b)/(b-1)
d_after = math.ceil(d_before + 1)

#d1 = a/(b-1)
#d2 = d1+1

print(d_after)




