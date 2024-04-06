N, X = map(int, input().split())
visitor = list(map(int, input().split()))

d = dict()  # 각 최대 방문인 경우 해당 방문자 수가 몇번 나왔는지 저장
start = 0
end = X - 1
total = sum(visitor[start:X])
max_total = total
d[total] = 1

while end < N - 1:
    start += 1
    end += 1
    total = (total+visitor[end]-visitor[start-1])

    if total >= max_total:
        if total not in d:
            d[total] = 1
        else:
            d[total] += 1

        max_total = total


if max_total == 0:
    print('SAD')
else:
    print(max_total)
    print(d[max_total])
