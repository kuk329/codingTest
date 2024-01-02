# === 입력 ===
n = int(input())


# == 초기 값 ==
d = [0]*(n+1) # d[i] : i 를 만드는데 필요한 최소 항의 개수

d[1] = 1

# === 계산 ===

for i in range(2,n+1):
    d[i] = i
    j=1
    while j*j<=i:
        d[i] = min(d[i],d[i-j*j]+1)
        j+=1



print(d[n])
