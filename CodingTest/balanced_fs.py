
def createLineValues(parent, files_size, sizes, node):
    child_sizes = 0
    for i in range(len(parent)):
        if parent[i] == node:
            #total_sizes[node] += size
            #total_sizes[i] = size
            print("parent=" + str(node) + "|child=" + str(i))
            children = createLineValues(parent, files_size, sizes, i)
            child_sizes += children[0]
    size = files_size[node]
    sizes[node] = child_sizes + size
    return child_sizes + size, sizes

def mostBalancedPartition(parent, files_size):
    sizes = [0]*len(parent)
    node_size, sizes = createLineValues(parent, files_size, sizes, 0)
    print(sizes)
    cut_weight = []
    for n in sizes:
        cut_weight.append(abs(node_size - 2*n))
    print(cut_weight)
    print(cut_weight.index(min(cut_weight)))
    
    
    #print(sizes)

A=[-1, 0, 0, 1, 1, 3, 2, 6, 6]
B=[0, 1, 2, 3, 4, 5, 6, 7, 8]
mostBalancedPartition(A, B)