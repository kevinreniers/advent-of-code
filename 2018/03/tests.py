from solution import overlap_count, transform

tests = [
    [['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2'], 4]
]

for claims, expected in tests:
    transformed_claims = transform(claims)
    overlaps = overlap_count(transformed_claims)
    print('{} overlap={} expected={} [{}]'.format(claims, overlaps, expected, 'OK' if overlaps == expected else 'NOK'))
    assert overlaps == expected
