#!/bin/python
def insertionSort(ar):
    shift_num = ar[len(ar)-1]
    for i in range(1, len(ar)):
        if ar[len(ar) - i - 1] > shift_num:
            ar[len(ar) - i] = ar[len(ar) - i - 1]
            print " ".join(map(str, ar))
        else:
            break
    if ar[len(ar) - i - 1] > shift_num:
        ar[len(ar) - i - 1] = shift_num
    else:
        ar[len(ar) - i] = shift_num
    print " ".join(map(str, ar))


#m = 14
l = "1 3 5 9 13 22 27 35 46 51 55 83 87 60"
ar = [int(i) for i in l.strip().split()]
#ar = [str(i) for i in raw_input().strip().split()]
#print ar
insertionSort(ar)

