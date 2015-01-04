import sys

def num(s):
    try:
        return int(s)
    except ValueError:
        print "Invalid Number: " + s
        sys.exit(1)

def test_digits(test_string):
    found_int = []
    split_string = test_string.split()

    for elem in split_string:
        num_elem = num(elem)
        if elem in found_int:
            found_int.remove(num_elem)
        else:
            found_int.append(num_elem)
    return found_int[0]

num_digits = num(sys.stdin.readline())
lone_int = test_digits(sys.stdin.readline())
print lone_int
