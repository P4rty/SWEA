# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())


def dfs(curr, depth):
    global max_depth
    if depth > max_depth:
        max_depth = depth
    for nxt in graph[curr]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt, depth + 1)
            visited[nxt] = False


for test_case in range(1, T + 1):
    # 입력
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    max_depth = 1

    visited = [False] * (N + 1)
    for start in range(1, N + 1):
        visited[start] = True
        dfs(start, 1)
        visited[start] = False

    print(f'#{test_case} {max_depth}')

