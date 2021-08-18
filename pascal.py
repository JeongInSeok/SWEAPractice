T = int(input())

for test_case in range(1,T+1):
    N=int(input())

    pascal = [[1] * x for x in range(1,N+1)]
    for y in range(1, N-1):
        for x in range(len(pascal[y])-1):
            pascal[y+1][x+1] = pascal[y][x] + pascal[y][x+1]

    print("#{}".format(test_case))

    for pas in pascal:
        print(*pas)
