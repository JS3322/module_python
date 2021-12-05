obstacleLanes = [2, 3, 2, 1, 3, 1]



#stay 자동자 위치
stay = 2
#move 이동해야할 위치
move = 2
move = obstacleLanes[count]
#stone 장애물
stone = 0

if stay == move:
    count += 1
    stone = obstacleLanes[count]
    if stone == 1:


#이동횟수
count = 0
#막힌 위치
arr = [1, 2, 3]
moving = True
temp = 0

while moving:
    if move == len(obstacleLanes):
        moving = False
    else:
        if len(arr) == 0:
            count += 1
            arr = [1, 2, 3]
            move += 1
        elif len(arr) == 1:
            temp = arr[0]
            move += 1
        else:
            arr.remove(obstacleLanes(move))
            move += 1
    



