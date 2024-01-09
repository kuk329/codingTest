from heapq import heappush, heappop, heapify

n, m = map(int, input().split())
cards = list(map(int, input().split()))

heapify(cards)
for _ in range(m):
    first = heappop(cards)
    second = heappop(cards)
    add = first + second
    heappush(cards, add)
    heappush(cards,add)

print(sum(cards))
