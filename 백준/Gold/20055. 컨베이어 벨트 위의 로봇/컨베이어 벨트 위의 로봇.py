import sys
input = sys.stdin.readline

n, k = map(int,input().split())
a = list(map(int,input().split()))
robot = [False]*(2*n) # 로봇이 존재하는지 여부 
durability = 0 # 내구도가 0 인 칸의 개수
count = 1 # 진행 횟수 

# 번호 0 ~ n-1
#    n-2 ~ 2n-1
while True: 
    # 한칸씩 뒤로 이동
    a = a[-1:] + a[:-1]  # 가장 마지막 수 + 마지막 수를 제외한 모든 수 (벨트 위치 이동)
    robot = robot[-1:] + robot[:-1] # 로봇 이동
    if robot[n-1]: # 마지막 위치(n-1) 에 로봇이 있으면 내림
        robot[n-1] = False

    for i in range(n-2,-1,-1):  # 끝부분 부터옆으로 이동할수있는지 확인한다. n-1은 비어있으므로 그 이전칸부터 확인
        if robot[i]: # 해당 위치에 로봇이 있으면
            if robot[i+1]==False and a[i+1]>0: # 그 다음 위치에 로봇이 없고 내구도가 0 이상이면
                robot[i+1] = True # 한칸 옮김
                robot[i] = False 
                a[i+1] -= 1 # 내구도 감소
                if a[i+1]==0: # 내구도가 0이 되었으면
                    durability+=1 # 추가
    
    if robot[n-1]: # 끝 위치에 로봇이 존재하면 바로 내림
        robot[n-1] = False
    
    if a[0]>0: # 올리는 위치에 내구도가 0이 아니면
        robot[0] = True # 로봇 올림
        a[0] -= 1 # 내구도 감소
        if a[0] == 0 : # 내구도 0인지 확인
            durability+=1
    
    if durability>=k: # 한 사이클을 돌고 종료 조건 확인 
        break

    count+=1

print(count)



