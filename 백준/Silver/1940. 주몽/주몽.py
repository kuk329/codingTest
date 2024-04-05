
N = int(input())
M = int(input())
nums = list(map(int,input().split()))

nums.sort()

i = 0
j = N - 1


cnt = 0

while i<j:
    add = nums[i]+nums[j]
    if add>M:
        j-=1
    if add<M:
        i+=1
    if add==M:
        cnt+=1
        j-=1
        i+=1

print(cnt)
