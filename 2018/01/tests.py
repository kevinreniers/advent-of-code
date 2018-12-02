from solution import FrequencyFinder, FrequencyAdder

adder_test = [
    [['+1', '+1', '+1'], 3],
    [['+1', '+1', '-2'], 0],
    [['-1', '-2', '-3'], -6]
]

finder_test = [
    [['+1', '-1'], 0],
    [['+3', '+3', '+4', '-2', '-4'], 10],
    [['-6', '+3', '+8', '+5', '-6'], 5],
    [['+7', '+7', '-2', '-7', '-4'], 14]
]

print('-- Adder Assertions --')
for changes, expected in adder_test:
    calced = FrequencyAdder.calc(changes)
    print(changes, calced, expected)
    assert calced == expected

print('-- Finder Assertions --')
for changes, expected in finder_test:
    finder = FrequencyFinder()
    frequency = finder.find(changes)
    print(changes, frequency, expected)
    assert frequency == expected
