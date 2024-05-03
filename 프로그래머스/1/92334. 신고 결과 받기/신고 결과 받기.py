def solution(id_list, report, k):
    n = len(id_list)  # 총 유저 수
    answer = [0]*n
    d1 = dict()
    d2 = dict()

    for i in range(n):
        d1[id_list[i]]=set() # ex) {'muzi': ['apeach'], 'frodo': ['muzi', 'apeach'], 'apeach': [], 'neo': ['frodo', 'muzi']}
        d2[i]=id_list[i] # ex) { 0 : muzi , 1 : frodo , .. }


    for r in report:
        f,t = r.split()
        d1[t].add(f) # 신고를 당한 유저의 딕셔너리에 리스트로 신고를 한 사람 이름 추가

    # 딕셔너리 전체를 돌면서 나를 신고한 횟수가 k 가 넘을 때는 나를 신고한 사람의 메일 횟수 하나 증가
    for i in range(n):
        report_count = len(d1[d2[i]]) # 신고 회수
        if report_count>=k: # 신고 횟수가 정지먹는 횟수가 되면
            # 해당 유저를 신고한 유저의 메일 횟수 한개 증가
            for id in d1[d2[i]]:
                answer[id_list.index(id)]+=1

    return answer
