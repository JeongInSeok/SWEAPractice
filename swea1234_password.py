for test_case in range(1, 11) :
    # N은 문자열의 길이 string은 비밀번호
    N, string = input().split()
    N = int(N)
    string = list(string)

    i = 0
    while(True) :
        if string[i] == string[i+1] :
            del(string[i:i+2])
            N -= 2
            i -= 2
            # 문자열 길이가 2 줄어들고 다시 뒤에서부터 검사하도록 i를 마이너스 2
        i += 1
        if i == (N-1) :
            break

    password = ''
    for i in range(N) :
        password += string[i]

    print("#{} {}".format(test_case, password))