# 영우는 지금 n개의 돌이 일렬로 놓여있는 돌다리에 있다.
# 그리도 돌다리 돌에는 숫자가 하나씩 적혀있다.
# 영우는 이 숫자가 적혀있는 만큼 오른쪽으로 점프할 수 있다.
# 이때 돌다리 밖으로는나갈 수 없다.
# 영우는 이 돌다리에서 자기가 방문 가능한 돌들의 개수를 알고싶어 한다.
# 돌다리에 써있는 숫자 만큼 오른쪽으로 점프 가능
# 돌다리 1 ~ n
n = int(input())
stones = [0]
stones += list(map(int,input().split()))
s = int(input())

visited = [False]*(n+1)

visited[s]=True


# 돌다리 즉 stones[i] 값 을 idx에서 빼면 왼쪽 더하면 오른쪽
cnt = 0

def go(i):
    global cnt
    visited[i] = True
    cnt+=1
    jump = stones[i]
    # 왼쪽
    left = i - jump
    if left>=1 and not visited[left]:
        go(left)

    right = i + jump
    if right<=n and not visited[right]:
        go(right)



go(s)
print(cnt)


