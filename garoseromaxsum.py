T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
 
    def is_garosero(r, c):
        total = 0
        for k in range(N):
            total += arr[r][k] + arr[k][c]
        total -= arr[r][c]
        return total
 
    max_val = 0
    for r in range(N):
        for c in range(N):
            ret = is_garosero(r, c)
            if ret > max_val:
                max_val = ret
    print(f'#{tc} {max_val}')