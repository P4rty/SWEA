# import sys
# sys.stdin = open("sample_input.txt", "r")
from collections import deque


def bfs(graph, start, goal, V):
    distance = [-1] * (V+1)
    queue = deque([start])
    distance[start] = 0
    # 현재 노드를 방문처리
    cnt = 0
    # 큐가 빌 때 까지 반복
    while queue:
        # 큐에서 하나의 원소를 꺼내 출력
        v = queue.popleft()

        if v == goal:
            return distance[v]

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에  삽입
        for nxt in graph[v]:
            if distance[nxt] == -1:
                distance[nxt] = distance[v] + 1
                queue.append(nxt)
    return 0



T = int(input())

for test_case in range(1, T + 1):
    # V : vertex, E : edge
    V, E = map(int, input().split())

    graph = [[] * (V+1) for _ in range(V+1)]
    for i in range(E):
        # E개의 간선 양쪽 노드 번호
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # S : start, G: goal
    S, G = map(int, input().split())

    visited = [0] * (V + 1)
    result = bfs(graph, S, G, V)
    print(f'#{test_case} {result}')