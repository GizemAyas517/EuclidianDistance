import math


class Point:

    def __init__(self, points, line):
        self.points = points
        self.line = line


"insert file name here"
file_name = "sample_input_2_8.tsv"

f = open(file_name,"r")

line = f.readline()
words = line.split()
dimension = words.__len__()


"close the file to get the dimension first"
f.close()

f = open(file_name,"r")

"get the points array"

points=list()
line_count = 0
for line in f:
    "['-262972', '508697']  --> burda su halder"
    current_point = line.split()
    points.append(Point(points=current_point, line=line_count))
    line_count+=1


def basic_euclidian(point_one, point_two):
    "sqrt(sum(distances of xs and ys and etc)))"
    "works on floating or integer"
    sum=0
    for index in range(dimension):
        sum += math.pow(point_one[index]-point_two[index],2)

    return math.sqrt(sum)


def no_optimization_helper(points_array, start_point):
    "every point will go through here"
    start_euclidian = basic_euclidian(start_point, points_array[0].points)
    closest_points = []
    for point in points_array:
        euclidian = basic_euclidian(start_point,point.points)
        if euclidian < start_euclidian:
            start_euclidian = euclidian
            closest_points = [start_point, point]

    return closest_points, start_euclidian

"we need to have current smallest euclidian"















