def solution(numbers):
    n = len(numbers)
    answer = [-1]*n
    stack = []
    
    for i in range(n):
        target = numbers[i] # 현재 확인할 값
        
        # 스택에 값이 있고 그 값이 확인한 값보다 작은 경우(뒷큰수 찾음)
        while stack and numbers[stack[-1]]<target:
            answer[stack[-1]]=target
            stack.pop()
        
        stack.append(i)
    
    return answer