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


if __name__ == '__main__':
    print('-- Results --')
    with open(r'in.txt') as file:
        hashes = file.readlines()
    print('Result of part 1: {}'.format(count_twos_and_threes(hashes)))