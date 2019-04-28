# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 2018

@author: Bokun Wei

This is a command.py file specifying what the command interface will return
after typing in abracadabra. It uses the input arguments yml file name
and the --reaction flag to run the alchemist experiment implementing the
Laboratory class.
"""
import yaml
from argparse import ArgumentParser
from .laboratory import Laboratory


def abracadabra():
    parser = ArgumentParser(description="Determine shelves contents/number \
                               of reactions after substances have reacted")

    # get the arguments and decide to output numbers of reactions or
    # shelves content
    parser.add_argument('--reactions', action="store_true")
    parser.add_argument('yml_file_name')

    arguments = parser.parse_args()
    # get the content in the yaml file
    shelves_before = yaml.load(open(arguments.yml_file_name))

    lab = Laboratory(shelves_before)
    # run the experiment based on arguments parsed in
    lab.run_full_experiment(arguments.reactions)


if __name__ == "__main__":
    abracadabra()
