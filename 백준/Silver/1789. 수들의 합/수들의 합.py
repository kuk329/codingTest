S = int(input())
i = 1
total = 0
while True:
    total += i
    if total > S:
        break
    i+=1


print(i-1)
