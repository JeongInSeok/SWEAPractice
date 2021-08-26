# S/W 문제해결 기본 Magnetic 

for test_case in range(1, 11) :
    length = int(input())
    magnets = []
    for _ in range(length) :
        magnets.append(list(map(int, input().split())))

    count = 0
    for i in range(length) :
        state = 0
        for j in range(length) :
            if magnets[j][i] == 1 and state == 0 :
                state = 1
            elif magnets[j][i] == 2 and state == 1 :
                state = 0
                count += 1

    print("#{} {}".format(test_case, count))