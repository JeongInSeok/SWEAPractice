T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    # M 은 M x M 파리채로 때려 죽일 영역
    # N 은 NxN 배열   

    Map = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            current = 0
            for k in range(M):
                for l in range(M):
                    current += Map[j+l][i+k]
            if current > ans:
                ans = current
    
    print('#{} {}'.format(test_case, ans))