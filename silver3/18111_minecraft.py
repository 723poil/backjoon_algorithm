N,M,B = map(int, input().split())

ground = []

max_b = -1
min_b = 257

for i in range(N):
    ground.append(list(map(int, input().split())))
    max_b = max(max_b, max(ground[-1]))
    min_b = min(min_b, min(ground[-1]))

time = 99999999
block = 0

if B == 0:
    time = 0
    for i in range(N):
        for j in range(M):
            time += 2 * (ground[i][j] - min_b)
            ground[i][j] -= ground[i][j] - min_b
else:
    for i in range(min_b, max_b+1):
        t = 0
        b = B
        for j in range(N):
            for k in range(M):
                height = ground[j][k] - i
                if height > 0:
                    t += 2 * height
                    b += height
                elif height < 0:
                    t -= height
                    b += height

        if b >= 0 and t <= time:
            time = t
            block = i

if B == 0:
    print(time, ground[0][0])
else:
    print(time, block)