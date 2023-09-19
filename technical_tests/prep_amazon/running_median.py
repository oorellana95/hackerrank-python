
from heapq import heappush, heappop


def runningMedian(a):
    running_median = []

    for i in range(len(a)):
        base = sorted(a[0:i+1])
        length = len(base)
        median_position = length // 2

        median_value = base[median_position]
        if length % 2 == 0:
            median_value = (base[median_position - 1] + median_value) / 2
        running_median.append(median_value)

    return running_median


def runningMedianOptimized(a):
    _min_heap, _top_heap = [], []
    running_median = []

    for number in a:
        if not _top_heap or number > _top_heap[0]:
            heappush(_top_heap, number)
        else:
            heappush(_min_heap, -number)  # for lowers we need a max heap

        if len(_min_heap) - len(_top_heap) > 1:
            heappush(_top_heap, -heappop(_min_heap))
        elif len(_top_heap) - len(_min_heap) > 1:
            heappush(_min_heap, -heappop(_top_heap))

        if len(_min_heap) == len(_top_heap):
            running_median.append((-_min_heap[0] + _top_heap[0]) / 2)
        elif len(_min_heap) > len(_top_heap):
            running_median.append(-_min_heap[0])
        else:
            running_median.append(_top_heap[0])

    return running_median


if __name__ == '__main__':

    a_count = 5

    a = [12, 4, 5, 3, 8, 13]

    result = runningMedianOptimized(a)
    print(result)
