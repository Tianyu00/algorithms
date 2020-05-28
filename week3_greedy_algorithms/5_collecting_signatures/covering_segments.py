# Uses python3
import sys
from collections import namedtuple
from operator import attrgetter

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    segments = sorted(segments, key=attrgetter('end'))
    while len(segments) > 0:
        # segments_tmp = [x for x in segments if x.start < segments[0].end]
        points.append(segments[0].end)
        segments = [x for x in segments if x.start > points[-1]]
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
