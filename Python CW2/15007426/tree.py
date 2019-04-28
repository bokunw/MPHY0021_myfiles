# -*- coding: utf-8 -*-
"""
Created on Fri Jan 4 2019

@author: Bokun Wei
"""

from math import sin, cos
from matplotlib import pyplot as plt
from argparse import ArgumentParser


class MakeTree(object):

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

    def update_splitting_point(self, current_point):
        """given the info on previous point where branches separates, info on
        the next splitting point is determined

        Parameters
        -------
        current_point: list
            contain info of a splitting point including x position, y position
            and angle

        Returns
        -------
        list
            info of the new updated splitting point including x position,
            y position and angle
        """
        current_xpos, current_ypos, current_angle = current_point
        # calculating the angle information of the new splitting point
        new_angle = current_angle + self.spread
        # calculating the x coordinate of the new splitting point
        new_x = current_xpos + self.size_scale*sin(new_angle)
        # calculating the y coordinate of the new splitting point
        new_y = current_ypos + self.size_scale*cos(new_angle)

        return [new_x, new_y, new_angle]

    def reverse_spread(self):
        """reverse the sign on the spread i.e. decide if it's left or
        right branch"""

        self.spread = -self.spread

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
        old_splitting_points = [[x_pos, y_pos, angle]]
        if plot:
            # plot the first line from bottom
            plt.plot(tree_starting_point, [x_pos, y_pos])

        while self.numbers_of_layers > 0:  # go through the layers
            new_splitting_points = []
            for splitting_point in old_splitting_points:
                # get the x, y angle info from the previous splitting point
                current_xpos, current_ypos, current_angle = splitting_point
                # get the new splitting point on the right
                new_right = self.update_splitting_point(splitting_point)
                self.reverse_spread()
                # get the new splitting point on the left
                new_left = self.update_splitting_point(splitting_point)
                self.reverse_spread()
                # store the above calculated results
                new_splitting_points.append(new_left)
                new_splitting_points.append(new_right)
                # obtain the x, y coordinates of new splitting point
                new_xpos_left, new_ypos_left, new_angle_left = new_left
                new_xpos_right, new_ypos_right, new_angle_right = new_right

                if plot:
                    # plot the lines connecting the splitting point
                    plt.plot([current_xpos, new_xpos_left],
                             [current_ypos, new_ypos_left])
                    plt.plot([current_xpos, new_xpos_right],
                             [current_ypos, new_ypos_right])
            # update the splitting point for next layer
            old_splitting_points = new_splitting_points
            # change size for the next layer
            self.size_scale *= self.scale_change
            self.numbers_of_layers -= 1
        if plot:
            plt.savefig('tree.png')


if __name__ == "__main__":
    parser = ArgumentParser(description="Produce tree strcture")
    parser.add_argument("numbers_of_layers")
    parser.add_argument("scale_change")
    parser.add_argument("spread")
    parser.add_argument("size_scale")
    arguments = parser.parse_args()

    tree = MakeTree(int(arguments.numbers_of_layers),
                    float(arguments.scale_change), float(arguments.spread),
                    float(arguments.size_scale))
    tree.produce_tree()
