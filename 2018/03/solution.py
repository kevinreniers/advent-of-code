import re
from collections import namedtuple

Coordinate = namedtuple('Coordinate', ['x', 'y'])


class Claim:
    def __init__(self, id, x, y, width, length):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.length = length

    def coordinates(self):
        coordinates = list()
        for x in range(self.x, self.x + self.width):
            for y in range(self.y, self.y + self.length):
                coordinates.append(Coordinate(x, y))
        print('id={} x={} y={} width={} length={} cells={} coordinates={}'.format(
            self.id, self.x, self.y, self.width, self.length, self.width * self.length, len(coordinates)
        ))
        print('first coordinate: {}'.format(coordinates[0]))
        print('last coordinate: {}'.format(coordinates[-1]))
        return coordinates


def transform(claims: list):
    c = list()
    pattern = re.compile('^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    for claim in claims:
        match = pattern.match(claim)
        c.append(
            Claim(match.group(1), int(match.group(2)), int(match.group(3)), int(match.group(4)), int(match.group(5))))
    return c


def overlap_count(claims: list):
    """Return the amount of overlapping cells"""
    count = 0
    coordinates = dict()
    for claim in claims:
        for coordinate in claim.coordinates():
            coordinates[coordinate] = coordinates.get(coordinate, 0) + 1
    return len([coordinates[coordinate] for coordinate in coordinates if coordinates[coordinate] > 1])


if __name__ == '__main__':
    print('-- Results --')
    with open(r'in.txt') as file:
        claims = file.readlines()
    transformed_claims = transform(claims)
    count = overlap_count(transformed_claims)
    print('Solution part 1: ', count)
