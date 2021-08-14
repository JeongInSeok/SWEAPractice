T = int(input())

# 가로 체크
def garo_check():
    ans = 0 
    for y in range(len(sudokuMap)):
        numbers=list(range(1,10))
        cnt = 0 
        for x in range(len(sudokuMap)):
            if sudokuMap[y][x] in numbers:
                numbers.remove(sudokuMap[y][x])
                cnt+=1
            else:
                return False 
        if cnt==9:
            ans+=1
    if ans == 9:
        return True
    return False
# 세로 체크 
def sero_check():
    ans = 0
    for y in range(len(sudokuMap)):
        numbers=list(range(1,10))
        cnt = 0 
        for x in range(len(sudokuMap)):
            if sudokuMap[x][y] in numbers:
                numbers.remove(sudokuMap[x][y])
                cnt+=1
            else:
                return False 
        if cnt==9:
            ans+=1
    if ans == 9:
        return True
    return False
# 3x3 영역 체크

def threetress():
    ans = 0 
    # 상자 3개씩 체크해야지
    for y in range(0,7,3):
        for x in range(0,7,3):
            numbers= list(range(1,10))
            cnt = 0 
            # 상자 하나 까봐야지
            for i in range(3): # 세로 i 아이
                for j in range(3): # 가로 j 제이
                    if sudokuMap[i+x][j+y] in numbers:
                        numbers.remove(sudokuMap[i+x][j+y])
                        cnt+=1
            if cnt==9:
                ans+=1
    if ans==9:
        return True
    return False



for test_case in range(1,T+1):
    # 스도쿠는 9x9 니까 
    sudokuMap = [list(map(int,input().split())) for _ in range(9)]

    if garo_check() and sero_check() and threetress():
        print('#{} 1'.format(test_case))
    else:
        print('#{} 0'.format(test_case))
    

    