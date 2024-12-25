# 2309

from itertools import combinations


arr = [int(input()) for _ in range(9)] # 키 9개 입력받음.

total = sum(arr)  # 9명 난쟁이 키 총합

out=[]

for a,b in combinations(arr,2):
    if total-(a+b) == 100:
        out.append(a)
        out.append(b)
        break


arr.sort() # 정렬

for i in range(9):
    if arr[i] not in out:
        print(arr[i])
