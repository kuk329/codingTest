import sys
input = sys.stdin.readline

N = int(input())

register = []

for _ in range(N):
    age,name = input().split()
    register.append((int(age),name))

register.sort(key=lambda x : x[0])

for age,name in register:
    print(age,name)