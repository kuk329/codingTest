n , m = map(int,input().split()) 

d = {}

for _ in range(n):
    a,b = input().split()
    d[a]=b


for _ in range(m):
    find = input()
    print(d[find])


