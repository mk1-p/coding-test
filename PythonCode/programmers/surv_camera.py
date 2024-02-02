# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    # 차량의 경로를 진출 지점 기준으로 정렬
    routes.sort(key=lambda x: x[1])
    # 카메라의 수
    camera_count = 0
    # 마지막으로 설치된 카메라의 위치
    camera_position = -30001

    for route in routes:
        # 현재 차량의 진입 지점이 마지막으로 설치된 카메라 위치보다 크다면,
        # 새로운 카메라가 필요함
        if route[0] > camera_position:
            camera_count += 1
            camera_position = route[1]

    return camera_count


# 테스트 케이스 실행
test_routes = [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]
solution(test_routes)
