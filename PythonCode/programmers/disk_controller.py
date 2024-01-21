import heapq
import copy

class Process:
    def __init__(self, req, time, point):
        self.point = point
        self.gap = req > point
        self.total_time = req + time if req >= point else (point - req) + time
        self.end_time = req + time if req >= point else point + time
        self.req = req
        self.time = time

    def __lt__(self, other):

        if self.gap < other.gap:
            return True
        elif self.gap == other.gap:
            if self.total_time < other.total_time:
                return True
            elif self.total_time == other.total_time:
                return self.req < other.req
            else:
                return False
        else:
            return False

    def __str__(self):
        return f'req : {self.req} | time : {self.time} | {self.total_time}'


def solution1(jobs):

    processes = []
    for job in jobs:
        processes.append(Process(job[0], job[1], 0))

    heapq.heapify(processes)
    total_process = 0

    while processes:
        curr = heapq.heappop(processes)

        dc = copy.deepcopy(processes)
        processes.clear()
        total_process += curr.total_time

        for c in dc:
            heapq.heappush(processes, Process(c.req, c.time, curr.end_time))

    return int((total_process)/len(jobs))


# solution([[0, 3], [1, 9], [2, 6]])
# -> 9


def solution(jobs):

    curr_time = 0
    heapq.heapify(jobs)

    # while jobs:
            


