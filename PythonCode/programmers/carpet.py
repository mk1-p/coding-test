def solution(brown, yellow):

    total = brown + yellow
    measures = []

    for i in range(3, int(total ** (1 / 2)) + 1):
        print(i)
        if total % i == 0:
            if total//i < i:
                break
            measures.append((total//i, i))

    answer = None
    if len(measures) == 1:
        answer = measures[0]
    else:

        while measures:
            answer = measures.pop()
            vir = answer[0]
            hor = answer[1]
            conv_br = (vir * 2) + (hor * 2) - 4

            if brown == conv_br:
                break
    return answer






solution(brown=10, yellow=2)
# [4,3]
solution(brown=8, yellow=1)
# [3,3]
solution(brown=24, yellow=24)
# [24,24]
