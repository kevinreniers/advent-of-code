from solution import OverlapCalculator, transform, WithoutOverlapFinder

tests = [
    [['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2'], 4]
]

for claims, expected in tests:
    transformed_claims = transform(claims)
    overlaps = OverlapCalculator.overlapping_cells(transformed_claims)
    overlaps = len(overlaps)
    print('{} overlap={} expected={} [{}]'.format(claims, overlaps, expected, 'OK' if overlaps == expected else 'NOK'))
    assert overlaps == expected
    for exclusive in WithoutOverlapFinder.exclusive_claim(transformed_claims):
        print(exclusive.id)