T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    for x in range(N):
        for y in range(N):
            if arr[x][y] == 'A':
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N:
                        arr[nx][ny] = 'X'
            elif arr[x][y] == 'B':
                for i in range(4):
                    for j in range(1, 3):
                        nx = x + dx[i] * j
                        ny = y + dy[i] * j
                        if 0 <= nx < N and 0 <= ny < N:
                            arr[nx][ny] = 'X'
            elif arr[x][y] == 'C':
                for i in range(4):
                    for j in range(1, 4):
                        nx = x + dx[i] * j
                        ny = y + dy[i] * j
                        if 0 <= nx < N and 0 <= ny < N:
                            arr[nx][ny] = 'X'
    cnt = 0
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 'H':
                cnt += 1
    #print('#{} {}'.format(test_case,cnt))
    print(f'#{test_case} {cnt}')
