def twoStrings(s1, s2):
    hash_table = {}
    for ch in s1:
        if ch in hash_table:
            hash_table[ch] += 1
        else:
            hash_table[ch] = 1
    
    for ch in s2:
        if ch in hash_table:
            return "YES"
    return "NO"

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')
