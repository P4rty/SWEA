# import sys
# sys.stdin = open("input.txt", "r")
from collections import deque

T = 10


for test_case in range(1, T + 1):
    # 입력
    N, start = map(int, input().split())
    data = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for i in range(0,N,2):
        a, b = data[i], data[i+1]
        graph[a].append(b)
    visited = [0] * 101
    q = deque([start])
    visited[start] = 1 # 시작 점 깊이 1

    max_depth = 1
    max_node =start

    while q:
        curr = q.popleft()
        curr_depth = visited[curr]

        for nxt in graph[curr]:
            if visited[nxt] == 0:
                visited[nxt] = curr_depth + 1
                q.append(nxt)

                if visited[nxt] > max_depth:
                    max_depth = visited[nxt]
                    max_node = nxt
                elif visited[nxt] == max_depth:
                    if nxt > max_node:
                        max_node = nxt

    print(f'#{test_case} {max_node}')

