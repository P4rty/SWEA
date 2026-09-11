# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    lst_command = [list(map(int, input().split())) for _ in range(E)]

    graph = [[0 for i in range(V + 1)] for i in range(V + 1)]
    for i, j in lst_command:
        graph[i][j] = 1

    S, G = list(map(int, input().split()))

    stack = [S]
    visited = [False] * (V + 1)
    visited[S] = True
    result = 0

    while stack:
        curr = stack.pop()

        if curr == G:
            result = 1
            break
        for daum in range(1, V + 1):
            if graph[curr][daum] == 1 and not visited[daum]:
                visited[daum] = True
                stack.append(daum)

    print(f'#{test_case} {result}')
