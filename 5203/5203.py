# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())


def is_triplet(cards):
    cnt = [0] * 10
    for card in cards:
        cnt[card] += 1
        if cnt[card] == 3:
            return True
    return False


def is_run(cards):
    cnt = [0] * 10
    for card in cards:
        cnt[card] += 1
    for i in range(8):
        if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i+2] >= 1:
            return True
    return False


for test_case in range(1, T + 1):
    result = 0
    cards = list(map(int, input().split()))
    # 12개를 받음.
    a_card = list(cards[0:12:2])
    b_card = list(cards[1:12:2])
    for i in range(2, 7):
        if is_triplet(a_card[0:i]):
            result = 1
            break
        if is_run(a_card[0:i]):
            result = 1
            break
        if is_triplet(b_card[0:i]):
            result = 2
            break
        if is_run(b_card[0:i]):
            result = 2
            break

    print(f'#{test_case} {result}')
