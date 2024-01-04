T = int(input())

for _ in range(T):
    string = input()
    arr = []
    chk = False
    for s in string:
        if s=="(":
            arr.append(s)
        else:
            if not arr: # 스택이 비었으면
                print("NO")
                chk = True
                break
            else: # 스택이 비지않았으면 하나 제거
                arr.pop()

   
    
    if not chk:
        if arr:
            print("NO")
        else:
            print("YES")

