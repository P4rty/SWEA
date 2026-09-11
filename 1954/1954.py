# import sys
# sys.stdin = open("sample_input.txt","r")
T = int(input())     # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다

for test_case in range(1, T + 1):
    N = int(input())
    lst = [[0]*N for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cur_pos_x = 0
    cur_pos_y = 0
    cur_direction = 0
    for i in range(1, N*N+1):
        lst[cur_pos_x][cur_pos_y] = i
        next_pos_x = cur_pos_x + dx[cur_direction]
        next_pos_y = cur_pos_y + dy[cur_direction]
        if next_pos_x < 0 or next_pos_y < 0 or next_pos_x >= N or next_pos_y >= N or lst[next_pos_x][next_pos_y] != 0:
            cur_direction = (cur_direction + 1) % 4
            next_pos_x = cur_pos_x + dx[cur_direction]
            next_pos_y = cur_pos_y + dy[cur_direction]
        cur_pos_x = next_pos_x
        cur_pos_y = next_pos_y

    print(f'#{test_case}')
    for i in range(N):
        for j in range(N):
            print(lst[i][j], end=' ')
        print()