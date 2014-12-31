import sys

def num(s):
    try:
        return int(s)
    except ValueError:
        print "Invalid Number: " + s
        sys.exit(1)

class AngryChildren:
    variance_list = []
    candy_list = []

    def __init__(self, candies = None):
        if candies is not None:
            self.candy_list(candies)


    def setup_candies(self, in_candy_list):
        candy_list = in_candy_list.sort();

        idx = 1
        while idx < len(self.candy_list):
            self.variance_list.add(self.candy_list[idx] - self.candy_list[idx-1])
            idx += 1


    def minimum_unfairness(self, num_children):



    def test_num(self, num):
        if num in self.fib_list:
            print "IsFibo"
        else :
            print "IsNotFibo"

num_candies = num(sys.stdin.readline())
tested = 0


while tested < num_tests:
    fibo.test_num(num(sys.stdin.readline()))
    tested+=1

fibo = AngryChildren()