def add(arr):
    if (arr[2]-arr[1])== (arr[1]-arr[0]):
        return True
    return False
 
def multi(arr):
    if (arr[2]//arr[1]) == (arr[1]//arr[0]):
        return True
    return False

def solution(common):
    answer = 0
    if add(common):
        diff = common[2]-common[1]
        answer = common[-1]+diff
    
    else :
        ratio = common[2]//common[1]
        answer = common[-1]*ratio
        
        
        
    return answer


    