# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    check = [[1 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(N+1):
        for j in range(i):
            check[i][j] = check[i - 1][j - 1] + check[i - 1][j]
            if j == i-1 or j == 0:
                check[i][j] = 1

    print(f'#{test_case}',end =" ")
    for i in range(N+1):
        for j in range(i):
            print(check[i][j], end=" ")
        print()



