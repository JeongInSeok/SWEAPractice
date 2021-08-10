'''
강변에 빌딩들이 옆으로 빽빽하게 밀집한 지역이 있다.
이곳에서는 빌딩들이 너무 좌우로 밀집하여, 강에 대한 조망은 모든 세대에서 좋지만 왼쪽 또는 오른쪽 창문을 열었을 때 바로 앞에 옆 건물이 보이는 경우가 허다하였다.

그래서 이 지역에서는 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다고 말한다.
빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.
아래와 같이 강변에 8채의 빌딩이 있을 때, 연두색으로 색칠된 여섯 세대에서는 좌우로 2칸 이상의 공백이 존재하므로 조망권이 확보된다. 따라서 답은 6이 된다.
'''
T=10
for test_case in range(1,T+1):
    w = int(input())
    height = list(map(int, input().split()))
    ans = 0 # 조망권 확보된 세대 수를 누적하는 변수
    for i in range(2, w - 2):
        # height[i]
        # height[i-2] vs height[i-1] vs height[i+1]
        max_height = int(-21e8)  # -21억
        if max_height < height[i - 2]:
            max_height = height[i - 2]
        if max_height < height[i - 1]:
            max_height = height[i - 1]
        if max_height < height[i + 1]:
            max_height = height[i + 1]
        if max_height < height[i + 2]:
            max_height = height[i + 2]
        # 0 x 8 => 1억, 만x만 = 1억
 
        tmp = height[i] - max_height
        if tmp > 0:
            ans += tmp
    print('#{} {}'.format(test_case, ans))