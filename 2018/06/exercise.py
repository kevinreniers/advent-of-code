class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def distance_from(self, point):
        return abs(point.x-self.x) + abs(point.y-self.y)

class Grid:
    labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    def __init__(self, points):
        self.points = points
        self.x = max([point.x for point in points])
        self.y = max([point.y for point in points])
        self.grid = self.init_grid()
        print(f"Grid({self.x}, {self.y})")
    

    def draw(self):
        print("\n".join([" ".join(l) for l in self.grid]))
    
    
    def init_grid(self):
        row = '.' * (self.x+1)
        grid = [list(row) for _ in range(self.y+1)]
        for k, p in enumerate(self.points):
            grid[p.y][p.x] = self.labels[k]
        return grid


    def largest_area(self):
        largest = {}
        infinites = set()
        for k, _ in enumerate(self.points):
            largest[k] = 0
        for y, row in enumerate(self.grid):
            for x, _ in enumerate(row):
                comp_point = Point(x, y)
                distances = [p.distance_from(comp_point) for p in self.points]
                min_distance = min(distances)
                #print(comp_point, distances, min_distance, distances.count(min_distance))
                if distances.count(min_distance) == 1:
                    if x in (self.x, 0) or y in (self.y, 0):
                        infinites.add(distances.index(min_distance))
                    largest[distances.index(min_distance)] += 1
                else:
                    x = [str(p) for p in self.points if p.distance_from(comp_point) == min_distance]
                    #print(f"{comp_point} is closest ({min_distance}) to {distances.count(min_distance)} points: {x}")
        
        print('infs', infinites)
        p_wo_inf = [(k, p, str(self.points[k])) for (k, p) in largest.items() if k not in infinites]
        print(p_wo_inf)
        return max([largest[k] for (k, _, _) in p_wo_inf])
    

    def within_safe_area(self):
        area_size = 0
        for y, row in enumerate(self.grid):
            for x, _ in enumerate(row):
                comp_point = Point(x, y)
                distance_from_all = sum([p.distance_from(comp_point) for p in self.points])
                if distance_from_all < 10000:
                    area_size += 1
        return area_size

with open('test.txt', 'r') as f:
    grid = Grid([Point(*l.rstrip().split(', ')) for l in f])

grid.draw()
assert(grid.largest_area() == 17)

with open('test2.txt', 'r') as f:
    grid = Grid([Point(*l.rstrip().split(', ')) for l in f])

grid.draw()
assert(grid.largest_area() == 9)

with open('data.txt', 'r') as f:
    grid = Grid([Point(*l.rstrip().split(', ')) for l in f])

print(grid.largest_area())
print(grid.within_safe_area())