import sys
import heapq


def num(s):
    try:
        return int(s)
    except ValueError:
        print "Invalid Number: " + s
        sys.exit(1)

L = num(sys.stdin.readline())
R = num(sys.stdin.readline())
l = R
r = R - 1
heap = []

while l >= L and r >= L:
    print "\tl=" + str(l) + "\tr=" + str(r) + "\tl xor r = " + str(l ^ r)
    heapq.heappush(heap, -1 * (l ^ r))
    if l > L:
        l -= 1
    else:
        r -= 1
        l = r - 1

N = heapq.heappop(heap)
print N * -1