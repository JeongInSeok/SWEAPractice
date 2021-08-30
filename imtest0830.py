
# 1번 부터 N번 까지 n개의 led 등 설치

# ON/OFF 2 상태

# i 버튼 누르면 i의 배수 LED 변화 (ON->OFF OFF->ON)

# led 패턴이 주어질 때 led가 모두 꺼진 상태에서 원하는 패턴을 만들기 위한 최소 스위치 조작 횟수
# 00000 -> 주어진 LED 값으로 변해야함.



# 1번 부터 N번 까지 n개의 led 등 설치

# ON/OFF 2 상태

# i 버튼 누르면 i의 배수 LED 변화 (ON->OFF OFF->ON)

# led 패턴이 주어질 때 led가 모두 꺼진 상태에서 원하는 패턴을 만들기 위한 최소 스위치 조작 횟수
# 00000 -> 주어진 LED 값으로 변해야함.

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    LED= list(map(int,input().split()))
    LED.insert(0,0)

    firstled = [0] * (N+1) # LED가 모두 꺼져있는 상태
    cnt = 0
    for i in range(N+1):
        if firstled[i] != LED[i]:
            cnt+=1
            if i==0:
                for zero in range(N+1):
                    if firstled[zero]==0:
                        firstled[zero]=1
                    elif firstled[zero]==1:
                        firstled[zero]=0
            elif i==1:
                for zero in range(1, N + 1):
                    if firstled[zero] == 0:
                        firstled[zero] = 1
                    elif firstled[zero] == 1:
                        firstled[zero] = 0
            else:
                for j in range(i,N+1,i):
                    if firstled[j]==0:
                        firstled[j]=1
                    elif firstled[j]==1:
                        firstled[j]=0
    print('#{} {}'.format(test_case, cnt))