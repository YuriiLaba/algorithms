prevCalculatedValues = {
    1:1,
    2:2,
    3:4
}

def stepPerms(n):
    if n in prevCalculatedValues.keys():
        return prevCalculatedValues[n]
    else:
        prevCalculatedValues[n] = stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)
        return stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)

if __name__ == '__main__':

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)