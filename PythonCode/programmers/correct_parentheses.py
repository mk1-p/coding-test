#https://school.programmers.co.kr/learn/courses/30/lessons/12909

input1 = "()()"
# return True
input2 = "(())()"
# return True
input3 = ")()("
# return False
input4 = "(()("
# return False


def solution(strs):
    stack = []

    # O(n)
    for s in strs:
        # 비교 문자열 변환, 괄호의 역방향으로 주어짐
        conv = ")" if "(" == s else "("

        # 스택이 존재하는 경우에 문자열 비교 진행
        if stack:
            if stack[len(stack) - 1] == conv:
                stack.pop()
            else:
                stack.append(s)
        # 스택이 존재하지 않는다면 괄호 시작인 경우에만 넘어감
        else:
            if s == ")":
                return False
            stack.append(s)

    return False if stack else True