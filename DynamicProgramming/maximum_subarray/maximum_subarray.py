
def max_subarray(ar, S):
    curr = int(ar[0])
    max_contig = curr
    curr_contig = curr
    max_non_contig = curr

    for i in range(1, len(ar)):
        curr = int(ar[i])

        if curr_contig < 0:
            curr_contig = 0
        if curr > 0:
            if max_non_contig < 0:
                max_non_contig = curr
            else:
                max_non_contig += curr

        curr_contig += curr
        if curr_contig > max_contig:
            max_contig = curr_contig

    print str(max_contig) + " " + str(max_non_contig)
    # return max_contig == int(S[0]) and max_non_contig == S[1]

T = int(sys.stdin.readline())
for i in range(0,T):
    N = int(sys.stdin.readline())
    ar = [str(i) for i in raw_input().strip().split()]
    max_subarray(ar)


input_numbers = open('input2', 'r')
results = open('output2', 'r')
T = int(input_numbers.readline())
for test in range(0, T):
    N = int(input_numbers.readline())
    A = [int(i) for i in input_numbers.readline().strip().split()]
    S = [int(i) for i in results.readline().strip().split()]
    res = max_subarray(A, S)
    if res == 0:
        print "\tTest " + str(test) + " failed."
    else:
        print "\tTest " + str(test) + " passed."