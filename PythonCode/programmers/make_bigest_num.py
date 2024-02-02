def solution(number, k):

    nl = list(number)
    first_num = (0,0)

    # k 범위 내 가장 큰 수 찾기
    for i, num in enumerate(number):
        tp = (int(num), i)
        curr_big = first_num[0]
        if curr_big < int(num):
            first_num = tp
        if i == k:
            break

    # 제거될 숫자의 값을 X로 변환
    x_cnt = 0
    for i, n in enumerate(nl):
        if x_cnt == k:
            break
        if i < first_num[1]:
            nl[i] = "X"
            x_cnt += 1
        elif len(nl)-1 > i and int(n) < int(nl[i + 1]):
            nl[i] = "X"
            x_cnt += 1

    # k = x_cnt 가 되지 않을 경우 역방향으로 제거해야한다.
    # 현재 X 값을 건너 뛰어 찾는 방법을 찾아야함.
    for i in range(len(nl)-1, x_cnt-1, -1):
        print(f'역방 {i} | nlen : {len(nl)}')
        if x_cnt == k:
            break
        if nl[i] == "X":
            continue
        if int(nl[i]) <= int(nl[i-1]):
            nl[i] = "X"
            x_cnt += 1

        # 역방향 검증 시 X 가 아닌 값을 찾아가야하는 로직 필요함

    number = ''.join(nl)
    number = number.replace("X", "")
    return number


solution(number="1924", k=2)
# 94
solution(number="1231234", k=3)
# 3234
solution(number="4177252841", k=4)
# 775841

solution(number="654312", k=2)
# 6543