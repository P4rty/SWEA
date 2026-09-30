# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())


for test_case in range(1, T + 1):

    # 최대한 많은 화물차 실을 수 있도록 하기.
    # docker 는 [[s1,e1],[s2,e2],...]형태
    N = int(input())
    docker = [list(map(int, input().split())) for _ in range(N)]
    # 종료 시간이 빠른 것 부터 넣기
    docker.sort(key=lambda x: x[1])
    result = 0
    last_end_time = 0

    for s, e in docker:
        if s >= last_end_time:
            result += 1
            last_end_time = e

    print(f'#{test_case} {result}')
