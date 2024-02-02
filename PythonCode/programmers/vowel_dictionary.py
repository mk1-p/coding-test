# https://school.programmers.co.kr/learn/courses/30/lessons/84512



# ["X","A","E","I","O","U"]

global cnt
cnt = 0

def back_t(word, cur_ivs):

    u_point = 0
    global cnt

    vows = ["A", "E", "I", "O", "U"]
    for i, vow in enumerate(vows):
        if cur_ivs[0] != 0:
            break

        if word[0] == vow:
            cur_ivs[0] = i+1
            cnt += 1
            break
        else:
            cnt += 781

    for i in range(4, -1, -1):
        if check_text(word, cur_ivs):
            return
        if cur_ivs[i] == 0:
            cur_ivs[i] += 1
            cnt += 1
            continue
        else:
            break

    while u_point == 0:

        for i in range(4, -1, -1):

            if check_text(word, cur_ivs):
                return

            cnt += 1

            if cur_ivs[i] != 5:
                cur_ivs[i] += 1
                break

            elif cur_ivs[i] == 5:
                u_point = i
                break

    for i in range(4, -1, -1):
        if u_point == 0:
            print(f'up 0 브레이크 : {u_point}')
            break
        elif i >= u_point:
            cur_ivs[i] = 0
            print(f'0 변환 : {i} -- {cur_ivs[i]} | u point {u_point}')
            continue
        elif i < u_point and cur_ivs[i] == 5:
            cur_ivs[i] = 0
            print(f'0 변환 : {i} -- {cur_ivs[i]} | u point {u_point}')
            continue
        elif i < u_point and cur_ivs[i] != 5:
            cur_ivs[i] += 1
            print(f'수치 업 : {i} -- {cur_ivs[i]} | u point {u_point}')
            break

    u_point = 0

    back_t(word, cur_ivs)

def check_text(word, cur_ivs):
    vows = ["A", "E", "I", "O", "U"]
    text = "".join([vows[i - 1] for i in cur_ivs if i != 0])
    print(text)
    if text == word:
        return True
    else:
        return False



def solution(word):
    cur_iv = [0,0,0,0,0]
    back_t(word,cur_iv)
    return cnt


# solution(word="AAAAE")
# 6
solution(word="AAAE")
# 10
# solution(word="I")
# # 1563
# solution(word="EIO")
# # 1189

# solution(word="AUUUU")
# solution(word="E")
