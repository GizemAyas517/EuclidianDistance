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

Closest points finder is used with an existing file of points. Open the project in an IDE and
type the following to the terminal:

```
python euclid.py --filename filename

 #or

python euclid.py -f filename

 # use the flag -h or --help to learn more about the flags.

```
The output file is creatde by the program with the name _output_sample.txt_ under the project directory.

### Running the test.py file

Test.py runs tests for distance_between() and find_closest_points() functions in euclid.py
To run the tests in test.py, run the following command:

```
python -m unittest test
```


Acknowledgements
------
- Inspiration for the readme file from [template].(https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
