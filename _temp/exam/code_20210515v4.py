logs = ["60 12 sign-in","80 20 sign-out","10 20 sign-in","60 20 sign-out"]
maxSpan = 100








logs.sort()
while_count = True
logs_len = len(logs)
logs_i = 0

sum_c = 0

result_c = []
test1 = []
test2 = []
print('카운트')
print(logs_len)

while while_count:
    if logs_len-1 <= logs_i:
        while_count = False
    else:
        #배열 비교
        test1 = logs[logs_i].split(' ')
        print(test1)
        test2 = logs[logs_i+1].split(' ')
        print(test2)

        if test1[0] == test2[0]:
            sum_c = int(test2[1])-int(test1[1])
            if maxSpan - sum_c >= 0:
                result_c.append(test1[0])
            print('같음')
            print(test1[0])
            logs_i += 2
            print('카운트!!')
            print(logs_i)
        else:
            print('다름')
            print(test1[0])
            logs_i += 1
            print('카운트!!')
            print(logs_i)

result_c = list(map(int, result_c))
result_c.sort()
result_c = list(map(str, result_c))

print('#####')
print(result_c)
