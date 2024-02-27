# [코딩테스트 연습 - 징검다리 | 프로그래머스 스쿨](https://school.programmers.co.kr/learn/courses/30/lessons/43236)


def solution(distance, rocks, n):

    rocks.sort()


    point = distance // 2
    rms = []
    while True :
        rms = []
        start = 0
        print(f'point : {point}')
        for i, rock in enumerate(rocks):
            if point >= (rock - start):
                rms.append(i)
            elif len(rocks)-1 == i and point >= (distance - rock):
                rms.append(i)
            start = rock

        if is_ok(rms, n) == 0:
            print(f'같아 {len(rms)}')
            break
        elif is_ok(rms, n) == -1:
            print(f'낮아 {len(rms)}')
            point = point + 1
        else:
            print(f'높아 {len(rms)}')
            point = point // 2

    rms.sort(reverse=True)

    for rm in rms:
        rocks.pop(rm)

    max_distance = 0
    start = 0
    for i, rock in enumerate(rocks):
        curr_dis = rock - start
        if curr_dis > max_distance:
            max_distance = curr_dis
        if i == len(rocks)-1 and (distance - rock) > max_distance :
            max_distance = (distance - rock)

    return max_distance
def is_ok(rms, n):
    if len(rms) == n:
        return 0
    elif len(rms) > n:
        return 1
    else:
        return -1


print(solution(distance=25, rocks=[2, 14, 11, 21, 17], n=2))


def solution1(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    left, right = 0, distance
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        min_distance = float('inf')
        current = 0
        remove_count = 0

        # 전체 바위 체크
        for rock in rocks:
            # 현재 위치에서 다음 바위의 거리
            diff = rock - current
            # 기준점보다 낮으면 지울 바위로 카운트 올림
            if diff < mid:
                remove_count += 1
            else:
                # 바위를 밟았다고 가정함
                current = rock
                min_distance = min(min_distance, diff)

        if remove_count > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = min_distance

    return answer


print(solution1(25, [2, 14, 11, 21, 17], 2))


