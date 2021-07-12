# 재귀를 사용한 문제인데, 파이썬의 한계상 재귀가 일정 이상 깊게 들어가면 recursionerror가 발생하게 된다.
# 해결법으로 sys.setrecursionlimit(100000)를 사용해 해결하였다.
# 또한 시간초과가 계속 발생하여 parent를 원래는 list형식이였는데 dictionary형식으로 바꾸어 해결하였다. -> 이걸로 해결했는지는 잘 모르겠다.

import sys
sys.setrecursionlimit(100000)

def find(a, parent):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a], parent)
    return find(parent[a], parent)

def union(a, b, parent):
    aroot = find(a, parent)
    broot = find(b, parent)

    if aroot <= broot:
        parent[broot] = aroot
    else :
        parent[aroot] = broot

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())

    parent = dict()

    for i in range(M):
        a = list(map(int, sys.stdin.readline().split()))

        if a[1] not in parent:
            parent[a[1]] = a[1]
        if a[2] not in parent:
            parent[a[2]] = a[2]

        if a[0] == 0:
            union(a[1], a[2], parent)
        elif a[0] == 1:
            if find(a[1], parent) == find(a[2], parent):
                print('YES')
            else :
                print('NO')
