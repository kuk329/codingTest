

board = list(input().split('.'))
success = True
result = []

for s in board:
    if len(s)%2!=0: # 홀수
        success=False
        break
    # 짝수
    n = len(s)//2 # 2개씩 묶을때 몇묶음 나오는 지 
    n_A = n//2
    n_B = n - n_A*2
    result.append('AAAA'*n_A + 'BB'*n_B)


result = '.'.join(result)


if not success:
    print(-1)
else:
    print(result)


