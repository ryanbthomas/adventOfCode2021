import math

class lineSegment:
    def __init__(self, start, end):

        rise = end[1] - start[1]
        run = end[0] - start[0]
        slope = None
        if run != 0:
            slope = rise / run

        self.isDiag = slope == None or slope == 0 
        self.points = lineSegment.find_all_points(start, end) 
    
    def find_all_points(start, end):

        rise = end[1] - start[1]
        rise_step = 1 if rise >= 0 else -1
        run = end[0] - start[0]
        run_step = 1 if run >= 0 else -1

        if rise == 0:
            return [(x, start[1]) for x in range(start[0], end[0] + run_step, run_step)]
        
        if run == 0:
            return [(start[0], y) for y in range(start[1], end[1] + rise_step, rise_step)]
        
        step = int(run / math.gcd(rise, run))

        return [(x, int(rise/run * (x - start[0]) + start[1])) for x in range(start[0], end[0] + run_step, step)]

    def __str__(self):
        out = str(self.points[0])
        for pt in self.points[1:]:
            out += "--{}".format(pt)
        return out
    
    def __repr__(self):
        return "LineSegment: {} -> {}".format(self.points[0],self.points[-1])

if __name__ == "__main__":

    test = lineSegment((8,0), (0, 8))
    print(type(test))
    print(test) 