for test_case in range(1, 11):
    N = int (input())
    a = list(map(int, input().split()))
    cnt_rv = 0
    for i in range(2,N-2):
        tmp_l1 = a[i-2]
        tmp_l2 = a[i-1]
        tmp_r1 = a[i+1]
        tmp_r2 = a[i+2]

        if a[i] >tmp_l1 and a[i] > tmp_l2 and a[i]>tmp_r1 and a[i]>tmp_r2:
            cnt_rv += min(a[i]-tmp_l1,a[i]-tmp_l2,a[i]-tmp_r1,a[i]-tmp_r2)


    print(f'#{test_case}',cnt_rv)
