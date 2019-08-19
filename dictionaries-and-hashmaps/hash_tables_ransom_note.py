def checkMagazine(magazine, note):
    hash_table = {}
    for word in magazine:
        if word in hash_table:
            hash_table[word] += 1
        else:
            hash_table[word] = 1

    for word in note:
        if word not in hash_table:
            return "No"
        if hash_table[word] == 0:
            return "No"
        else:
            hash_table[word] -= 1
    return "Yes"


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))