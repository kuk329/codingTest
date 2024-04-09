N = int(input())
T = list(map(int,input().split()))

T.sort()
result = []

if N%2==0: # 짝수이면
    for i in range(0, N // 2):
        result.append(T[i] + T[N - i - 1])
    print(max(result))
else:
    result.append(T[N-1])
    del T[N-1]
    N = N -1
    for i in range(0,N//2):
        result.append(T[i]+T[N-i-1])
    print(max(result))
