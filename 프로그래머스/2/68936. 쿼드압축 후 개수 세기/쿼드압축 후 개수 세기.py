d = {0:0,1:0}
def go(xs,xe,ys,ye,arr):
    global zero,one
    if (xe-xs)<2:
        d[arr[xs][ys]]+=1
        return

    check = arr[xs][ys]
    for i in range(xs,xe):
        for j in range(ys,ye):
            if check!=arr[i][j]:
                go(xs,(xe+xs)//2,ys,(ye+ys)//2,arr) 
                go(xs,(xe+xs)//2,(ye+ys)//2,ye,arr)
                go((xe+xs)//2,xe,ys,(ye+ys)//2,arr)
                go((xe+xs)//2,xe,(ye+ys)//2,ye,arr)
                return

    if check==0:
        d[0]+=1
    else:
        d[1]+=1

def solution(arr):
    n = len(arr) 
    go(0,n,0,n,arr)
    return [d[0],d[1]]
