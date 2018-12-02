from solution import count_twos_and_threes

test_twos_and_threes = [
    [['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab'], 12]
]

test_off_by_one = [
    [['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz'], 'fgij']
]

print('-- TwosThrees Assertions --')
for hashes, expected in test_twos_and_threes:
    score = count_twos_and_threes(hashes)
    print('{} score={} expected={} [{}]'.format(hashes, score, expected, 'OK' if score == expected else 'NOK'))
    assert score == expected
