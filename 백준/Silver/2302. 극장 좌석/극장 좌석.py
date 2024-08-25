N = int(input())
M = int(input())

seat = [0]*(N) # 실제 좌석 번호는 0 ~ N-1 이라고 두고 품
vip = []
for _ in range(M):
    vip.append(int(input())-1) # 나중에 헷갈리지 않기위해 실제 좌석 번호 -1 로 입력

result = 1


def dp(n): #
    d = [0] * (n + 1)
    if n==1 or n==2:
        return n
    d[1] = 1
    d[2] = 2

    for i in range(3,n+1):
        d[i] = d[i-1] + d[i-2]

    return d[n]


# 고정좌석을 기준으로 배열을 쪼갠다.
s = 0
for v in vip:
    arr = seat[s:v]
    s = v + 1 # 배열 시작 위치 (인덱스)

    if len(arr)>0:
        result *= dp(len(arr))


arr = seat[s:]
if len(arr) > 0:
    result *= dp(len(arr))
print(result)




