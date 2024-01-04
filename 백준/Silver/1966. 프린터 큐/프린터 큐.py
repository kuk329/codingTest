from collections import deque

T = int(input())

for _ in range(T):
    N,M  = map(int,input().split()) # 문서의 개수, 몇번째로 인쇄되었는지 궁금한 문서의 초기 위치
    tmp = [int(i) for i in input().split()]

    q = deque()

    for i in range(N):
        q.append((i,tmp[i])) # 튜플로 원래 위치와 중요도를 같이 저장.

    # 가장 중요도가 높은 문서부터 차례로 삭제할때 M 과 일치하는 문서 번호이면 그 값을 리턴하고 종료
    count = 0
    while q:
        idx,importance = q.popleft()

        for i in range(len(q)): # 현재 문서보다 더 중요성이 큰 문서가 있는지 모든 문서를 확인
            if importance<q[i][1]: # 그런 문서가 하나라도 있으면 현재 문서를 맨 뒤에 추가
                q.append((idx,importance))
                break # 현재 for 문 종료

        else: # 현재 문서보다 더 중요한 문서가 없다면 현재 문서를 출력
            count+=1
            if idx==M:
                print(count)
                break # while 문을 종료

