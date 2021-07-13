# dp 공부좀 해야할거같다.
# 이 문제의 경우는 모든 경우를 구하는 식으로 사용
# 시간 초과 방지로 그 전 과정에서 계산한 수들은 모드 제거 (8번 줄)

def dp(solve):
    global count
    count += 1
    Nsolve = []
    for a in solve:
        Nsolve.append(a-1)
        if a%3== 0 and a >= 3:
            Nsolve.append(a/3)
        if a%2== 0 and a >=2:
            Nsolve.append(a/2)
    
    return Nsolve

if __name__ == '__main__':
    N = int(input())
    solve = [N]
    count = 0
    if N == 1:
        print(count)
    else:
        while min(solve) != 1:
            solve = dp(solve)

        print(count)