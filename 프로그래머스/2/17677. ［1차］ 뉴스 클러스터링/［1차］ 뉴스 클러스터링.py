def solution(str1, str2):
    answer = 0
    A = []
    B = []
    d = dict()
    dupli = set()  # 양쪽 문자열에 존재하는 문자열 저장
    union = 0  # 합집합 개수
    intersection = 0  # 교집합 개수

    # 1. 입력받은 문자열을 통해 다중집합을 만든다.
    for i in range(len(str1) - 1):
        tmp = str1[i:i + 2]  # 두 글짜씩 뽑는다
        if tmp.isalpha():  # 뽑은 글자가 모두 알파벳으로 이루어졌는지 확인
            tmp=tmp.lower()  # 소문자로 모두 변환
            A.append(tmp)  # A 집합에 추가
            if tmp in d:  # str1의 경우 모든 값을 다 딕셔너리에 넣음
                d[tmp][0] += 1
            else:
                d[tmp] = [1, 0]

    for i in range(len(str2) - 1):
        tmp = str2[i:i + 2]
        if tmp.isalpha():
            tmp=tmp.lower()
            B.append(tmp)
            if tmp in d:  # map에 이미 있는 값일 경우
                d[tmp][1] += 1  # 추가한다
                dupli.add(tmp)

   
    # 예외 처리
    if len(A)==0 and len(B)==0:
        return 65536

    # dupli 에 있는 key 값의 value ([]형태) 를 꺼내 배열의 최솟 값을 중복 값으로 지정
    for s in dupli:
        intersection += min(d[s])

    union = len(A) + len(B) - intersection

    answer = int((intersection / union) * 65536)

    return answer
