from solution import react, basic_react, optimised_react, is_opposite

is_opposite_test = [
    [['a', 'A'], True],
    [['A', 'a'], True],
    [['a', 'a'], False],
    [['A', 'A'], False]
]

basic_tests = [
    ['dabAcCaCBAcCcaDA', 'dabCBAcaDA']
]

optimized_tests = [
    ['dabAcCaCBAcCcaDA', 4]
]

if __name__ == '__main__':
    for input, expected in is_opposite_test:
        assert is_opposite(input[0], input[1]) == expected

    assert react('dabAcCaCBAcCcaDA') == 'dabAaCBAcaDA'

    for input, expected in basic_tests:
        assert basic_react(input) == expected

    for input, expected in optimized_tests:
        assert len(optimised_react(input)) == expected