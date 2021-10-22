# Class for plotting route for TSP task
# Oliver Clarke 2021

import matplotlib.pyplot as plt
import numpy as np
import algorithms

def plot(points, route, dpi, widith, height, showOrSave, saveName):

    # plotting a line plot after changing it's width and height
    f = plt.figure()
    f.set_figwidth(widith)
    f.set_figheight(height)

    # Reorder the cities matrix by route order in a new matrix for plotting.
    newPointsOrder = np.concatenate((np.array([points[route[i]] for i in range(len(route))]), np.array([points[0]])))

    # Use ggplot stylesheet (https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)
    with plt.style.context('ggplot'):

        # Label axis and title plot
        plt.xlabel("\nx axis" + '\n\n' + 'Distance: ' + str(round(algorithms.route_distance(points, route), 2)) + '\n')
        plt.ylabel("\ny axis")
        plt.title("Optimal route generation using 2-opt algorithm." + '\n')

        # Plot the cities.
        plt.scatter(points[:, 0], points[:, 1], marker='.', color='black')

        # Plot the path.
        plt.plot(newPointsOrder[:len(newPointsOrder) - 1, 0], newPointsOrder[:len(newPointsOrder) - 1, 1], linewidth=0.5, color='fuchsia')


        if showOrSave == True:
            plt.savefig(saveName, dpi=dpi)

        else:
            plt.show(dpi=dpi)



    # Print the route as row numbers and the total distance travelled by the path.
    print("Route: " + str(route) + "\n\nDistance: " + str(algorithms.route_distance(points, route)))