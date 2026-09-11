# import sys
# sys.stdin = open("input.txt","r")
T = 10     # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다

for test_case in range(1, T + 1):
    trash = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]
    # 위 , 오, 왼
    dr = [0, 1, 0]
    dc = [-1, 0, -1]
    N = 100
    cur_pos_r = N - 1
    for i in range(N):
        if lst[cur_pos_r][i] == 2:
            cur_pos_c = i

    while cur_pos_r > 0:
        if 0 <= (cur_pos_c-1) < N and lst[cur_pos_r][cur_pos_c - 1] == 1:
            lst[cur_pos_r][cur_pos_c] = 0
            cur_pos_c -= 1
        elif 0 <= (cur_pos_c+1) < N and lst[cur_pos_r][cur_pos_c + 1] == 1:
            lst[cur_pos_r][cur_pos_c] = 0
            cur_pos_c += 1
        else:
            cur_pos_r -= 1

    print(f'#{test_case} {cur_pos_c}')

