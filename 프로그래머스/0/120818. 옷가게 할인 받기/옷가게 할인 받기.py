def solution(price):
    answer = 0 # 지불 금액
    if 500_000 <= price:
        answer = price*0.8
    elif 300000 <= price:
        answer = price*0.9
    elif 100000 <= price:
        answer = price*0.95
    else:
        answer = price
    
    return int(answer)