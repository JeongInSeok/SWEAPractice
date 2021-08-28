# N X N 크기의 판이 있다. 판의 각 칸에는 돌이 있거나 없을 수 있다. 
# 돌이 가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지 
# 판정하는 프로그램을 작성하라.

four = 4
zero = 0
yes = 'YES'
no = 'NO'
 
 
def gomoku():
    N = int(input())
    field = []
    for i in range(N):
        field.append(input())
    return find(field, N)
 
 
def find(field, N):
    for y in range(N):
        for x in range(N):
            # o가 아닐때는 체크할 필요가 없음
            if field[y][x] != 'o':
                continue
            # 오른쪽 체크
            if x + four < N and five_check(field, 0, 1, y, x):
                return yes
            # 하단 체크
            if y + four < N and five_check(field, 1, 0, y, x):
                return yes
            # 좌측상단
            if x - four >= zero and y - four >= zero and five_check(field, -1, -1, y, x):
                return yes
            # 우측상단
            if x + four < N and y - four >= zero and five_check(field, -1, 1, y, x):
                return yes
    return no
 
 
def five_check(field, dy, dx, y, x):
    for z in range(1, 5):
        if field[y + (dy * z)][x + (dx * z)] != 'o':
            return False
    return True
 
 
for t in range(int(input())):
    answer = gomoku()
    print('#{} {}'.format(t+1, answer))