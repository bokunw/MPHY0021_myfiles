# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 2019

@author: Bokun Wei
"""

import numpy as np
from matplotlib import pyplot as plt
from argparse import ArgumentParser


class MakeTreeNP(object):

    def __init__(self, numbers_of_layers, scale_change, spread, size_scale):
        """ The constructor for the MakeTree class, setting up the initial
        parameters to plot a graph of the tree

        Parameters
        -------
        numbers_of_layers: int
            number of the layers the tree has, going from bottom to top
        scale_change: double
            how much the size scaling of the branches change for each layer
        spread: double
            how much the branches of the tree will spread out
        size_scale: double
            the initial size scale of the tree from the bottom

        """
        self.numbers_of_layers = numbers_of_layers
        self.scale_change = scale_change
        self.spread = spread
        self.size_scale = size_scale

    def update_x(self, old_x, angle):
        """update the x coordinate of the splitting point given the old point
        and the angle

        Parameters
        -------
        old_x: ndarray
            all the old x coordinates of the previous points to be updated
        angle: ndarray
            all the angle information of the old points, which are used
            to calculate the new x coordinate

        Returns
        -------
        ndarray
            the updated new x coordinate of the new splitting point
        """
        new_x = np.add(old_x, self.size_scale*np.sin(angle))
        return new_x

    def update_y(self, old_y, angle):
        """update the y coordinate of the splitting point given the old point
        and the angle

        Parameters
        -------
        old_y: ndarray
            all the old y coordinates of the previous points to be updated
        angle: ndarray
            all the angle information of the old points, which are used
            to calculate the new y coordinate

        Returns
        -------
        ndarray
            the updated new y coordinate of the new splitting point
        """
        new_y = np.add(old_y, self.size_scale*np.cos(angle))
        return new_y

    def produce_tree(self, plot=True, tree_starting_point=[0, 0],
                     x_pos=0, y_pos=1, angle=0):
        """ this function produce the tree by determining the coordinate
        of each splitting point and optionally plot them

        Parameters
        -------
        plot: bool
            whether to produce the plot or not
        tree_starting_point: list
            coordinate of the starting position of the tree
        x_pos: double
            x position of the first splitting point of the tree
        y_pos: double
            y position of the first splitting point of the tree
        angle: double
            angle information of the first splitting point of the tree

        """
        # define the initial splitting point
        old_splitting_points = np.array([[x_pos], [y_pos], [angle]])
        if plot:
            # plot the first line from bottom
            plt.plot(tree_starting_point, [x_pos, y_pos])

        while self.numbers_of_layers > 0:  # go through the layers
            # get the x, y and angle into separate numpy arrays
            all_x, all_y, all_angle = old_splitting_points
            # calculate new angles using numpy operations
            all_angle_left = np.subtract(all_angle, self.spread)
            all_angle_right = np.add(all_angle, self.spread)
            # update all x coordinates using numpy operations
            all_x_left = self.update_x(all_x, all_angle_left)
            all_x_right = self.update_x(all_x, all_angle_right)
            # update all y coordinates using numpy operations
            all_y_left = self.update_y(all_y, all_angle_left)
            all_y_right = self.update_y(all_y, all_angle_right)
            # combine the left and right branches
            all_new_x = np.hstack([all_x_left, all_x_right])
            all_new_y = np.hstack([all_y_left, all_y_right])
            all_new_angle = np.hstack([all_angle_left, all_angle_right])
            # put the x, y and angle information together and ready to be
            # updated
            new_splitting_points = np.array([all_new_x, all_new_y,
                                             all_new_angle])
            # create x, y coordinates for the plot, since each old splitting
            # point create 2 branches, the points for the plot need to be
            # doubled
            x_plot = np.hstack([all_x, all_x])
            y_plot = np.hstack([all_y, all_y])
            # plot the tree
            if plot:
                plt.plot([x_plot, all_new_x], [y_plot, all_new_y])

            # update the splitting point for next layer
            old_splitting_points = new_splitting_points
            # change size for the next layer
            self.size_scale *= self.scale_change
            self.numbers_of_layers -= 1
        if plot:
            plt.savefig('tree_np.png')


if __name__ == "__main__":
    parser = ArgumentParser(description="Produce tree strcture")
    parser.add_argument("numbers_of_layers")
    parser.add_argument("scale_change")
    parser.add_argument("spread")
    parser.add_argument("size_scale")
    arguments = parser.parse_args()

    tree = MakeTreeNP(int(arguments.numbers_of_layers),
                      float(arguments.scale_change), float(arguments.spread),
                      float(arguments.size_scale))
    tree.produce_tree()
