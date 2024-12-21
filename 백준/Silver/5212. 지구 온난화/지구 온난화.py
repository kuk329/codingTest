R, C = map(int,input().split()) # 지도 크기를 입력받음
arr = [] # 지도

# 지도 정보를 입력받음
for _ in range(R):
    arr.append(list(input()))


# 어떤 섬이 바다로 변할지 확인
dir = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우
change = [] # 바다로 변할 섬의 위치
cnt = 0
for i in range(R):
    for j in range(C):
        cnt = 0
        if arr[i][j]=='X': # 해당 지점이 섬인경우
            for k in range(4): # 4면을 확인
                nx = i + dir[k][0]
                ny = j + dir[k][1]
                if nx>=0 and nx<R and ny>=0 and ny<C:
                    if arr[nx][ny]=='.':
                        cnt+=1
                else:
                    cnt+=1
            if cnt>=3:
                change.append((i,j))

# 섬을 바다로 변경
for a,b in change:
    arr[a][b] = '.'


# 지도 줄이기
minX = R
maxX = 0
minY = C
maxY = 0

for x in range(R):
    for y in range(C):
        if arr[x][y] == 'X':
            minX = min(minX, x)
            maxX = max(maxX, x)
            minY = min(minY, y)
            maxY = max(maxY, y)

# 6. 최소 크기에 맞게 지도를 출력합니다.
for i in range(minX, maxX + 1):
    for j in range(minY, maxY + 1):
        print(arr[i][j], end='')
    print()

