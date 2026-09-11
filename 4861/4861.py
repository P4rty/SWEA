# import sys
# sys.stdin = open("sample_input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst_N = [list(input()) for _ in range(N)]
    result = ""
    for r in range(N):
        for c in range(N-M+1):
            compare_str = lst_N[r][c:c+M]
            if compare_str == compare_str[::-1]:
                result = "".join(compare_str)
                break
        if result:
            break
    if not result:
        for c in range(N):
            for r in range(N - M + 1):
                compare_str = "".join(lst_N[r+k][c] for k in range(M))
                if compare_str == compare_str[::-1]:
                    result = compare_str
                    break
            if result:
                break

    print(f'#{test_case} {result}')