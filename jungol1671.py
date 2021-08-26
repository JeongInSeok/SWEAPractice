# 가로 세로 크기가 각각 100인 정사각형 모양 흰색 도화지가 있다. 
# 가로 세로 크기가 10인 정사각형 색종이를 붙임 
# 색종이 여러장 붙인 다음 검은 영역의 둘레 길이를 구하는 프로그램 작성


lst = [ [0] * 100 for _ in range(100)]

# 색종이 갯수 N
# 입력값은 다음 좌표는 N의 갯수만큼 좌표깞 3 7  

result = 0 
N = int(input())
for n in range(N):
    Y, X = map(int,input().split())
    for i in range (0,10): 
        for j in range(0,10): # 선분의 개념으로 보면 11로 지정해야겠는데..
            # 1 갯수 세면 넓이 
            lst[Y+i][X+j] = 1
            

for y in range(len(lst)): # 100 
    for x in range(len(lst)):
        if lst[y][x] == 1:
            if x==99 and y==99:
                result+=2
                continue
            if x==99 and y==0:
                result+=2
                continue
            if x==0 and y==99:
                result+=2
                continue
            if x==0 and y==0:
                result+=2
                continue
            if x==99:
                result+=1
                if lst[y+1][x]==0:
                    result+=1
                if lst[y-1][x]==0:
                    result+=1
                continue
            if y==99:
                result+=1
                if lst[y][x+1]==0:
                    result+=1
                if lst[y][x-1]==0:
                    result+=1
                continue
            if lst[y-1][x]==0:
                result+=1
            if lst[y][x-1]==0:
                result+=1
            if lst[y+1][x]==0:
                result+=1
            if lst[y][x+1]==0:
                result+=1

print(result)

