N = int(input())
lope = []

for _ in range(N):
    lope.append(int(input()))

lope.sort() # 오름차순 정렬  # O(N)

max_weight = 0

for i in range(N): # O(N)
    tmp = (N-i)*lope[i]
    max_weight = max(tmp,max_weight)

print(max_weight)

