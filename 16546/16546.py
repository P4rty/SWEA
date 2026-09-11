T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    cards = list(map(int, input().strip()))
    count_list = [0]*10
     
    for card in cards:
        count_list[card] += 1
    
    tri_cnt = 0
    run_cnt = 0
    i = 0

    while i < 10:
        if count_list[i] >= 3:
            count_list[i] -= 3
            tri_cnt += 1
            continue
        if i <= 7 and count_list[i] >= 1 and count_list[i+1] >= 1 and count_list[i+2]>= 1 :
            count_list[i] -= 1
            count_list[i+1] -= 1
            count_list[i+2] -= 1
            run_cnt += 1
            continue
        i += 1
    if run_cnt + tri_cnt == 2:
        print(f'#{test_case} true')
    else:
        print(f'#{test_case} false')

    
