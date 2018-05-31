import math


class Point:
    """
    Point object has two attributes, a point array to keep all the coordinates and the line
    number of the point in the file.
    """
    def __init__(self, points, line):
        self.points = points
        self.line = line





def fill_points_list(filename):
    f = open(filename, "r")

    points = list()
    line_count = 1
    for line in f:
        current_point = line.split()
        points.append(Point(points=current_point, line=line_count))
        line_count += 1

    f.close()

    return points





def distance_between(point_one, point_two):
    """

    :param point_one:
    :param point_two:
    :return:
    """
    sum = 0
    for d1,d2 in zip(point_one,point_two):
        sum += math.pow(float(d1) - float(d2), 2)

    return math.sqrt(sum)


def find_closest_points(points):
    """
    Finds the closest points in a given list of Point objects.
    There are two for loops because I imagined the Point list this way.
    y -> represents the rows
    x -> represents the columns

    We only look at the top left triangle to avoid:
        1) comparing P1 and P2 -> Therefore getting a 0 as an answer and thinking into finding a solution this way.
        2) comparing P1 and P2 etc. twice.

    Unnecessary compares are avoided this way.

    [
           P1 P2 P3 P4
       P1 [0 1  2  3  ],
       P2 [1          ],
       P3 [2          ],
       P4 [3          ]


    ]

    :return: the closest poits's line numbers, the coordinates of the closest points points
    """
    closest_dist = float("inf")
    closest_points = None, None
    for y, point_one in enumerate(points):
        for x, point_two in enumerate(points):
            if x > y:
                dist= distance_between(point_one.points,point_two.points)
                if dist < closest_dist:
                    closest_dist = dist
                    closest_points= point_one, point_two

    return closest_points


def file_write(file,point):

    str1=' '.join(str(e) for e in point.points)
    file.write("%s:%s\n" % (str(point.line), str1))


def main():

    "insert input file name here"
    file_name = "sample_input_100_100.tsv"
    points = fill_points_list(file_name)
    point_one, point_two = find_closest_points(points)
    out = open("output_sample.txt","w")



    file_write(out, point_one)
    file_write(out, point_two)


    out.close()


if __name__ == "__main__":
    main()