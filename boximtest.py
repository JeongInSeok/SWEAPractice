# 장난감을 보관할 상자 X x Y 크기의 골판지를 샀다.
# 5개의 직사각형으로 구성된 a x b x h 크기의 상자를 만들계획 
# 상자의 최대 부피를 계산하는 프로그램 작성
'''
정답은 도출가능하지만 시간이 오래걸림
def myrange(start, end, step):
    r = start
    while r < end:
        yield r
        r += step
'''
T = int(input())

for test_case in range(1,T+1):
    X, Y = map(int,input().split())
    # Y = b + (h * 2)
    # X = a + (h * 2)

    # result = (X-2*h)*(Y-2*h)*h  ( 3차 함수 )
    # (12*h*h)-(4*X*h)-(4*Y*h)+X*Y = 0 ( 미분 )
    # 근의 공식 -b + (b**2 - 4*a*c)**0.5 / 2a 

    h1 = (-((-4*X)+(-4*Y))+((-4*X+(-4*Y))**2-(4*12*(X*Y)))**0.5)/(2*12)
    h2 = (-((-4*X)+(-4*Y))-((-4*X+(-4*Y))**2-(4*12*(X*Y)))**0.5)/(2*12)
    
    if Y-(h1*2)>0 and X-(h1*2)>0:
        result = (X-(2*h1))*(Y-(2*h1))*h1
    elif Y-(h2*2)>0 and X-(h2*2)>0:
        result = (X-(2*h2))*(Y-(2*h2))*h2
 
    #result = (X-(2*h))*(Y-(2*h))*h
    '''
    maxval = -100
    폐기 
    # result = X*Y*h - 2*X*h*h - 2*Y*h*h
    for h in myrange(0,min(X,Y),0.0001):
        result = (X-2*h)*(Y-2*h)*h        
        if maxval < result:
            maxval = result
        if maxval > result:
            break
    '''


    print('#{} {:.6f}'.format(test_case, result))