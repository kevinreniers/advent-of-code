with open('test.txt', 'r') as f:
    numbers = sorted([int(s) for s in f])

print('test', numbers)

def find2020(numbers):
    for n in numbers:
        for n2 in numbers:
            if n+n2 == 2020:
                return n*n2

result = find2020(numbers)
print('result', result)
assert(result == 514579)

with open('data.txt', 'r') as f:
    numbers = sorted([int(s) for s in f])

result = find2020(numbers)
print('result', result)

def find2020_3(numbers):
    for n in numbers:
        for n2 in numbers:
            for n3 in numbers:
                if n+n2+n3 == 2020:
                    return n*n2*n3

result = find2020_3(numbers)
print('result', result)