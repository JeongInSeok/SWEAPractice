
T = int(input())
for test_case in range(1, T+1):
    lst = []
    for i in range(2): # i는 0, 1 2번 실행
        lst.append(list(input()))

    dic_t = {}
    for s in lst[1]:
        if s in lst[0]:
            dic_t[s] = dic_t.get(s, 0) + 1

    # get("키값", 0)
    # get ( 키값 , 키값에 해당하는 value가 없을 때 반환할 값 )
    try:
        print("#{} {}".format(test_case, max(list(dic_t.values()))))
    except ValueError as ve:
        print("#{} 해당하는 값 없음".format(test_case))

