from collections import Counter

n = int(input())
A = list(map(int,input().split()))

M = int(input())
a = list(map(int,input().split()))
counter = Counter(A)

for i in a:
    if i in counter:
        print(1)
    else:
        print(0)
