N = int(input())
drink = list(map(int,input().split()))

drink.sort() # 오름차순 정렬

for i in range(N-1):
    a = drink[i]
    b = drink[N-1]
    drink[N-1] = (a/2 + b)

print(drink[N-1])