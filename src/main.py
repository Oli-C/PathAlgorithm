import numpy as np
import dataLoader
import algorithms
import routePlot

# Oliver Clarke 2021

# TASK:
# We would like the shortest path starting from Point 1 and travelling via
# all the other points to Point 60. Every point must be visited at least 1 time.
# The sequence may be whatever you suggest apart from Point 1 being the fixed starting point
# and Point 60 the fixed end point.

# MAIN
if __name__ == '__main__':

    # Launch Test Case
    #points = dataLoader.testCaseCircle()

    # Load and convert data from .csv
    points = dataLoader.convertLatAndLong('data.csv')

    # Run 2-opt local search algorithm on data
    route = algorithms.two_opt(points, 0.001)