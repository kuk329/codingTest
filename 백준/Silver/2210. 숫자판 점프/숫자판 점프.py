import sys
input = sys.stdin.readline
arr = []

for _ in range(5):
    arr.append(list(map(int,input().split())))

dir = [(0,1),(1,0),(-1,0),(0,-1)]

group = set()

def dfs(x,y,s): # 시작 위치부터 탐색하면서 만들 수 있는 숫자 탐색
    s += str(arr[x][y])

    if len(s)==6:
        group.add(s)
        return

    for i in range(4):
        nx = x + dir[i][0]
        ny = y + dir[i][1]

        if nx>=0 and nx<5 and ny>=0 and ny<5:
            dfs(nx,ny,s)


for i in range(5):
    for j in range(5):
        dfs(i,j,"")


print(len(group))