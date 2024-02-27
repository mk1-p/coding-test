import sys

problem = sys.stdin.readline().split(' ')
N = int(problem[0].strip())
M = int(problem[1].strip())
pocket_list = []
pocket_dict = dict()
for i in range(N):
    pocket_mon = sys.stdin.readline().strip()
    pocket_list.append(pocket_mon)
    pocket_dict[pocket_mon] = i + 1

for _ in range(M):
    req = sys.stdin.readline().strip()
    if req.isdigit():
        point = int(req) - 1
        print(pocket_list[point])
    else:
        print(pocket_dict[req])

