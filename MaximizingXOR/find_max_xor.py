import sys

# The max xor between L and R is the bitmaps with 1's in each bit from 0 to the max position where
# R=1 and L=0. So 10=1010, 1=0001, so res=1111; res=15 in decimal
def find_max_xor (l, r):
    c = l ^ r
    res = 1
    # assume 4 byte int
    for idx in range(0,31):
        # shift a^b to the right
        c = c >> 1
        # construct res by setting 1's and shifting left
        res = (res << 1) + 1
        # if current c | 1 = 1 we have the most significant bit difference. break and return res.
        if c | 1 == 1:
            print idx
            break
    return res

L = int(sys.stdin.readline())
R = int(sys.stdin.readline())

print find_max_xor(L, R)