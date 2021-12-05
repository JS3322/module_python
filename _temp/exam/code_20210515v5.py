obstacleLanes = [2, 3, 2, 1, 3, 1]




#배열 위치
move = 0
#이동횟수
count = 0
#막힌 위치
arr = [1, 2, 3]
moving = True
temp = 0

if obstacleLanes[0] == 2:
    count += 1

while moving:
    if move == len(obstacleLanes):
        moving = False
    else:
        if len(arr) == 0:
            count += 1
            arr = [1, 2, 3]
            move += 1
        else:
            arr.remove(obstacleLanes[move])
            if len(arr) == 1:
                temp = arr[0]
                move += 1
            move += 1

print(count)
    



