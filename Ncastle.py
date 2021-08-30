# swea 12649 'N Castle'(전용)
 
def set_castle(N, col_visit, cnt):
    if cnt == N:
        global result
        result += 1
        print('카운트'.format(cnt)) 
        print(col_visit)
        return
 
    for j in range(N):
        if col_visit[j]:
            continue
 
        col_visit[j] = True
        print('j{} , col_visit{}'.format(j,col_visit[j]))
        set_castle(N, col_visit, cnt + 1)
     

        col_visit[j] = False
 
    return
 
 
if __name__ == '__main__':
    T = 10
 
    for t in range(1, T + 1):
        N = int(input())
 
        col_visit = [False for _ in range(N)]
        print(col_visit)
        result = 0
 
        set_castle(N, col_visit, 0)
 
        print('#{} {}'.format(t, result))
