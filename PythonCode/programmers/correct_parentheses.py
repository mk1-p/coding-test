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
        conv = ")" if "(" == s else "("

        if stack:
            if stack[len(stack) - 1] == conv:
                stack.pop()
            else:
                stack.append(s)
        else:
            if s == ")":
                return False

            stack.append(s)

    return False if stack else True