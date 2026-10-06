# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    result = 0


    def fdboss(member):
        if arr[member] == member:
            return member
        ret = fdboss(arr[member])
        arr[member] = ret

        return ret


    def union(a, b):
        fa = fdboss(a)
        fb = fdboss(b)
        if fa == fb:
            return
        arr[fb] = fa

    arr = [i for i in range(N + 1)]

    for i in range(0, 2 * M, 2):
        union(lst[i], lst[i+1])
    for i in range(1, N + 1):
        arr[i] = fdboss(arr[i])
    result = len(set(arr[1:]))
    print(f'#{test_case} {result}')