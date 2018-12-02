import collections


def count_twos_and_threes(hashes: list):
    twos = 0
    threes = 0
    for hash in hashes:
        has_two = False
        has_three = False
        hash = collections.Counter(hash)
        for character in hash:
            if hash[character] == 2:
                has_two = True
            if hash[character] == 3:
                has_three = True
        if has_two:
            twos += 1
        if has_three:
            threes += 1
    return twos * threes


def off_by_one_index(first, second):
    if first == second:
        return False

    off_by_index = 0
    off_by = 0
    for i in range(0, len(first)):
        index_of_first = first[i]
        index_of_second = second[i]
        if index_of_first != index_of_second:
            off_by += 1
            off_by_index = i
        if off_by > 1:
            return False

    return off_by_index


def generate_secret_hash(hashes: list):
    for hash in hashes:
        for hash_cmp in hashes:
            off_by = off_by_one_index(hash, hash_cmp)
            if off_by is not False:
                return hash[:off_by] + hash[off_by+1:]


if __name__ == '__main__':
    print('-- Results --')
    with open(r'in.txt') as file:
        hashes = file.readlines()
    print('Result of part 1: {}'.format(count_twos_and_threes(hashes)))
    print('Result of part 2: {}'.format(generate_secret_hash(hashes)))