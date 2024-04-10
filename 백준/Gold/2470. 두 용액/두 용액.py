N = int(input())
liquid = list(map(int,input().split()))

liquid.sort()
d = {}
i = 0
j = N - 1

min_value = 2_000_000_000

while i<j:
    value = liquid[i]+liquid[j]
    if abs(min_value) > abs(value):
        min_value = value

    d[value]=[liquid[i],liquid[j]]

    if value<0:
        i+=1

    elif value>0:
        j-=1

    else:
        print(liquid[i],liquid[j])
        break



a, b = d[min_value]
print(a,b)
