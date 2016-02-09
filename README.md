# point-grouping-test
A coding challenge for a Platform Engineer.

This repo contains the instructions and template to complete a coding challenge in Python. It is aimed at Python programmers of mid-level experience and up, and is designed to test the programmer's skill in designing and implementing algorithms. 

No external libraries are required—however, due to the algorithmic/numerical nature of the code at hand, Python libraries that provide robust implementations of various mathematical or statistical algorithms might be useful. The programmer should feel free to calibrate their approach to their own experience level. 

# Instructions

## The goal
One of the most enduring technical challenges at MakeSpace involves generating the routes that our vans and trucks run every day. A good routing algorithm has to take a group of points on a map and group them according to how many vans we want to run that day.

`points.json` is a JSON data file that contains a list of objects representing geographic points, with a `lat`, `lon` and `id`. Your job is to write a Python script that will take an integer argument *n*, then read the file and output the `id`s of all the points, grouped into *n* groups, into a second file, `groups.json`.

Given that the data set represents geographic data, you should try to group points by proximity, so that the geographically closest points are grouped together. 

## Stretch goal #1

The file `utils.py` is a Python module that contains a function, `driving_time_and_distance`. This function is pulled from our van routing logic. Given four values representing an origin and destination lat/lon, it will return two values: the driving time and distance between those two points. Write a script that works like above, but uses this function as the function to determine distance between the two points.

## Stretch goal #2

When grouping addresses to produce our daily routes, it's important that each van has roughly the same number of stops to make in a day. Do the same as above, with one final optimization - optimize for both geographical proximity, using the function in the first stretch goal, *and* for equal group size for each van.
