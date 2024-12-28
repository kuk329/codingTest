def solution(number, k):
    # 1. 필요한 변수와 값 초기화
    answer = ''
    stack = [number[0]]
    n = len(number)


    # 스택을 사용해서 k 개의 숫자를 제거한다.
    for i in range(1,n):
        while stack: # 스택에 값이 있는 동안 반복
            if k==0:
                break
            if int(stack[-1]) < int(number[i]): # 현재 확인 중인 값보다 스택에 들은 값이 더 작으면 삭제
                stack.pop()
                k-=1
            else:
                break
        stack.append(number[i])

    if k>0:
        while k>0:
            stack.pop()
            k-=1

    answer = answer.join(stack)
    return answer