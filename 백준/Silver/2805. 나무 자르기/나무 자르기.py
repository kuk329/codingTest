import sys

input = sys.stdin.readline

N, M = map(int, input().split())

tree = list(map(int, input().split()))
tree.sort()


def search(s, e):
    max_height = 0
    while s <= e:
        cut = 0
        mid = (s + e) // 2
        for i in range(N):
            if mid < tree[i]:  # 절단기 높이가 나무 높이보다 작으면
                cut += (tree[i] - mid)  # 잘라서 가져갈 수 있음.

        if cut < M:  # 나무를 자른 크기가 가져가려는 크기보다 작을때
            e = mid - 1  # 절단기 높이를 줄임
        else:  # 나무를 자른 크기가 가져가려는 크거나 같을때
            if max_height < mid:
                max_height = mid
            s = mid + 1

    return max_height


print(search(1, tree[-1]))


