N = int(input())
paper = []
d = {0:0,1:0} # 0 : white , 1 : blue
for _ in range(N):
    paper.append(list(map(int,input().split())))

def divide_paper(sx,sy,ex,ey):
    if sx>ex or sy>ey:
        return
    color = paper[sx][sy]
    for x in range(sx,ex):
        for y in range(sy,ey):
            if color!=paper[x][y]: # 자른 색종이에 칸들의 색이 다 동일하지 않으면 다시 분할
                divide_paper(sx,sy,(sx+ex)//2,(sy+ey)//2) # 1 사분면
                divide_paper(sx,(sy+ey)//2,(sx+ex)//2,ey) # 2 사분면
                divide_paper((sx+ex)//2,sy,ex,(sy+ey)//2) # 3 사분면
                divide_paper((sx+ex)//2,(sy+ey)//2,ex,ey) # 4 사분면

                return

    d[color]+=1


divide_paper(0,0,N,N)


print(d[0])
print(d[1])


