N,K = map(int,input().split())
count = 0
for i in range(N+1): # N시 까지 반복
    if i<10:
        h = '0'+str(i)
    else:
        h = str(i)
    for j in range(0,60):
        if j<10:
            m = '0'+str(j)
        else:
            m = str(j)
        for l in range(0,60):
            if l<10:
                s = '0'+str(l)
            else:
                s = str(l)
            clock = h + m + s

            if str(K) in clock:
                count+=1

print(count)

