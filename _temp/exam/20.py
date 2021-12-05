# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


#처음 시간 : 최대
#마지막 시간 : 최소
#else if : -1

#if(0<=H<=23 && 0<=M<=59)
#HH:MM ~ HH:MM

#if(1<=N<=20)

list_1 = []
list_2 = []

user_input = input()

client_1 = input()
client_2 = input()
client_3 = input()

temp1 = client_1.split(' ~ ')
temp2 = client_2.split(' ~ ')
temp3 = client_3.split(' ~ ')

for i in range(0, 2):
    if (i==0):
        temp1_1 = temp1[i]
        temp2_1 = temp2[i]
        temp3_1 = temp3[i]
        list_1.append(temp1_1)
        list_1.append(temp2_1)
        list_1.append(temp3_1)
    if (i==1):
        temp1_1 = temp1[i]
        temp2_1 = temp2[i]
        temp3_1 = temp3[i]
        list_2.append(temp1_1)
        list_2.append(temp2_1)
        list_2.append(temp3_1)


list_1.sort(reverse=True)
list_2.sort()

if (list_1[0]>=list_2[0]):
    print(-1)
else:
    awd = list_1[0] + ' ~ ' + list_2[0]
    print(awd)