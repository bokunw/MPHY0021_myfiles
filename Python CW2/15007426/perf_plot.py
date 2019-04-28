# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 2019

@author: Bokun Wei
"""
from tree_np import MakeTreeNP
from tree import MakeTree
from matplotlib import pyplot as plt
import time


def time_tree(tree_obj):
    """determine the time taken to produce the tree

        Parameters
        -------
        tree_obj: object
            the tree object imported to produce the tree

        Returns
        -------
        double
            the time taken to produce a tree
        """

    start = time.time()
    tree_obj.produce_tree(False)  # produce the tree
    end = time.time()
    return end - start  # return the duration of producing the tree


def compare_performance(ieration_num, iteration_num_np):
    """compare the performance of the original append solution and the
    numpy solution to produce the tree

        Parameters
        -------
        ieration_num: int
            number of iteration to perform on the append solution
        iteration_num_np: int
            number of iteration to perform on the numpy solution

        """
    time_taken = []
    time_taken_np = []
    # calculate iteration times for append solution
    for i in range(ieration_num):
        tree = MakeTree(i, 0.6, 0.1, 1.0)
        time_taken.append(time_tree(tree))
    # calculate iteration times for numpy solution
    for i in range(iteration_num_np):
        tree_np = MakeTreeNP(i, 0.6, 0.1, 1.0)
        time_taken_np.append(time_tree(tree_np))
    # produce performance comparison plot
    plt.plot(time_taken, label='without use of numpy')
    plt.plot(time_taken_np, label='with use of numpy')
    plt.xlabel('Number of iterations')
    plt.ylabel('Time taken to plot the tree (seconds)')
    plt.title('Time to produce tree versus numbers of iteration steps')
    plt.legend(loc='upper left')
    plt.savefig('perf_plot.png')


if __name__ == "__main__":
    ieration_num = 21
    iteration_num_np = 25
    compare_performance(ieration_num, iteration_num_np)
