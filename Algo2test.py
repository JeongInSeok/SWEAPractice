
# 토지 개발 30점
# 토지 평탄화 2차원 배열의 값은 토지의 높이
# 총합을 - 개수로 나눈 값이 평탄화 높이
# 평탄화 비용 = 평탄화 높이 값과 기존 값의 절대값 차이의 총합

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    # M값은 좌상단 좌표와 우하단 좌표값으로 평탄화 시킬 영역을 표현
    M = input().split()
    teritori_garo=int(M[3])-int(M[1])+1
    teritori_sero=int(M[2])-int(M[0])+1
    Map = [list(map(int,input().split())) for _ in range(N)]

    teritori_num = teritori_garo*teritori_sero
    current = 0
    height = 0
    for y in range(int(M[0]),int(M[2])+1):
        for x in range(int(M[1]),int(M[3])+1):
            current += Map[y][x]
    height = current//teritori_num
    nedan = 0
    # nedan 은 평탄화 비용입니다. 영어가 안떠올라서 일본어인 네단을 변수명으로 정했습니다.
    for y in range(int(M[0]),int(M[2])+1):
        for x in range(int(M[1]),int(M[3])+1):
            nedan += abs(height - Map[y][x])

    print('#{} {} {}'.format(test_case, height, nedan))

