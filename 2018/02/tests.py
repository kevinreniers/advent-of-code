from solution import count_twos_and_threes, generate_secret_hash

test_twos_and_threes = [
    [['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab'], 12]
]

test_off_by_one = [
    [['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz'], 'fgij'],
    [['aaaa', 'aaab'], 'aaa'],
    [['aaaa', 'aabb'], None]
]

print('-- TwosThrees Assertions --')
for hashes, expected in test_twos_and_threes:
    score = count_twos_and_threes(hashes)
    print('{} score={} expected={} [{}]'.format(hashes, score, expected, 'OK' if score == expected else 'NOK'))
    assert score == expected

print('-- TwosThrees Assertions --')
for hashes, expected in test_off_by_one:
    score = generate_secret_hash(hashes)
    print('{} hash={} expected={} [{}]'.format(hashes, score, expected, 'OK' if score == expected else 'NOK'))
    assert score == expected
