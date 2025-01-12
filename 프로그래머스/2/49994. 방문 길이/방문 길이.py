def solution(dirs):
    answer = 0
    ways = {
        "U": [0, 1],
        "D": [0, -1],
        "R": [1, 0],
        "L": [-1, 0]
    }
    x,y,paths = 0,0 , set()
    for i in dirs:
        dx = x + ways[i][0]
        dy = y + ways[i][1]
        if ((-5<=dx<=5) and (-5<=dy<=5)):
            paths.add((x,y,dx,dy)) # 양쪽 방향 다 넣기
            paths.add((dx,dy,x,y))
            x,y = dx,dy

    answer = len(paths)//2
    return answer