import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 삼각형 리스트
    tri = []

    for i in range(N):
        # 첫째줄은 1, 한칸
        row = [1] * (i+1)

        # 둘째줄부터 왼쪽과 오른쪽위의 합으로 채우기
        for j in range(1, i):
            # 왼위 + 오위
            row[j] = tri[i-1][j-1] + tri[i-1][j]
            # tri에 담기
        tri.append(row)
        #     인덱스에러 발생 out of range....... 해결
        # 이제 삼각형으로 만들기
    # 방법 2: 일반 for 문과 end=" " 사용
    for row in tri:
        for num in row:
            print(num, end=" ")
        print()

