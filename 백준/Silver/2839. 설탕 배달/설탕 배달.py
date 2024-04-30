sugar = int(input()) # 배달할 설탕 무게

cnt=0

while sugar>=0:
    if sugar%5==0:
        cnt+=sugar//5
        break
    sugar-=3
    cnt+=1


if sugar<0:
    print(-1)
else:
    print(cnt)