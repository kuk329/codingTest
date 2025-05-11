def solution(skill, skill_trees):
    idx = 0
    cnt = 0
    chk = True
    for data in skill_trees:
        for s in data:
            if s in skill:
                if s == skill[idx]:
                    idx+=1
                else:
                    chk = False
                    break
        if chk:
            cnt+=1
        idx=0
        chk = True
    return cnt