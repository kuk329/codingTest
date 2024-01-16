import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
stickers = []
for _ in range(K): # 스티커 정보 입력
    a,b = map(int,input().split())
    stickers.append([list(map(int,input().split())) for _ in range(a)])

def check(sticker):
    n = len(sticker) # 스티커 행 길이
    m = len(sticker[0]) # 스티커 열 길이
    for i in range(0,N-n+1): # 노트북에서 스티커를 붙일 스티커 시작 위치(왼쪽 위) 찾기
        for j in range(0,M-m+1):
            if stick(i,j,n,m,sticker): # 해당 위치를 시작으로 스티커를 붙일수 있는지 확인
                return True

    return False

def stick(i,j,n,m,sitcker):
    able = True
    for x in range(n):
        for y in range(m):
            if sitcker[x][y]==1: # 스티커가 색칠되어 있다면
                if notebook[x+i][y+j]==0: # 해당 노트북 위치는 비어있어야 한다.
                    pass
                else:
                    able = False
                    break # 두번째 for 문 종료
        if not able: # 첫번째 for문 종료
            break
    
    if able: # 해당 스티커를 해당 위치에 붙일수 있으면 붙이기
        for x in range(n):
            for y in range(m):
                if sitcker[x][y]==1:
                    notebook[x+i][y+j]=1 # 1로 변경

    return able


def rotate(sticker):
    n = len(sticker)
    m = len(sticker[0])
    roate_sticker = [[0]*n for _ in range(m)] # 90도 회전한 결과이므로 행과 열의 길이가 바뀜
    for i in range(n):
        for j in range(m):
            roate_sticker[j][n-i-1] = sticker[i][j]

    return roate_sticker



notebook = [[0]*M for _ in range(N)] # 빈 노트북 
for s in stickers:
    if check(s): # 해당 스티커를 붙일수 있으면
        continue # 다음 스티커도 확인
    for i in range(3): # 붙일수 없으면 회전한뒤 다시 확인 90->180->270
        s = rotate(s) 
        if check(s): # 붙일수 있으면
            break #회전 멈춤

# 스티커 수가 붙여진 칸 수 출력

count = 0
for i in range(N):
    for j in range(M):
        if notebook[i][j]==1:
            count+=1

print(count)