import sys

N = int(sys.stdin.readline().strip())

temp_set = set()

for _ in range(N):
    command = sys.stdin.readline().strip().split()
    method = command[0]
    x = int(command[1]) if len(command) > 1 else None

    if method == 'add':
        temp_set.add(x)
    elif method == 'remove':
        temp_set.discard(x)
    elif method == 'check':
        print(1 if x in temp_set else 0)
    elif method == 'toggle':
        if x in temp_set:
            temp_set.remove(x)
        else:
            temp_set.add(x)
    elif method == 'all':
        temp_set = set(range(1, 21))
    elif method == 'empty':
        temp_set.clear()
