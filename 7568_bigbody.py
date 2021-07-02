N = int(input())

info = []
rank = []

for i in range(N):
    rank.append(int(0))

for i in range(N):
    a, b = map(int, input().split())
    info.append([a, b])

for i in range(N-1):
    for j in range(i+1, N):
        if x[i] > x[j]:
            if y[i] > y[j]:
                rank[i] += 1
                rank[j] += rank[i]+1
            else:
                if rank[i] == 0:
                    rank[i] += 1
                    rank[j] += 1
                else:
                    rank[i] 