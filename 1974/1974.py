import sys
sys.stdin = open("input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    result_rc = 1
    result_box = 1
    correct = 45
    # 가로 세로 합 무조건 45
    # 행의 합 리스트, 열의 합 리스트

    for i in range(9):
        cnt_r = 0
        cnt_c = 0
        for j in range(9):
            cnt_r += sudoku[i][j]
            cnt_c += sudoku[j][i]
        if cnt_r != correct or cnt_c != correct:
            result_rc = 0
            break

    box = [set(), set(), set(), set(), set(), set(), set(), set(),set()]
    lst_correct = list(range(1, 10))
    for i in range(3):
        for j in range(3):
            box[0].add(sudoku[i][j])
            box[1].add(sudoku[i+3][j])
            box[2].add(sudoku[i+6][j])
            box[3].add(sudoku[i][j+3])
            box[4].add(sudoku[i+3][j+3])
            box[5].add(sudoku[i+3][j+6])
            box[6].add(sudoku[i][j+6])
            box[7].add(sudoku[i+6][j+3])
            box[8].add(sudoku[i+6][j+6])

    for i in range(9):
        if len(box[i]) != 9:
            result_box = 0
            break
    result = result_rc & result_box
    print(f'#{test_case} {result}')
