import sys
input = sys.stdin.readline
n = int(input()) # 스위치의 개수
switch = [-1]
switch+=list(map(int,input().split())) # 스위치 초기 상태
m = int(input()) # 학생수

def boy(num):
    for idx in range(1,n+1):
        if idx%num==0: # 배수이면
            if switch[idx]: # 1이면 0으로
                switch[idx]=0
            else:
                switch[idx]=1 # 0이면 1로


def girl(num):
    
    if switch[num]:
        switch[num]= 0
    else:
        switch[num] = 1

    left = num -1
    right = num +1

    while left>=1 and right<=n:
        if switch[left]==switch[right]:
            if switch[left]:
                switch[left],switch[right] = 0 , 0
            else:
                switch[left],switch[right] = 1 , 1
            left-=1
            right+=1
        else:
            break
    


for _ in range(m):
    gender , num = map(int,input().split())
    if gender == 1:
        boy(num)
    if gender == 2:
        girl(num)


for i in range(1,n+1):
    print(switch[i],end = " ")
    if i%20 == 0:
        print()

