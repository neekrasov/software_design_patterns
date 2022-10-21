class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Rectangle(list):
    def __init__(self, x, y , width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))

class LineToPointAdapter:
    cache = {}
    def __init__(self, line):
        self.h = hash(line)
        if self.h in self.cache:
            return
        
        print(f"Generating points for line "
              f"[{line.start.x},{line.start.y}] -> "
              f"[{line.end.x},{line.end.y}] (caching)")
        
        points = []
        
        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = max(line.start.y, line.end.y)
        dx = right - left
        dy = line.end.y - line.start.y
        
        if dx == 0:
            for y in range(top, bottom):
                points.append(Point(left, y))
        elif dy == 0:
            for x in range(left, right):
                points.append(Point(x, top))
        else:
            slope = dy / dx
            y = top
            for x in range(left, right + 1):
                points.append(Point(x, y))
                y += slope
                
        self.cache[self.h] = points
    
    def __iter__(self):
        return iter(self.cache[self.h])

def draw_point(p):
    print(f"point ({p.x}, {p.y})")

def draw(rcs):
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)
        
if __name__ == "__main__":
    rs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]
    draw(rs)
    draw(rs)