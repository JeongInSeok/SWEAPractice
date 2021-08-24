
def dfs(num, sum, cnt, path):
    global N
    global K
    global ans
    if cnt > N:
        return
    if sum > K:
        return
    if num == 21:
        if sum == K and cnt == N:
            ans += 1
        return
 
    dfs(num + 1, sum + num, cnt + 1, path + str(num))  # 부분집합에 포함
    dfs(num + 1, sum, cnt, path)  # 부분집합에 안포함
    return
 
T = int(input())
for test_ in range(1, T + 1):
    N, K = map(int, input().split())
    ans = 0
    dfs(1, 0, 0, "")
    print('#{} {}'.format(test_, ans))
