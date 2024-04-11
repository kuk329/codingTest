N = int(input())
cow = {}
count = 0
for _ in range(N):
    a,b=map(int,input().split())
    if a in cow:
        pos = cow[a]
        if pos!=b:
            count+=1
            cow[a]=b

    else:
        cow[a]=b

print(count)
