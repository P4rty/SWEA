# import sys
# sys.stdin = open("input.txt", "r")

T = 10

for test_case in range(1, T + 1):
    # 테스트 케이스의 번호, 길의 총개수(엣지)
    dummy, E = map(int, input().split())
    # 노드의 개수 100개 (0 ~ 99)
    V = 100
    # 순서쌍
    lst_command = list(map(int, input().split()))
    # 그래프 쉽게 설정하기
    # graph_1 = [0 for i in range(V)]
    # graph_2 = [0 for i in range(V)]
    graph = [[0]*V for _ in range(V)]
    # 한 노드에서 경로가 2개 이상은 아니므로
    for i in range(0, len(lst_command), 2):
        u = lst_command[i]
        v = lst_command[i+1]
        graph[u][v] = 1

    S, G = 0, 99
    stack = [S]
    visited = [False] * V
    visited[S] = True
    result = 0

    while stack:
        curr = stack.pop()
        if curr == G:
            result = 1
            break
        for nxt in range(0, V):
            if graph[curr][nxt] == 1 and not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)

    print(f'#{test_case} {result}')
