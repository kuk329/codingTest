import sys

input = sys.stdin.readline

H,W = map(int,input().split()) # H : 세로 , W : 가로
N = int(input())

# 스티커 정보 입력받기
stickers = []

for _ in range(N):
    r,c = map(int,input().split())
    stickers.append([r,c])

def check(x,y,z,w): # 스티커1 세로,가로 / 스티커2 세로,가로
    if (x+z)<=H and max(y,w)<=W: # 세로로 붙일때
        return True
    if(y+w)<=W and max(x,z)<=H: # 가로로 붙일때
        return True
    return False

ans = 0

# 스티커들 중에 2개 고르기 (NC2)
for i in range(N):
    for j in range(i+1,N):
        # 고른 스티커로 붙일 수 있는 경우의 수 모두 확인
        area = stickers[i][0]*stickers[i][1]+stickers[j][0]*stickers[j][1]
        if check(stickers[i][0],stickers[i][1],stickers[j][0],stickers[j][1]):
            ans = max(ans,area)

        if check(stickers[i][1],stickers[i][0],stickers[j][0],stickers[j][1]):
            ans = max(ans,area)

        if check(stickers[i][0],stickers[i][1],stickers[j][1],stickers[j][0]):
            ans = max(ans,area)

        if check(stickers[i][1],stickers[i][0],stickers[j][1],stickers[j][0]):
            ans = max(ans,area)

print(ans)

