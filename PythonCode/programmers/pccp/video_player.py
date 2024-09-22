def solution(video_len, pos, op_start, op_end, commands):
    # video_len 총 길이
    # pos 현재 위치
    # op_start 오프닝 시작 시각
    # op_end 오프닝 종료 시각
    # commands 명령어

    if op_start <= pos <= op_end:
        pos = op_end

    for command in commands:

        if command == 'next':
            pos = calc_time(pos, 10)

        elif command == 'prev':
            pos = calc_time(pos, -10)

        if op_start <= pos <= op_end:
            pos = op_end

        if pos < '00:00':
            pos = '00:00'
        elif pos > video_len:
            pos = video_len

    return pos


def calc_time(current_time, time):

    times = current_time.split(':')
    minute = int(times[0])
    second = int(times[1])
    second = second + time
    if second < 0:
        minute -= 1
        second = 60 + second
        if minute < 0:
            minute = 0
            second = 0
    elif second >= 60:
        minute += 1
        second = second - 60

    return f'{minute:02}:{second:02}'



result = solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"])
print(result)

result = solution("07:22", "04:05", "00:15", "04:07", ["next"])
print(result)


# https://school.programmers.co.kr/learn/courses/30/lessons/340213?language=python3