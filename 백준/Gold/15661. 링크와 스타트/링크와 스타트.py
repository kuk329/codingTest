n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]


def bf(index,link,start):
    if index == n:
        if len(link)==0 or len(start)==0:
            return -1
        link_sum = 0
        start_sum = 0
        for i in range(len(link)):
            for j in range(len(link)):
                if i==j:
                    continue
                link_sum+=arr[link[i]][link[j]]

        for i in range(len(start)):
            for j in range(len(start)):
                if i==j:
                    continue
                start_sum +=arr[start[i]][start[j]]

        diff = abs(link_sum-start_sum)
        return diff
    
    if len(link)==n or len(start)==n:
        return -1

    ans = -1
    r1 = bf(index+1,link+[index],start)
    r2 = bf(index+1,link,start+[index])

    if (ans==-1) or (r1!=-1 and ans>r1):
        ans=r1

    if (ans==-1) or (r2!=-1 and ans>r2):
        ans=r2

    return ans

print(bf(0,[],[]))