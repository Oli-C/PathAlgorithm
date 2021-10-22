# Script for loading and manipulating .csv data for processing by algorithms.py
# Created by Oli Clarke 2021
import numpy as np
import pandas as pd
from math import radians,cos,sin
import matplotlib.pyplot as plt


# Loads .csv file and prints the contents
def loadAndPrintData(data):
    points = pd.read_csv(data)
    print(points)

# Converts Latitude and Longitude values to cartesian (x,y)
def convertLatAndLong(data):

    # Converting lat, long from: http://www.geomidpoint.com/example.html

    points = pd.read_csv(data)
    lat = points["Latitude"].map(radians)
    lon = points["Longitude"].map(radians)
    x = lon.map(cos) * lat.map(cos) * 6371
    y = lon.map(cos) * lat.map(sin) * 6371

    points["x"] = x
    points["y"] = y

    # Print and Plot to check cartesian conversion
    #print(points)
    #plotCartesianPoints(points)

    converted_points = points.drop(["Name","Latitude", "Longitude"], 1)

    return np.asarray(converted_points)

def plotCartesianPoints(points):

    plt.scatter(points['x'], points['y'])
    plt.show()

# Function to hold test circle data
def testCaseCircle():
                     #   x         y
    circleCoords = ([[-0.0000, -1.0000],
                         [0.9511, 0.3090],
                          [0.3090, -0.9511],
                          [-0.8090, 0.5878],
                          [0.0000, 1.0000],
                          [0.5878, -0.8090],
                          [-0.5878, -0.8090],
                          [0.5878, 0.8090],
                          [0.9511, -0.3090],
                          [-0.9511, 0.3090],
                          [0.8090, 0.5878],
                          [-0.5878, 0.8090],
                          [-0.3090, 0.9511],
                          [0.3090, 0.9511],
                          [-0.9511, -0.3090],
                          [-1.0000, 0.0000],
                          [0.8090, -0.5878],
                          [-0.8090, -0.5878],
                          [1.0000, -0.0000],
                          [-0.3090, -0.9511]])

    return circleCoords