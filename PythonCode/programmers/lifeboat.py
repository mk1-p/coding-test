from collections import deque

def solution1(people, limit):
    people.sort(reverse=True)
    pdq = deque(people)

    cnt = 0
    while pdq:

        big_p = pdq.popleft()
        cnt += 1

        empty_weight = limit - big_p
        if empty_weight < 40:
            continue

        waits = []
        while pdq:
            min_p = pdq.pop()
            near_weight = empty_weight - min_p

            if near_weight < 0 and waits:
                waits.pop()
                pdq.append(min_p)
                waits.sort(reverse=True)
                pdq.extend(waits)
                break
            elif near_weight == 0:
                waits.sort(reverse=True)
                pdq.extend(waits)
                break

            waits.append(near_weight)
    print(cnt)
    return cnt


def solution2(people, limit):
    # people.sort(reverse=True)

    dict_wp = dict()
    keys = []
    for p in people:
        if p in dict_wp:
            dict_wp[p] += 1
        else:
            dict_wp[p] = 1
            keys.append(p)

    cnt = 0
    point = 0

    keys.sort(reverse=True)
    for i, key in enumerate(keys):
        weight = key
        print(key)
        num = dict_wp[key]

        if cnt == len(people):
            break
        if num == 0:
            continue

        empty_weight = limit - weight

        print(f'low empty : {weight} | cnt : {cnt}')
        if empty_weight < 40:
            cnt += num
            dict_wp[key] = 0

            continue

        for j in range(i, len(keys)):
            vs_weight = keys[j]
            vs_num = dict_wp[keys[j]]
            conv_weight = empty_weight - vs_weight
            print(f'conv f | {weight} | {vs_weight}')

            if conv_weight < 0:
                continue
            if vs_num == 0:
                continue

            conv_num = num - vs_num

            if conv_weight == 0:
                print("조건 충족")
                cnt += int(num/2+0.6)
                print(cnt)
                dict_wp[key] = 0
                break
            if conv_num == 0:
                cnt += num
                dict_wp[keys[j]] = 0
                dict_wp[key] = 0
                break
            if conv_num > 0:
                cnt += vs_num
                dict_wp[keys[j]] = 0
                dict_wp[key] -= vs_num
                num = dict_wp[key]
                continue
            if j == len(keys) - 1:
                cnt += num
                dict_wp[key] = 0
                break

    print(cnt)
    return cnt



        # 보트에 동승 가능한 무게의 값이 존재하는지 찾아간다.



        # 해당 무게의 소지 값 - 동승 가능한 무게의 소지 값



def solution(people, limit):
    people.sort(reverse=True)
    pdq = deque(people)

    cnt = 0
    print(pdq)
    while pdq:

        big_p = pdq.popleft()
        cnt += 1
        print(f'bigger : {big_p}')

        empty_weight = limit - big_p
        if empty_weight < 40:
            continue

        # for _ in range(0, len(pdq)):


        while pdq:
            low_p = pdq.pop()
            if empty_weight >= low_p:
                print(f'with : {low_p} | emp : {empty_weight}')
                break
            else:
                pdq.append(low_p)
                break



    print(cnt)





solution(people=[70, 50, 80, 50], limit=100)
# 3
# solution(people=[70, 80, 50], limit=100)
# 3