for test_case in range(1,11):
    dump = int(input())
    box = list(map(int, input().split()))
    while dump:
        max_box = max(box)
        min_box = min(box)
        max_idx = box.index(max(box))
        min_idx = box.index(min(box))

        box[max_idx] -= 1
        box[min_idx] += 1
        dump -= 1

    print('#{} {}'.format(test_case,max(box)-min(box)))