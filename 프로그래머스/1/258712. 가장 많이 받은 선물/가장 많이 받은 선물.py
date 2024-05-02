def solution(friends, gifts):
    answer = 0 # 가장 많이 받는 친구의 이번달 받을 선물 개수
    d = dict()
    n = len(friends)
    for i in range(n):
        d[friends[i]] = i

    info = [[0] * n for _ in range(n)]

    for gift in gifts:
        A, B = gift.split()
        A_index = d[A]
        B_index = d[B]
        info[A_index][B_index] += 1

    for i in range(n): # 첫번째 친구부터 내가 받을 선물 개수 구하기
        gift_number = 0 # i 친구의 이번달까지 받은 선물 개수
        for j in range(n):
            if i==j:
                continue
            give = info[i][j] # 내가 준 선물 개수
            take = info[j][i] # 내가 받은 선물 개수
            if give==take:
                # 각각의 선물 지수 구해서 비교
                give_num_i = 0 # 내가 준 총 선물 개수
                take_num_i = 0 # 내가 받은 총 선물 개수
                for k in range(n):
                    if i!=k:
                        give_num_i+=info[i][k]
                for k in range(n):
                    if i!=k:
                        take_num_i += info[k][i]
                total_num_i = give_num_i - take_num_i

                give_num_j = 0  # 내가 준 총 선물 개수
                take_num_j = 0  # 내가 받은 총 선물 개수
                for k in range(n):
                    if j != k:
                        give_num_j += info[j][k]
                for k in range(n):
                    if j != k:
                        take_num_j += info[k][j]
                total_num_j = give_num_j - take_num_j

                if total_num_i > total_num_j:
                    gift_number+=1

            elif give > take:
                gift_number+=1
            else:
                pass

        if answer < gift_number: # 최댓값 갱신
            answer = gift_number



    return answer