arr = [3, 2, 1, 3]

anw = []
temp = 0
count = 1
wh = True
wh_count = True
x_count = 0
    
while wh:  
    if arr[0] < count:
        wh = False
    else:
        if count == 1:
            anw.append(0)
            count += 1
        else:
            temp = 0
            while wh_count:
                if count - x_count == 0:
                    wh_count = False
                else:
                    x_count += 1
                    temp += abs(arr[count]-arr[count-x_count])
                    print('temp count')
                    print(count)
                    print(arr[count])
                    
                    print('temp x_count')
                    print(x_count)
                    print(arr[count-x_count])

                    print('temp')
                    print(temp)
            anw.append(temp)
            wh_count = True
            count += 1
            

print('##########')
print(anw)