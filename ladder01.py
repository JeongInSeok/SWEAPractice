T = 10
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 도착지점에 해당하는 인덱스를 찾고 저장
    for n in range(100):
        if arr[99][n] == 2:
            x = n
            break
    # 사다리를 도착지점부터 출발
    y = 99
    while 1:
        # 오른쪽으로 갈 수 있는 경우
        if x < 99 and arr[y][x+1]:
            while x < 99 and arr[y][x+1]:
                x += 1
            else:
                y -= 1
        # 왼쪽으로 갈 수 있는 경우
        elif x > 0 and arr[y][x-1]:
            while x > 0 and arr[y][x-1]:
                x -= 1
            else:
                y -= 1
        else:
            y -= 1
        # 출발지점 도착하면 종료
        if y == 0:
            break
    print('#{} {}'.format(t, x))