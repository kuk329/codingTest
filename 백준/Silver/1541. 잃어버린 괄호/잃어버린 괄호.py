expression = input()
digit = [str(i) for i in range(0,10)]
op = '+'
tmp = []
num = ''
for e in expression:

    if e in digit:
        num+=e
    else:
        if op =="+":
            tmp.append(int(num))
        else:
            tmp.append(-int(num))
        if e=="+": # +
            op = e
        else: # -
            op = e
        num = ""

if op=="+":
    tmp.append(int(num))
else:
    tmp.append(-int(num))

result = 0
minus = False

for num in tmp:
    if num<0:
        minus=True

    if minus:
        if num>0:
            result-=num
        else:
            result+=num
    else:
        result+=num

print(result)



