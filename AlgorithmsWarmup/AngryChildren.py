import sys
import heapq


def num(s):
    try:
        return int(s)
    except ValueError:
        print "Invalid Number: " + s
        sys.exit(1)


class AngryChildren:
    variance_list = []
    candy_list = []

    def __init__(self, candies=None):
        if candies is not None:
            self.candy_list = candies
            self.setup_candies()

    def add_candy(self, candy):
        self.candy_list.append(candy)

    def setup_candies(self):
        self.candy_list.sort()
        idx = 1
        while idx < len(self.candy_list):
            self.variance_list.append(self.candy_list[idx] - self.candy_list[idx-1])
            idx += 1
        #self.variance_list.sort()

    def minimum_unfairness(self, num_children):
        unfairness = 0
        unfairness_heap = []
        i = 0
        #print self.candy_list
        #print self.variance_list
        for candy in self.variance_list:
            unfairness += self.variance_list[i]
            if i > num_children - 2:
                #print "\t" + str(i) + "\t" + str(self.variance_list[i - num_children + 1])
                unfairness -= self.variance_list[i - num_children + 1]
            #print unfairness
            if i >= num_children - 2:
                heapq.heappush(unfairness_heap, unfairness)
                #print unfairness_heap
            i += 1
        return heapq.heappop(unfairness_heap)


num_candies = num(sys.stdin.readline())
num_children = num(sys.stdin.readline())

#num_candies = 7
#num_children = 3
i = 0
angry_children = AngryChildren()
#candies = [1,5,3,9,11]
#candies = [10,100,300,200,1000,20,30]

while i < num_candies:
    angry_children.add_candy(num(sys.stdin.readline()))
    #angry_children.add_candy(candies[i])
    i += 1

angry_children.setup_candies()
print angry_children.minimum_unfairness(num_children)