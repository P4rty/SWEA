# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())


# list 를 int 로 변경하기 위해서
def prize_to_int(lst):
    # 리스트의 길이
    length = len(lst)
    # 결과 값
    result = 0
    # 맨 뒤 부터 순회 하면서 result 값에 더함.
    for i in range(-1, -length-1, -1):
        result += int(lst[i])*10**(abs(i)-1)
    return result


def dfs(cnt):
    global answer
    state = "".join(cards)
    # 가지치기
    if (state, cnt) in visited:
        return
    visited.add((state, cnt))

    if cnt == trade:
        answer = max(answer, int(state))
        return

    for i in range(N):
        for j in range(i+1,N):
            # 바꾸고
            cards[i], cards[j] = cards[j], cards[i]
            dfs(cnt + 1)
            # 되돌리기
            cards[i], cards[j] = cards[j], cards[i]


for test_case in range(1, T + 1):
    card_str, trade_str = input().split()
    cards = list(card_str)
    trade = int(trade_str)
    N = len(cards)
    visited = set()
    answer = 0
    dfs(0)
    print(f'#{test_case} {answer}')
