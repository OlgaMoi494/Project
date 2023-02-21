class Vector:
    def __init__(self, start_points: tuple, end_points: tuple):
        self.start_points = start_points
        self.end_points = end_points

    def length(self):
        x1, y1 = self.start_points[0], self.start_points[1]
        x2, y2 = self.end_points[0], self.end_points[1]
        length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        return length

    def __lt__(self, other):
        return self.length() < other.length()

    def __gt__(self, other):
        return self.length() > other.length()

    def __ge__(self, other):
        return self.length() >= other.length()

    def __le__(self, other):
        return self.length() <= other.length()

    def __eq__(self, other):
        return self.length() == other.length

    def __ne__(self, other):
        return self.length() != other.length
