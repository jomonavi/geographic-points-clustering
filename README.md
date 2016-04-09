# point-grouping-test

A coding challenge for a Platform Engineer.

One of the most enduring technical challenges at MakeSpace involves generating the routes that our vans and trucks run every day. A good routing algorithm has to take a group of points on a map and group them according to how many vans we want to run that day. Your job will be to implement this step.

## Instructions

**Your solution should be presented as a standalone script we can run from command line using different input data files, and obtain corresponding output data files.**

Please include instructions, comments and anything you deem relevant for us to evaluate your solution.

You can submit it as a Github repository or compressed file.

### The main goal: grouping

`points.json` is a JSON data file that contains a list of objects representing geographic points, with a `lat`, `lon` and `id`. Your job is to write a Python script that will take an integer argument *n*, then read the file and output the `id`s of all the points, grouped into *n* groups, into a second file, `groups.json`.

Given that the data set represents geographic data, you should try to group points by proximity, so that the geographically closest points are grouped together. You should end up with a clean partitioning of the overall space.

### Stretch goal: distribution

When grouping addresses to produce our daily routes, it's important that each van has roughly the same number of stops to make in a day. Do the same as above, with one final optimization - optimize for both geographical proximity, using the function in the first stretch goal, *and* for equal group size for each van.

## About

This repo contains the instructions and template to complete a coding challenge in Python. It is aimed at Python programmers of mid-level experience and up, and is designed to test the programmer's skill in designing and implementing algorithms. 

No external libraries are required—however, due to the algorithmic/numerical nature of the code at hand, Python libraries that provide robust implementations of various mathematical or statistical algorithms might be useful. The programmer should feel free to calibrate their approach to their own experience level. 

Please do not hesitate to ask us any questions before submitting your solution!

## My Solution
I implemented 2 different algorithms for this problem, k-means and DBSCAN. K-means was a better fit for how this problem was supposed to be solved, as it always assigns every point to an nth cluster. With the DBSCAN, due to how disparate some of the points where, it would mark some points as "Noise", and not assign them to any cluster, but this may have been more of an issue with selecting the proper ε for the problem at hand. Either algorithms can be used inside of the group_points.py file, by importing the classes and initializing them with the right parameters. DBSCAN is initialized with all the points as a python dict, and k-means is initialized with the points as a dict, k(or n) as an integer specifying the amount of clusters, and the iterations as an integer specifying how many times you want k-means to run. 
