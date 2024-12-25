import sys
from itertools import permutations

input = sys.stdin.readline

k = int(input())
sign = list(input().split())
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nPr = list(permutations(numbers, k + 1))  # numbers 배열에서 k+1개를 뽑아서 순서있게 나열

# nPr.sort()  # 오름차순 정렬

def check(num):  # 해당 숫자가 부등호를 만족하는지 확인
    for i in range(k):
        if sign[i] == '<':
            if num[i] >= num[i + 1]:
                return False
        else:
            if num[i] <= num[i + 1]:
                return False
    return True

# 부등호를 만족하는
n = len(nPr)

# 최댓값 찾기
nPr.sort(reverse=True)
for num in nPr:
    if check(num):
        for n in num:
            print(n,end='')
        break

# 최솟값 찾기
print()
nPr.sort()
for num in nPr:
    if check(num):
        for n in num:
            print(n,end='')
        break
