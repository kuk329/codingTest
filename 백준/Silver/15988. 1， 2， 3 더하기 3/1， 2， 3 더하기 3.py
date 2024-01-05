MAX = 1000000
MOD = 1000000009

T = int(input())

d = [0]*(MAX+1)
d[0] = 0 

for i in range(1,4):
        d[i] = 1


for i in range(1,MAX+1):
        for j in range(1,4):
            if j<i:
                d[i]+=d[i-j]
                d[i]%=MOD


for _ in range(T):
    n = int(input())

    print(d[n])







