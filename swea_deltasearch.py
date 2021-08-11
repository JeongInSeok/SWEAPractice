
T = 10
for test_case in range(1, T+1):
    N = int(input())
    lis = [list(map(int,input().split())) for _ in range(N)]

    dx = [0,1,0,-1]
    dy = [-1,0,1,0]

    ans = 0
    for x in range(N):
        for y in range(N):
            for z in range(4):
                newx = x+dx[z]
                newy = y+dy[z]
                if newx < 0 or newy < 0 or newx >= N or newy >= N:
                    continue
                ans = ans + abs(lis[x][y]-lis[newx][newy])
    print('#{} {}'.format(test_case, ans))


