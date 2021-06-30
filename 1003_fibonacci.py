# 다이나믹 프로그래밍을 사용하여 문제를 품.
# 재귀 함수를 사용하여 풀려고 했지만, 시간복잡도가 너무 커지기 때문에 사용하지 않았음.

n = input()

zerocount = [1, 0 ,1]
onecount = [0, 1, 1]

for i in range(int(n)):
    a = int(input())

    while len(zerocount)-1 < a:
        zerocount.append(int(zerocount[len(zerocount)-1])+int(zerocount[len(zerocount)-2]))
        onecount.append(int(onecount[len(onecount)-1])+int(onecount[len(onecount)-2]))

    print(str(zerocount[int(a)])+" "+str(onecount[int(a)]))