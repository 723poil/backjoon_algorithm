#dp문제 규칙을 찾아서 문제를 풀어야함
import sys

N = int(sys.stdin.readline())

def case(a):
    if a == 1:
        return 1
    elif a == 2:
        return 2
    elif a == 3:
        return 4
    return case(a-1)+case(a-2)+case(a-3)

for i in range(N):
    a = int(sys.stdin.readline())

    print(case(a))