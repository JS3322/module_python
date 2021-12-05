# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

list_0 = []

list_1 = []
list_2 = []

user_input = input()
user_len = int(user_input)

for i in range(0, user_len):
    list_0.append(input())
    temp0_0 = list_0[i].split(' ~ ')
    for j in range(0, 2):
        if (j==0):
            list_1.append(temp0_0[j])
        if (j==1):
            list_2.append(temp0_0[j])


list_1.sort(reverse=True)
list_2.sort()

if (list_1[0]>=list_2[0]):
    print(-1)
else:
    awd = list_1[0] + ' ~ ' + list_2[0]
    print(awd)