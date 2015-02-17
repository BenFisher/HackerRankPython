class QuickSort:
    pivot_method = "mean of three"
    debug = 0
    array = []
    soln = []
    soln_elem = 0
    num_comparisons = 0
    level = 0
    def __init__(self, A, S):
        self.array=A
        self.soln = S
        self.quicksort(0,len(self.array)-1,0)

    # Simple swap. Happens during the partition.
    # Method used in course lecture. Not the only way to do this.
    def swap(self, i, j):
        if i != j:
            j_elem = self.array[j]
            self.array[j] = self.array[i]
            self.array[i] = j_elem

    # Call by quicksort to recurse.
    def partition(self, p, r):
        partition_idx = p
        boundary_idx = p
        self.num_comparisons += r-p
        if (self.debug):
                print "    p=" + str(p) + " r=" + str(r) + " comparisons=" + str(r-p)
        pivot_idx = r #self.pick_pivot(p, r)
        #self.swap(p,pivot_idx)  # Put the pivot element at the beginning of the subarray.
        pivot = self.array[r]
        if (self.debug):
            print "    pivot=" + str(pivot) + " pivot_idx=" + str(pivot_idx)
        for boundary_idx in range(p, r):
            if self.array[boundary_idx] < pivot:
                self.swap(boundary_idx, partition_idx)
                partition_idx+=1
        self.swap(r, partition_idx)
        pstr = " ".join(map(str, self.array))
        if pstr != self.soln[self.soln_elem]:
            print "line " + str(self.soln_elem) + " mismatch."
            print pstr
            print self.soln[self.soln_elem]
            exit(0)
        else:
            print pstr
            #print "line " + str(self.soln_elem) + " match."
        self.soln_elem += 1
        return partition_idx

    def quicksort(self, p, r, level):
        if p<r:
            q=self.partition(p,r)
            if(self.debug):
                print "    q=" + str(q)# + " Array=" + str(self.array)
            self.quicksort(p, q-1,level+1)
            self.quicksort(q+1,r,level+1)

solution_file = open('testcase3_solution.txt', 'r')
soln = [line.strip() for line in open('testcase3_solution.txt')]
   # [str(i) for i in solution_file.readlines().strip()]

input_numbers = open('testcase3.txt', 'r')
ar = [int(i) for i in input_numbers.readline().strip().split()]

A = QuickSort(ar, soln)

if A.array == sorted(A.array):
    print "Success"
else:
    print "Fail"
    Asort = A.array.sort()
    for i in range(0,len(A.array)):
        if A.array[i] != Asort[i]:
            print "element " + str(i) + " mismatch"
            print "A[i] = " + A.array[i]
            print "A_sort[i] = " + Asort[i]
            break
    print A.array