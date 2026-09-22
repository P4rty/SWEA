# import sys
# sys.stdin = open('carrot_sample_in.txt')

T = int(input())

for test_case in range(1, T + 1):
    car_num = int(input())
    carrots = list(map(int, input().split()))

    # 전체 연속하는거 cnt_all = 0
    # 연속하는 숫자 개수세는 cnt = 0
    cnt_all = 1
    cnt = 1

    for i in range(car_num - 1):
        # i번째랑 i+1번째가 1개차이날경우 cnt +=1
        if carrots[i + 1] > carrots[i]:
            cnt += 1
            # cnt_all에 cnt를 넣는다. 이때 cnt_all보다 cnt가 커야댐
            if cnt_all < cnt:
                cnt_all = cnt
        # 아닐경우 cnt 1로 초기화
        else:
            cnt = 1

    print(f'#{test_case} {cnt_all}')