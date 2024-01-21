# https://school.programmers.co.kr/learn/courses/30/lessons/42840?language=python3


def answer_generator1(index):
    return (index % 5) + 1

# def answer_generator2(index):
#     even_num = index % 2
#     return 2 if even_num == 0 else (int(index/2) % 5) + 1
def answer_generator2(index):
    answers = [1,3,4,5]
    even_num = index % 2
    return 2 if even_num == 0 else answers[int(index/2) % 4]

def answer_generator3(index):
    answers = [3,1,2,4,5]
    return answers[int(index/2) % 5]


def solution(answers):
    person1 = 0
    person2 = 0
    person3 = 0

    print(len(answers))

    for i, answer in enumerate(answers):
        print(f'index:{i}, answer:{answer} | {answer_generator1(i)} | {answer_generator2(i)} | {answer_generator3(i)}')
        if answer_generator1(i) == answer:
            person1 += 1
        if answer_generator2(i) == answer:
            person2 += 1
        if answer_generator3(i) == answer:
            person3 += 1

    persons = [(1,person1), (2,person2), (3,person3)]

    persons.sort(key=lambda x:x[1], reverse=True)
    max_num = persons[0][1]
    print(f'{person1} | {person2} | {person3}')
    values = []

    for person in persons:
        if person[1] == max_num:
            print(f'inner! : {person[0]}')
            values.append(person[0])
        else:
            break
    print('-----------')
    return values


solution(answers=[1,2,3,4,5])
# [1]
solution(answers=[1,3,2,4,2])
# [1,2,3]
solution(answers=[2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5])
# [2]
solution(answers=[1, 1, 1, 1, 1, 1])
# [1,3]