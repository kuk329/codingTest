N = int(input())
color = list(input())

d = {"R":0,"B":0}

d[color[0]]+=1
prev = color[0]


for i in range(1,N):
    if color[i]!=prev:
        d[color[i]]+=1
        prev = color[i]


min_group = min(d["R"],d["B"])

result = 1 + min_group

print(result)