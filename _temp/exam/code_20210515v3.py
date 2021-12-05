arr = [2, 1, 3]

anw = []
arr_length = len(arr)
temp = 0
count = 0
wh = True
wh_count = True
x_count = 0
    
while wh:  
    if arr_length == count:
        wh = False
    else:
        if count == 0:
            anw.append(0)
            count += 1
        else:
            temp = 0
            x_count = 0
            print('다음배열')
            while wh_count:
                if count - x_count == 0:
                    wh_count = False
                else:
                    x_count += 1
                    temp += arr[count]-arr[count-x_count]
                    print('temp count')
                    print(count)
                    print(arr[count])
                    
                    print('temp x_count')
                    print(count-x_count)
                    print(arr[count-x_count])

                    print('temp')
                    print(temp)
            anw.append(temp)
            wh_count = True
            count += 1
            

print('##########')
print(anw)