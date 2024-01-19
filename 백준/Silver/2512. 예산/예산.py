# 가능한 최대의 예산으로 분배

N = int(input()) # 지방의 수
arr = list(map(int,input().split()))
arr.sort() # 110 120 140 150
limit = int(input()) # 총 예산의 수


def go(s,e):
    max_money = 0

    while s<=e:
        add = 0
        mid = (s+e)//2 # 각 지방마다 분배할 예산
        for i in range(N):
            if arr[i]<mid:
                add+=arr[i]
            else:
                add+=mid
        if add > limit: # 지방에 나누어준 예산합이 총 예산보다 크면
            e = mid - 1 # 예산수를 줄임
        else: # 지방에 나누어준 예산합이 총 예산보다 작으면 (가능한 경우들)
            if max_money < mid:
                max_money = mid
            s = mid + 1

    return max_money




print(go(1,arr[-1])) # 각 지방마다 줄수있는 예산의 범위 구하기