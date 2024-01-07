

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
# return [4, 1, 3, 0]

def solution(genres, plays):

    dict_music = dict() # 뮤직 카테고리 : (인덱스, 플레이수)
    dict_cont = dict()  # 뮤직 카테고리 : 총 플레이수

    # 리스트 -> 딕셔너리
    for i in range(len(genres)):
        key = genres[i]
        value = plays[i]
        elem = (i, value)

        if key in dict_music:
            dict_music[key].append(elem)
            dict_cont[key] += value
        else:
            dict_music[key] = list()
            dict_music[key].append(elem)
            dict_cont[key] = value

    # 카테고리 별 정렬 후 상위 2개의 플레이 뮤직 인덱스를 추출
    answer = []
    for k, v in sorted(dict_cont.items(), key=lambda x: x[1], reverse=True):
        print(dict_music[k])
        picked_musics = sorted(dict_music[k], key=lambda x: x[1], reverse=True)[0:2]

        for music in picked_musics:
            answer.append(music[0])

    return answer


solution(genres, plays)