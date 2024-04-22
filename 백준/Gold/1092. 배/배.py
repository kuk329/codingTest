import sys
input = sys.stdin.readline
N = int(input())
crane = list(map(int,input().split()))
M = int(input())
box = list(map(int,input().split()))

crane.sort(reverse=True) # 내림 차순
box.sort(reverse=True)

if crane[0]<box[0]:
    print(-1)
    exit()


time = 0

while box:
    for i in range(N):
        for j in range(len(box)):
            if crane[i]>=box[j]:
                del box[j]
                break
    time+=1
print(time)



