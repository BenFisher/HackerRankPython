class QuickSort:
    debug = 0
    array = []
    num_comparisons = 0
    level = 0
    def __init__(self, A):
        self.array=A
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
        pivot_idx = r #self.pick_pivot(p, r)
        #self.swap(p,pivot_idx)  # Put the pivot element at the beginning of the subarray.
        pivot = self.array[r]
        for boundary_idx in range(p, r):
            if self.array[boundary_idx] < pivot:
                self.swap(boundary_idx, partition_idx)
                partition_idx+=1
        self.swap(r, partition_idx)
        print(" ".join(map(str, self.array)))
        return partition_idx

    def quicksort(self, p, r, level):
        if p<r:
            q=self.partition(p,r)
            self.quicksort(p, q-1,level+1)
            self.quicksort(q+1,r,level+1)


#raw_input()
ar = [str(i) for i in input().strip().split()]
#input_numbers = open('testcase3.txt', 'r')
#ar = [int(i) for i in input_numbers.readline().strip().split()]
A = QuickSort(ar)

print("\n\n" + str(A.array))