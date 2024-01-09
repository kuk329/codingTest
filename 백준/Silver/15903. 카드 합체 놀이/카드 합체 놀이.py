n,m = map(int,input().split())
card = list(map(int,input().split())) 

def play():
    # 카드에서 가장 작은 값 두개를 찾아서 합친뒤 그 값을 다시 넣어준다.
    card.sort() # 오름차순 정렬
    add=card[0]+card[1]
    card[0]=add
    card[1]=add

for _ in range(m):
    play()

print(sum(card))
    

