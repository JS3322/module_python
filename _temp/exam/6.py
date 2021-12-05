# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

list_0 = []
list_temp = []

temp = 0
count = 0

check1 = 0
check2 = 0 

user_input = input().split(' ')
user_len_ga = int(user_input[0])
user_len_se = int(user_input[1])

for i in range(0, user_len_se):
    list_temp = input().split(' ')
    for j in range(0, user_len_ga):
        list_0.append(int(list_temp[j]))


#1차 검색 : 0+user_len_ga or +1
for i in range(0, user_len_ga + user_len_se):
    if (count >= user_len_ga + user_len_se):
        break
    if (i == 0 ):
        temp = list_0[i]
    else:
        check1 = list_0[count+1]
        check2 = list_0[count+user_len_ga]
        if(check1 >= check2):
            count = count+1
            temp = temp + check1
        if(check1 < check2):
            count = count + user_len_ga
            temp = temp + check2
            
print(temp)
     



#전체검색
