import sys

def num(s):
    try:
        return int(s)
    except ValueError:
        print "Invalid Number: " + s
        sys.exit(1)

class Fibo:
    fib_list = [];

    def __init__(self):
        self.build_fib_list()
        #print self.fib_list

    def build_fib_list(self):
        prev_num = 0;
        curr_num = 1;
        self.fib_list.append(prev_num)
        self.fib_list.append(curr_num)

        while curr_num < 1000000000:
            new_num = prev_num + curr_num
            self.fib_list.append(new_num)
            prev_num = curr_num
            curr_num = new_num

    def test_num(self, num):
        if num in self.fib_list:
            print "IsFibo"
        else :
            print "IsNotFibo"

num_tests = num(sys.stdin.readline())
tested = 0
fibo = Fibo()

while tested < num_tests:
    fibo.test_num(num(sys.stdin.readline()))
    tested+=1