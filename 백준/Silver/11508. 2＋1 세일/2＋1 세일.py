N = int(input())
price = []
for _ in range(N):
    price.append(int(input()))

price.sort(reverse=True) # 내침차순 정렬

all = sum(price)
free = sum(price[2::3])
print(all-free)
