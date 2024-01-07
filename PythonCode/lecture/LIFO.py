

## 괄호 유효성 문제 LIFO 문제1
## 스택을 이용한 문제
## 괄호 (){}[]
## O(n) 의 시간복잡도
def isValid(s):
    stack = []
    for p in s:
        if p == "(":
            stack.append(")")
        elif p == "{":
            stack.append("}")
        elif p == "[":
            stack.append("]")
        elif not stack or stack.pop() != p:
            return False
    return not stack


## Temperatures LIFO 문제2
## 온도가 더 높은 날짜가 얼마 만에 오는가
temps = [73,71,69,67,72,76]
def dailyTemperatures(temperatures):
    ans = [0] * len(temperatures)
    stack = []
    for cur_day, cur_temp in enumerate(temperatures):
        print("[cur day : {0}][cur temp : {1}]",cur_day,cur_temp)
        count = 0
        while stack and stack[-1][1] < cur_temp:
            count += 1
            print(f'count : {count}')
            prev_day, _ = stack.pop()
            ans[prev_day] = cur_day - prev_day

        stack.append((cur_day,cur_temp))

    return ans

dailyTemperatures(temps)

