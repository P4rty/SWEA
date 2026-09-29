# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())


def permute(arr, r):
    result = []
    visited = [False] * len(arr)
    path = []

    def backtrack():
        if len(path) == r:
            result.append(path[:])      # 복사해서 저장
            return
        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True
                path.append(arr[i])
                backtrack()
                path.pop()              # 되돌리기
                visited[i] = False

    backtrack()
    return result


for test_case in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    nodes = list(range(1, N))
    min_sum = float('inf')
    permute_lst = permute(nodes, N-1)
    for arr in permute_lst:
        curr = 0
        tmp = 0
        for nxt in arr:
            tmp += grid[curr][nxt]
            curr = nxt
        tmp += grid[curr][0]
        min_sum = min(min_sum, tmp)

    print(f'#{test_case} {min_sum}')
