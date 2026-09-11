T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N =  int(input().split())
    card_list = list(map(int, input().split("")))
    fq_card_num = 0
    fq_card_cnt = 0
    for card in card_list:



    print(f'#{test_case} {fq_card_num} {fq_card_cnt}')
