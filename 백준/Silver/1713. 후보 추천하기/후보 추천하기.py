import sys
input = sys.stdin.readline
N = int(input()) # 사진틀의 개수
n = int(input()) # 전체 학생의 총 추천 횟수
arr = list(map(int,input().split())) # 추천받은 학생들의 번호 (n 개)
d = dict() # 딕셔너리에는 현재 사진틀에 지금 추천을 받은 학생이 있는지와 몇번 추천받았는지를 저장

picture = []
delete_student_idx = 0 # 삭제 대상학생의 사진틀 인덱스 번호
delete_student = 0
min_nominate = 1000 # 최소로 추천받은 횟수

for i in range(n):
    min_nominate = 1000  # 최소로 추천받은 횟수
    if len(picture)<N: # 사진틀에 자리가 남아있는 경우
        if arr[i] in d: # 이미 사진틀에 게시된 경우
            d[arr[i]]+=1 # 해당 학생의 추천 횟수 증가
        else: # 아직 게시되지 않은 경우
            d[arr[i]] = 1 # 횟수와 번호 넣어주고
            picture.append(arr[i]) # 사진틀에도 넣어주기

    else: # 사진틀에 자리가 꽉 찬 경우
        # 현재 호명된 학생이 이미 사진틀에 있는 경우
        if arr[i] in d:
            d[arr[i]]+=1
        else:
            for j in range(N): # 사진틀을 돌면서 삭제할 대상 찾기
                tmp = d[picture[j]]
                if tmp<min_nominate: # 더 작지 않은 이상 바뀌지 않기 때문에 맨 앞에서 부터 확인할 경우 먼저 들어온 사람이 선택될 수 밖에 없다.
                    delete_student_idx = j
                    min_nominate = tmp

            # 삭제할 학생을 실제로 제거
            # 1. 사진 틀에서 제거
            delete_student = picture[delete_student_idx]
            picture.remove(delete_student)
            # 2. 딕셔너리 정보 제거
            del d[delete_student]

            # 남은 자리에 새로 추천받은 학생 넣기
            picture.append(arr[i])
            d[arr[i]] = 1

picture.sort() # 오름차순 정렬
for p in picture:
    print(p,end=' ')

