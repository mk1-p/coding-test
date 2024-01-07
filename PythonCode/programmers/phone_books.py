

# https://school.programmers.co.kr/learn/courses/30/lessons/42577

input1 = ["119", "97674223", "1195524421"]
# return false
input2 = ["123","456","789"]
# return  true
input3 = ["12","123","1235","567","88"]
# return false

def solution(phone_book):
    # 정렬하기 => 접두어가 되는 번호가 항상 인접한 위치에 있음
    phone_book.sort()

    # 현재 전화번호와 다음 전화번호를 순차 비교
    # 접두어가 있다면 False 반환
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    # 접두어가 없다면 True 반환
    return True

