# import sys
# sys.stdin = open("sample_input.txt","r")
T = int(input())     # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다

for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst_asc = sorted(lst)
    lst_dec = sorted(lst, reverse=True)
    result = []
    for i in range(len(lst)):
        if i % 2 == 0:
            result.append(lst_dec[i//2])
        else:
            result.append(lst_asc[i//2])

    print(f'#{test_case}', end=' ')
    for i in range(10):
        print(result[i], end=' ')
    print()
