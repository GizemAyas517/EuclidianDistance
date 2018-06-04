Closest Points Finder
======

Given a txt or a tsv file of points, Closest Points Finder finds the closest points using euclidian distance.

Getting Started
------

### Installing

Download the project or clone with:

```
git clone https://github.com/GizemAyas517/EuclidianDistance.git
```

Usage
------

Open the project in an IDE and type the following to the terminal. For input_file_name, give the input file you want to use to the system.
For output_file_name, give the name of the output file you want the system to create or give an existing designated output file you want.
There's _no_ need to write the file names in quotes.

```
 python euclid.py --closest input_file_name output_file_name

 # or

 python euclid.py -c input_file_name output_file_name

 # use the flag -h or --help to learn more about the flags.

 # Example

 python euclid.py --closest sample_input_files/sample_input_4_4.tsv sample_output_files/sample_output_4_4.txt

 python euclid.py --closest sample_input_files/five_dimension_input sample_output_files/five_dimension_output


```
The output file is created by the program with the name _output_sample.txt_ under the project directory.

### Running with given or custom input files

Sample input and output files are in their correspoding directory in the project directory under sample_input_files and
sample_output_files respectively.

In addition to the given sample inputs, here are the custom input files and their corresponding outputs.

| Given Input file name | Tests edge case? | Output  |
| -------------          |:-------------:| :-------------:|
| empty_test_file        | Yes |No. Input file is empty. |
| unmatch_points_input  | Yes |No. Some points's dimensions doesn't match. |
| five_dimension_input | No |five_dimension_output.txt |
| just_one_point  | Yes | No. There should be more than 1 points in the input. |
| wrong_type_point  | Yes | No. The points should have only floats and integers as coordinates. |



Testing
------

### Test Coverage

Test file is named test.py under the project directory. It contains tests for functions distance_between() and
find_closest_points(), which are under euclid.py.

For distance_between(), sample points group and their known distances are tested for points in 1,2, and 3 dimensions. Three different points
are in sample points group for each dimension. A total of 3 distances are tested for each dimension as the
distance between the points in the sample points group.

For find_closest_points(), 3 points which are 3 dimensional are given as a set of points. The points are (0,0,0) , (0,1,0),
and (1,1,1) respectively. The closest amongst these three are the first and second ones. The test looks whether
or not the implemented function gives the correct pair of points. Same test is done for 2 dimensional points.

Checkout test.py file for more information.

### Running the test.py file

Run the following command:

```
pytest test.py
```

Implementation
------

Euclid.py has a brute force solution approach for finding the closest points problem. The time complexity of the algorithm is O(n^2) and the
space complexity is O(1).

Details of how the code works are inside the descriptions of functions in euclid.py.

There's another solution in file divide.py with a more optimized approach. The function is called "solution" in divide.py. The algorithm used in divide.py is as follows:

1. Transfer the points in the file to a points array.
2. Sort the points array according to each dimension in individual arrays, keep them in a list. (lets call this list _sortedlist_)
3. For each sorted array: divide them into two halves recursively and keep dividing until they can be solved with just 2 comparisons. (sub_array length maximum of 3)
4. Compare the minimum value of distance returned by each halve and the corresponding points.
5. Keep all the minimum values in a separate list for each array in _sortedlist_. Let's call this list _minimums_.
6. Return the minimum of the list _minimums_.

Divide.py's approach is similar to a divide and conquer solution. To find the time complexity of this algorithm we need to consider the number of
sorts and comparisons. The number of comparisons are: O(2*n*m). The number of sorts are: m. Each sort takes O(n*logn) time. So the total time
the sorting takes is O(n*logn*m).(m is the dimension)

### Usage of Divide.py

It is very similar to euclid.py. Here is an example:

```
python divide.py --closest sample_input_files/five_dimension_input sample_output_files/five_dimension_output
```


