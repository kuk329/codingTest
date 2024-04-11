# nCr = n!/ r!(n-r)!

n,m = map(int,input().split())

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)


numerator = factorial(n) # 분자
denominator = factorial(m)*factorial(n-m) # 분모

result = numerator//denominator

print(result)
