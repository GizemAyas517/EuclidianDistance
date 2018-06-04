import argparse
import sys

from euclid import PointError, file_write, find_dimesion, distance_between, find_closest_points


def fill_just_points(filename):
    """

    :param filename:
    :return:
    """
    file = open(filename, "r")
    points = list()
    dimension = find_dimesion(filename)
    flag = False

    for line in file:
        point = line.split()
        if dimension == len(point):
            new_points=list()
            for el in point:
                new_points.append(float(el))
            points.append(new_points)
        else:
            flag = True
            break

    if flag:
        print PointError()
        sys.exit()

    return points

def change_str_to_float(array):
    new_array=list()
    for item in array:
        new_array.append(float(item))
    return new_array



def create_output_file(lines, points, filename):
    out = open(filename,"w")
    point_one = points[0]
    point_two = points[1]

    str1=' '.join(str(e) for e in point_one)
    str2 = ' '.join(str(e) for e in point_two)
    out.write("%s:%s\n" % (str(lines[0]), str1))
    out.write("%s:%s\n" % (str(lines[1]), str2))



def find_line_numbers(pointone, pointtwo, filename):

    file=open(filename,"r")
    line1,line2 = 0,0
    for index,line in enumerate(file):
        points = line.split()
        compare = change_str_to_float(points)
        print points
        if compare == pointone:
            line1 = index+1
        elif compare == pointtwo:
            line2 = index+1


    return line1,line2





def compare_min_values(list):

    #list will have values in the form (p1,p2,m)
    sorted_list = sorted(list,key=lambda x : x[2]) # sorted according to min values
    smallest = sorted_list[0]

    return smallest


def find_midpoint_index(array):
    return len(array) // 2


def split_array_from_midpoint(array,mid):
    left = array[:mid]
    right = array[mid:]
    return left, right


def split_from_point(array, point, dimension):

    left = list()
    right = list()

    for item in array:
        if item[dimension] < point[dimension]:
            left.append(item)
        else:
            right.append(item)

    return left, right


def sort_for_dimensions(point_array):
    """

    :param point_array: a 2 dimensional array
    :return: array of sorted arrays
    """
    sorted_arrays=list()
    dimension = len(point_array[0])
    for dim in range(dimension):
        sorted_arrays.append(sorted(point_array, key=lambda x:x[dim]))

    return sorted_arrays


def solution(points):
    sorted_arrays = sort_for_dimensions(points)

    min = float("inf")
    pointx,pointy = None, None

    for array in sorted_arrays:
        (p1,p2,m) = closest_pair(array)
        if m < min :
            min = m
            pointx = p1
            pointy = p2

    return pointx, pointy


def closest_pair(sorted_arrays):

    if len(sorted_arrays) <= 3:
        return brute(sorted_arrays)

    mid = find_midpoint_index(sorted_arrays)
    first ,second = split_array_from_midpoint(sorted_arrays,mid)

    small = list()
    small.append(closest_pair(first))
    small.append(closest_pair(second))

    d = compare_min_values(small)[2]
    points = compare_min_values(small)[0],compare_min_values(small)[1]

    return points[0], points[1], d


def brute(array):
    closest_dist = float("inf")
    closest_points = None, None
    for y, point_one in enumerate(array):
        for x, point_two in enumerate(array):
            if x > y:
                dist = distance_between(point_one, point_two)
                if dist < closest_dist:
                    closest_dist = dist
                    closest_points = point_one, point_two
    return closest_points[0],closest_points[1], closest_dist


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str, help="input file name")
    parser.add_argument("output", type=str, help="output file name")
    parser.add_argument('-c', "--closest", action="count",
                        help='Find closest points in input file and write to output file.', required=True)

    file_name = parser.parse_args().input
    output_filename = parser.parse_args().output

    points = fill_just_points(file_name)

    closest_points = solution(points)
    lines = find_line_numbers(closest_points[0],closest_points[1],file_name)
    create_output_file(lines,closest_points,output_filename)


if __name__ == "__main__":
    main()
