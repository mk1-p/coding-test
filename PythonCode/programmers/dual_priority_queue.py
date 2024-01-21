import heapq


def solution(operations):

    hq = []

    for op in operations:
        cmd = op[0]
        num = int(op[1:].strip())
        # print(f'{op} >> {cmd} | {num}')

        if cmd == "I":
            heapq.heappush(hq, num)
        elif cmd == "D" and len(hq) > 0:
            if num == -1:
                heapq.heappop(hq)
            elif num == 1:
                hq.pop() # 이 부분에서 제일 낮은 깊이의 데이터들이 완전 정렬이 된 상태가 아니므로! 원하는 결과가 나오지 않음

    # hq.sort() 이 부분을 넣은면 테스트 케이스는 통과했지만 위의 pop 부분이 틀어진다는건 변하지 않는다.

    return [hq[len(hq)-1], hq[0]] if len(hq) >= 1 else [0, 0]






solution(operations=["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
# [0, 0]

solution(operations=["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])
# [333, -45]

solution(operations=["I 1", "I 2", "D 1", "D -1", "I 3", "I 4", "D 1"])