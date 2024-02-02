
global cnt
cnt = 0

def findNext(point, visits, cis):
    global cnt
    cnt += cis[point]
    visits[point] = True

    if len([x for x in visits if x == False]) == 0:
        return

    a_cnt = 0
    r_cnt = 0

    print("-----")
    a_near = -1
    r_near = -1
    for i in range(1, len(cis)//2 + 1):
        temp_loc = i + point
        print(f'temp : {temp_loc}')
        loc = abs(temp_loc - (len(cis)-1)) if temp_loc > (len(cis)-1) else temp_loc
        # loc = temp_loc if temp_loc <= (len(cis) - 1) else temp_loc - (len(cis) - 1)
        print(f'loc : {loc}')

        if visits[loc]:
            continue
        elif visits[loc] == False and a_near == -1:
            a_near = loc
            a_cnt += 1
        elif visits[loc] == False:
            a_cnt += 1

    print("-----")
    for i in range(1, (len(cis)//2) + 1):
        temp_loc = point - i
        print(f'temp : {temp_loc}')
        # loc = temp_loc if temp_hf >= 0 else len(cis) - 1 + temp_hf
        loc = temp_loc if temp_loc >= 0 else (len(cis)) + temp_loc
        print(f'loc : {loc}')

        if visits[loc]:
            continue
        elif visits[loc] == False and r_near == -1:
            r_near = loc
            r_cnt += 1
        elif visits[loc] == False:
            r_cnt += 1

    print(f'an: {a_near} | ac: {a_cnt}')
    print(f'rn: {r_near} | rc: {r_cnt}')
    print(visits)

    if a_near != -1 and r_near != -1:

        if a_cnt > r_cnt:
            cnt += abs(a_near - point)
            point = a_near
        elif r_cnt > a_cnt:
            cnt += abs(r_near - point)
            point = r_near
        else:
            if abs(a_near - point) > abs(r_near - point):
                cnt += abs(a_near - point)
                point = a_near
            else:
                cnt += abs(r_near - point)
                point = r_near

        # if abs(a_near - point) == abs(r_near - point):
        #     if a_cnt > r_cnt:
        #         cnt += abs(a_near - point)
        #         point = a_near
        #     else:
        #         cnt += abs(r_near - point)
        #         point = r_near
        # elif abs(a_near - point) < abs(r_near - point):
        #     cnt += abs(a_near - point)
        #     point = a_near
        # else:
        #     cnt += abs(r_near - point - 1)
        #     point = r_near

    elif a_near != -1 and r_near == -1:
        cnt += abs(a_near - point)
        point = a_near
    elif a_near == -1 and r_near != -1:
        cnt += abs(r_near - point - 1)
        point = r_near


    print(f'next point : {point} | cnt : {cnt}')
    print("=========")
    findNext(point, visits, cis)


def solution(name):

    visits = []
    cis = []



    for i, char in enumerate(name):
        print(f'{i} - {char} : {ord(char)-65}')
        a_ci = ord(char)-65
        r_ci = 26 - a_ci
        ci = a_ci if a_ci < r_ci else r_ci
        visits.append(True) if ci == 0 else visits.append(False)
        cis.append(ci)

    print(f'init visit : {visits}')

    findNext(point=0, visits=visits, cis=cis)

    print(cnt)
    return cnt



solution(name="JEROEN")
# # 56
# solution(name="JEROE")
# solution(name="JAN")
# # 23
# solution(name="JAZ")
# solution(name="JAAAAAAZ")
#
# solution(name="BAAABAAB")
# solution(name="BBAAAAAB")
# solution(name="AABBAAAB")
# solution(name="AABBAAA")
