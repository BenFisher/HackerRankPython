
def testUsername(user):
    user_list = list(user)
    n = len(user_list)
    for i in range(n):
        for j in range(i+1, n):
            c_j = user_list[j]
            c_i = user_list[i]
            print([i, j, c_i, c_j])
            if c_j < c_i:
                return True
    return False

def testUsernamesOptimized(user):
    user_list = [ord(c) for c in list(user)]
    for i in range(1, len(user_list)):
        if user_list[i-1] > user_list[i]:
            return True
    return False 


def possibleChanges(usernames):
    ret = []
    for name in usernames:
        t = testUsernamesOptimized(name)
        if t == True:
            ret.append('YES')
        else:
            ret.append('NO')
    return ret

t = ['bee', 'superhero', 'ace']

print(testUsername('ace'))
changes = possibleChanges(t)
print(changes)
