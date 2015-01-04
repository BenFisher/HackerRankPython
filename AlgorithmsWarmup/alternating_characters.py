import sys

def find_del_chars(STR):
    del_chars = ""
    curr_char = STR[0]
    for idx in range(1, len(STR)):
        new_char=STR[idx]
        if new_char == curr_char:
            del_chars += new_char
        else:
            curr_char = new_char
    return del_chars


num_tests = int(sys.stdin.readline())

for test in range(0,num_tests):
    print len(find_del_chars(sys.stdin.readline()))
