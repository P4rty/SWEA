# import sys
# sys.stdin = open("input.txt", "r")

def shoot(ball, count, org):  # ball 구슬 순서, count 남은 벽돌, org 현재리스트
    global min_v

    if ball == N or count == 0:  # 구슬을 모두 발사했거나 남은 벽돌이 없는 경우
        min_v = min(min_v, count)
        return
    for j in range(W): # 다른 열 쏴보기
        dest = [row[:] for row in org]  # 벽돌을 깬 결과 저장용
        tmp = []
        n_count = count
        for i in range(H):
            if dest[i][j]:
                tmp.append([i, j, dest[i][j]])
                dest[i][j] = 0
                n_count -= 1
                break
        if not tmp:
            shoot(ball + 1, count, dest)
            continue

        while tmp:
            i, j, p = tmp.pop()
            for k in range(1, p):
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    ni, nj = i + di * k, j + dj * k
                    if 0 <= ni < H and 0 <= nj < W and dest[ni][nj]:
                        if dest[ni][nj] > 1:
                            tmp.append([ni, nj, dest[ni][nj]])
                        dest[ni][nj] = 0
                        n_count -= 1
        for c in range(W):
            idx = H - 1
            for r in range(H - 1, -1, -1):
                if dest[r][c]:
                    dest[idx][c] = dest[r][c]
                    if idx != r:
                        dest[r][c] = 0
                    idx -= 1
        shoot(ball + 1, n_count, dest)


T = int(input())
for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())
    board_brick = [list(map(int, input().split())) for _ in range(H)]
    min_v = 12*15
    block_num =0
    for row in board_brick:
        for b in row:
            if b:
                block_num += 1
    min_v = block_num
    shoot(0, block_num, board_brick)
    print(f'#{test_case} {min_v}')