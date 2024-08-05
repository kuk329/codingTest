N = int(input()) # 지방의 수
budget = list(map(int,input().split()));
M = int(input())
budget.sort()

left = 0
right = budget[-1]

def total(mid):
    result = 0
    for i in range(N):
        if budget[i]<mid:
            result+=budget[i]
        else:
            result += mid

    return result

max_money = 0
while left<=right:
    mid = (left+right)//2
    add = total(mid)
    if add > M:
        right = mid -1
    # elif add==M:
    #     print(mid)
    #     break
    else:
        if max_money<mid:
            max_money=mid
        left = mid +1



print(max_money)



