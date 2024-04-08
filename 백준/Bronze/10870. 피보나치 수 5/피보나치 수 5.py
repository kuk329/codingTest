# 해당 문제의 경우 점화식이 문제 안에 나와있다.
# 피보나치는 하위 결과가 상위 결과에 계속해서 포함되는 dp 대표 문제

n = int(input())
dp = [0]*21

dp[0] = 0
dp[1] = 1

if n==0 or n==1:
    print(n)
    exit()

for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])