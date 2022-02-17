import numpy as np

class LeastWorkAgent(object):
    def __init__(self, k = None):
        self.k = k

    def get_action(self, state):
        workers, job, _ = state

        size = job.size
        min_work_idx = None
        min_work = np.inf

        low, high = 0, len(workers)

        if size > 900 and self.k is not None: 
            low = len(workers) - self.k
        elif self.k is not None: 
            high = len(workers) - self.k

        for i in range(low, high):
            worker = workers[i]
            work = np.sum([j.size for j in worker.queue])
            if work < min_work:
                min_work_idx = i
                min_work = work

        return min_work_idx

class ShortestProcessingTimeAgent(object):
    def __init__(self, k = None):
        self.k = k

    def get_action(self, state):
        workers, job, _ = state

        size = job.size
        min_time_idx = None
        min_time = np.inf

        low, high = 0, len(workers)

        if size > 900 and self.k is not None: 
            low = len(workers) - self.k
        elif self.k is not None: 
            high = len(workers) - self.k

        for i in range(low, high):
            worker = workers[i]
            work = np.sum([j.size for j in worker.queue])
            remain_time = work / worker.service_rate
            if remain_time < min_time:
                min_time_idx = i
                min_time = remain_time

        if min_time_idx == None: 
            print("{} {} {} {} {}\n\n".format(self.k, low, high, size, len(workers)))
        return min_time_idx

class SizeSensitiveQueueAgent(object):
    def __init__(self):
        pass

    def get_action(self, state, k):
        workers, size, _ = state

        min_time_idx = None
        min_time = np.inf

        if size > 900:
            for i in range(len(workers) - k, len(workers)):
                worker = workers[i]
                work = np.sum([j.size for j in worker.queue])
                remain_time = work / worker.service_rate
                if remain_time < min_time:
                    min_time_idx = i
                    min_time = remain_time

            return workers[len(workers) - 1]

        for i in range(len(workers) - k):
            worker = workers[i]
            work = np.sum([j.size for j in worker.queue])
            remain_time = work / worker.service_rate
            if remain_time < min_time:
                min_time_idx = i
                min_time = remain_time

        return min_time_idx
