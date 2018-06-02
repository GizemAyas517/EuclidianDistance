from unittest import TestCase
import sys
import subprocess



from euclid import distance_between, Point, find_closest_points


class DistanceTests(TestCase):
    def setUp(self):
        pass

    def test_distance_1dim(self):
        p1 = (1,)
        p2 = (2,)
        p3 = (-1,)

        self.assertEquals(1, distance_between(p1, p2))
        self.assertEquals(2, distance_between(p1, p3))
        self.assertEquals(3, distance_between(p2, p3))

    def test_distance_2dim(self):
        p1 = (0,0)
        p2 = (3,4)
        p3 = (5,12)

        self.assertEquals(5, distance_between(p1, p2))
        self.assertEquals(13, distance_between(p1, p3))
        self.assertTrue(8 < distance_between(p2, p3) < 9)

    def test_distance_3dim(self):
        p1 = (0,0,0)
        p2 = (0,1,0)
        p3 = (0,0,1)

        self.assertEquals(1, distance_between(p1, p2))
        self.assertEquals(1, distance_between(p1, p3))

    def tearDown(self):
        pass


class ClosestDistanceTests(TestCase):

    def setUp(self):
        pass


    def test_distance_2dim(self):

        p1 = Point(line=0,points=[1, 1])
        p2 = Point(line=98,points=[2, 2])
        p3 = Point(line=7,points=[5,5])
        points = list()
        points.append(p1)
        points.append(p2)
        points.append(p3)


        self.assertEquals((p1,p2), find_closest_points(points))


    def test_distance_3dim(self):

        p1 = Point(line=0,points=[0, 0, 0])
        p2 = Point(line=98,points=[0, 1, 0])
        p3 = Point(line=7,points=[1, 1, 1])
        points = list()
        points.append(p1)
        points.append(p2)
        points.append(p3)


        self.assertEquals((p1,p2), find_closest_points(points))



    def tearDown(self):
        pass


