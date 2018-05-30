import math


class Point:
    def __init__(self, points, line):
        self.points = points
        self.line = line


"insert file name here"
file_name = "sample_input_100_100.tsv"

f = open(file_name, "r")

line = f.readline()
words = line.split()
dimension = words.__len__()


f.close()

f = open(file_name, "r")



points = list()
line_count = 1
for line in f:
    current_point = line.split()
    points.append(Point(points=current_point, line=line_count))
    line_count += 1




def distance_between(point_one, point_two):
    """

    :param point_one: multidimensional point, in array format
    :param point_two: multidimensional point, in array format
    :return: distance between point one and point two
    """
    sum = 0
    for d1,d2 in zip(point_one,point_two):
        sum += math.pow(float(d1) - float(d2), 2)

    return math.sqrt(sum)


def find_closest_points():
    closest_dist = float("inf")
    closest_points = None, None
    for y, point_one in enumerate(points):
        for x, point_two in enumerate(points):
            if x > y:
                dist= distance_between(point_one.points,point_two.points)
                if dist < closest_dist:
                    closest_dist = dist
                    closest_points= point_one.line, point_two.line

    return closest_points, point_one.points, point_two.points

print find_closest_points()[0]