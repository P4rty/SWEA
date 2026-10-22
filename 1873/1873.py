# import sys
# sys.stdin = open("input.txt", "r")

# 방향 정의: 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 방향 문자와 인덱스 매핑
dir_map = {'^': 0, 'v': 1, '<': 2, '>': 3}
dir_chars = ['^', 'v', '<', '>']

T = int(input())

for test_case in range(1, T + 1):
    H, W = map(int, input().split())
    # 높이(행)가 H인 배열 받기
    board = [list(input().strip()) for _ in range(H)]

    N = int(input())
    commands = input().strip()

    # 전차의 초기 위치와 방향 찾기
    r, c, d = 0, 0, 0
    for i in range(H):
        for j in range(W):
            if board[i][j] in dir_map:
                r, c = i, j
                d = dir_map[board[i][j]]
                break
            # 명령어 처리
    for cmd in commands:
        if cmd == 'U':
            d = 0
            board[r][c] = dir_chars[d]
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < H and 0 <= nc < W and board[nr][nc] == '.':
                board[r][c] = '.'
                r, c = nr, nc
                board[r][c] = dir_chars[d]
        elif cmd == 'D':
            d = 1
            board[r][c] = dir_chars[d]
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < H and 0 <= nc < W and board[nr][nc] == '.':
                board[r][c] = '.'
                r, c = nr, nc
                board[r][c] = dir_chars[d]
        elif cmd == 'L':
            d = 2
            board[r][c] = dir_chars[d]
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < H and 0 <= nc < W and board[nr][nc] == '.':
                board[r][c] = '.'
                r, c = nr, nc
                board[r][c] = dir_chars[d]
        elif cmd == 'R':
            d = 3
            board[r][c] = dir_chars[d]
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < H and 0 <= nc < W and board[nr][nc] == '.':
                board[r][c] = '.'
                r, c = nr, nc
                board[r][c] = dir_chars[d]
        elif cmd == 'S':
            # 포탄 발사
            curr_r, curr_c = r, c
            while True:
                curr_r += dr[d]
                curr_c += dc[d]

                # 맵 밖을 나가면 소멸
                if not (0 <= curr_r < H and 0 <= curr_c < W):
                    break

                # 강철 벽(#)을 만나면 포탄 소멸
                if board[curr_r][curr_c] == '#':
                    break

                # 벽돌 벽(*)을 만나면 평지(.)로 바꾸고 포탄 소멸
                if board[curr_r][curr_c] == '*':
                    board[curr_r][curr_c] = '.'
                    break

    print(f'#{test_case}', end=" ")
    for row in board:
        print("".join(row))

