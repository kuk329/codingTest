start = list(input().split(':'))
end = list(input().split(':'))

h = int(end[0])-int(start[0])
m = int(end[1]) - int(start[1])
s = int(end[2]) - int(start[2])

if h==0 and m==0 and s==0:
    print("24:00:00")
    exit()

if s<0:
    m -= 1
    s = 60 + s
if m<0:
    m = 60 + m
    h -= 1
if h<0:
    h = h + 24

if h<10:
    h='0'+str(h)
else:
    h = str(h)
if m<10:
    m='0'+str(m)
else:
    m = str(m)
if s<10:
    s='0'+str(s)
else:
    s = str(s)
print(h+":"+m+":"+s)