k,n = map(int,input().split())
a = []

for _ in range(k):
    a.append(int(input()))
    
a.sort() # 457 539 743 802

max_length = 0 # 만들수 있는 최대 길이
def search(s,e):
    global max_length
    while s<=e:
        cnt=0
        mid = (s+e)//2
        for i in range(k): # 해당 길이로 총 랜선을 몇개 만들수 있는지 
            cnt+=a[i]//mid
        if cnt<n:
            e=mid-1
        else:
            if max_length<mid:
                max_length = mid
            s=mid+1

search(1,a[-1])

print(max_length)
    