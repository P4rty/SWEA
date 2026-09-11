# import sys
# sys.stdin = open("sample_input.txt","r")
T = int(input())     # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다


def binary_search(n, key):  # key를 찾게함.
    start = 1
    end = n
    cnt = 0
    while start <= end:
        middle = int((start+end)/2)

        if middle == key:
            return cnt
        elif middle > key:
            end = middle
        else:
            start = middle
        cnt += 1
    return cnt


for test_case in range(1, T + 1):
    N, pa, pb = map(int, input().split())
    pa_cnt = binary_search(N, pa)
    pb_cnt = binary_search(N, pb)
    if pa_cnt < pb_cnt:
        result = "A"
    elif pa_cnt == pb_cnt:
        result = 0
    else:
        result = "B"
    print(f'#{test_case} {result}')