# Script for shortest path algorithm (TSP) where first and end points are fixed
# Created by Oliver Clarke 2021

import numpy as np
import pandas as pd
from scipy.spatial import distance_matrix
import routePlot

two_opt_swap = lambda r, i, k: np.concatenate((r[0:i], r[k:-len(r) + i - 1:-1], r[k + 1:len(r)]))

# 2-opt Algorithm
def two_opt(points, improvement_threshold):

    route = np.arange(points.shape[0])  # Make an array of row numbers corresponding to points.

    iterations = 0

    improvement_factor = 1  # Init improvement factor.

    best_distance = route_distance(points, route)  # Calculate the distance of the initial path.

    while improvement_factor > improvement_threshold:  # If the route is still improving, keep going!

        distance_to_beat = best_distance  # Record the distance at the beginning of the loop.

        # Fixed start (first point of array)
        #for swap_first in range(1, len(route) - 2):
            #for swap_last in range(swap_first + 1, len(route)):

        # Any points to start or end
        #for swap_first in range(0, len(route) - 2):
            #for swap_last in range(swap_first + 1, len(route)):

        # Fixed start and end (first and last points within input array)
        for swap_first in range(1, len(route) - 3):
            for swap_last in range(swap_first + 1, len(route) - 1):

                new_route = two_opt_swap(route, swap_first, swap_last)  # try reversing the order of these points

                new_distance = route_distance(points, new_route)  # calc total distance with this modification.

                if new_distance < best_distance:  # If the new route distance is an improvement,

                    route = new_route

                    best_distance = new_distance  # update best distance corresponding to this route.

                    routePlot.plot(points, route, 200, 10, 10, True, str(iterations)) # Plot each iteration

                    iterations += 1

        improvement_factor = 1 - best_distance / distance_to_beat  # Calculate how much the route has improved.

    print(route)

    return route  # When the route is no longer improving substantially, stop searching and return the route.


# Reverse the order of all elements from element i to element k in array r.
def reverseArray(array, i, k):

    return

    ###      UTILITY FUNCTIONS      ###


# Returns the Euclidean distance of two points in the Cartesian Plane.
def distance(pointA, pointB):

    return ((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2) ** 0.5


# Returns the length of the path passing through all the points in the given order.
def route_distance(points, route):

    pointsIndexedWithRoute = points[route] # Index coordinate points for route

    # Sum Euclidean distances between points of route
    totalDist = sum([distance(point, pointsIndexedWithRoute[index + 1]) for index, point in enumerate(pointsIndexedWithRoute[:-1])])

    return totalDist


def all_distances(points):

    dataX = np.asarray(points['x'])

    dataY = np.asarray(points['y'])

    data = np.array([dataX, dataY]).T

    ctys = np.asarray(points['Name'])

    print(data)

    print(ctys)

    df = pd.DataFrame(data, columns=['xcord', 'ycord'], index = ctys)

    all_distances_matrix = pd.DataFrame(distance_matrix(df.values, df.values), index=df.index, columns=df.index)

    return all_distances_matrix