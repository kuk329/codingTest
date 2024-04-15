def solution(array, height):
    answer = 0
    array.sort(reverse=True)
    for h in array:
        if h > height:
            answer+=1
        else:
            break
    return answer