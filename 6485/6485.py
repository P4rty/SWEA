# import sys
# sys.stdin = open("s_input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst_bus_route = [list((input().split())) for _ in range(N)]
    lst_bus_stop = [0]*5001
    for i in range(N):
        start = int(lst_bus_route[i][0])
        end = int(lst_bus_route[i][1])
        for j in range(start, end+1):
            lst_bus_stop[j] += 1
    P = int(input())
    lst_c = [int(input()) for _ in range(1, P+1)] # 질문 리스트

    print(f'#{test_case}', end=" ")
    for i in range(P):
        print(lst_bus_stop[lst_c[i]], end=" ")
    print()
