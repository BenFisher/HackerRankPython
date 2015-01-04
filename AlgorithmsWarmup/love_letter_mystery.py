import sys

# Result strings aren't needed, but are handy for creating the actual result palindromes
def find_alternating_characters(STR):
    l = STR[0:len(STR)/2]
    r = STR[len(STR)/2:len(STR)]
    l_res = ""
    r_res = ""
    num_ops = 0
    for idx in range(0, len(r)):
        try:
            n_l = ord(l[idx])
            n_r = ord(r[len(r) - idx - 1])
            num_ops += abs(n_l - n_r)
            if n_l > n_r:
                n_l = n_r
            l_res += chr(n_l)
            r_res = chr(n_l) + r_res
        except IndexError:
            l_res += STR[len(STR)/2]

    #print str(l_res + r_res) + ", ops=" + str(num_ops)
    return num_ops

def find_alternating_characters_concise(STR):
    num_ops = 0
    for idx in range(0, len(STR)/2):
        try:
            num_ops += abs(ord(STR[idx]) - ord(STR[len(STR) - idx - 1]))
        except IndexError:
            break
    return num_ops


num_tests = int(sys.stdin.readline())

for test in range(0,num_tests):
    print find_alternating_characters_concise(sys.stdin.readline().rstrip())