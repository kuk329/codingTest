def solve(lottos,index,select):
    if len(select)==6:
        print(' '.join(map(str,select)))
        return

    if len(lottos)==index: # 가장 마지막 수까지 확인했으면 더는 고를게 없음
        return

    solve(lottos,index+1,select+[lottos[index]])
    solve(lottos,index+1,select)

while True:
    n, *lottos = list(map(int,input().split()))
    if n == 0:
        break
    solve(lottos,0,[])
    print()