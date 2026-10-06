# import sys
# sys.stdin = open("test_in.txt", "r")

T = int(input())


for test_case in range(1, T + 1):
    N, E = map(int, input().split())  # 정점 개수, 간선 수
    eg_lst = list(map(int, input().split()))  # 간선의 양 끝점
    adj_lst = [[] for _ in range(E + 1)]  # 인접 리스트
    for i in range(0, len(eg_lst), 2):  # 간선의 양 끝점을 인접리스트에 넣기
        adj_lst[eg_lst[i]].append(eg_lst[i+1])
    S, G = map(int, input().split())  # 출발점, 도착점

    cnt = 0  # 횟수 세기
    used = [0] * (N + 1)  # 방문 리스트

    def dfs(now):
        global cnt

        if now == G:
            cnt += 1

        for i in adj_lst[now]:
            if used[i] == 0:
                used[i] = 1
                dfs(i)
                used[i] = 0

    dfs(S)
    answer = cnt
    print(f'#{test_case} {answer}')
