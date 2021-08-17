def is_palindrome(str):
    n = len(str)
    for i in range(n//2):
        # 0 vs n-1, 1 vs n-2, 2 vs n-3, i vs n-1-i
        if str[i] != str[n-1-i]:
            return 0
    return 1
 
T = int(input())
for test_case in range(1, T+1):
    MAP = []
    N, M = map(int, input().split())
    for y in range(N):
        MAP.append(input())
    # 가로 회문 검사
    ans = ""
    for y in range(N):
        for x in range(N-M +1):
            temp_str = MAP[y][x:x+M]
            print('temp_str {}'.format(temp_str))
            ret = is_palindrome(temp_str) #O(M)
            if ret == 1:
                ans = temp_str
 
    # 세로 회문 검사
    for x in range(N):
        for y in range(N-M+1):
            if x == 5 and y ==0:
                de = -1
            temp_str = ""
            #O(M)
            for p in range(y, y+M):
                temp_str += MAP[p][x]
            #O(M)
            ret = is_palindrome(temp_str)
            if ret == 1:
                ans = temp_str
 
    print('#{} {}'.format(test_case, ans))
