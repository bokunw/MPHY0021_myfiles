# -*- coding: utf-8 -*-
"""
Wed Nov 21 2018

@author: Bokun Wei

This code contains a class called Laboratory,
with methods that carries out behaviors of the package which is to evaluate
the contents of the shelves after the chemical have reacted and determine
how many reactions have happened base on the rule provided.
"""

import random


class Laboratory(object):

    def __init__(self, shelves):

        """ The constructor for the Laboratory class, setting up the initial
        shelf content in the Laboratory class

        Parameters
        -------
        shelves: dictionary
            content of both lower and upper shelves with the key "lower"
            and "upper"

        """
        # check if input is completely empty
        if shelves is None:
            raise ValueError("Shelves input cannot be empty")
        # check only 2 shelves are in the input
        if len(list(shelves.keys())) != 2:
            raise TypeError("Number of shelves presented should have a \
                                                                  value of 2")
        # check the keys have correct values
        if list(shelves.keys()) != ["lower", "upper"] and \
                list(shelves.keys()) != ["upper", "lower"]:
            raise ValueError("The keys to the shelves \
                                           should be \"upper\" and \"lower\"")
        # obtain contents of the shelves
        self.shelf1 = shelves['lower']
        self.shelf2 = shelves['upper']
        # initialising number of reactions happened between the shelves
        self.num_react = 0

        # if the input shelves are empty in any way, set them as empty shelves
        # which are allowed
        if self.shelf1 is None or None in self.shelf1:
            self.shelf1 = []

        if self.shelf2 is None or None in self.shelf2:
            self.shelf2 = []
        # check if all substances are string
        if not all(isinstance(n, str) for n in self.shelf1) or not \
                all(isinstance(n, str) for n in self.shelf2):
            raise TypeError("The shelves should be array of strings")

        # raise exception is substance name start with antianti
        if any(s for s in self.shelf1 if s.startswith("antianti")) or \
                any(s for s in self.shelf2 if s.startswith("antianti")):
            raise ValueError("The substances cannot start with antianti")

    def can_react(self, substance1, substance2):
        """check if two substances can react or not. They can react if
        X is matched with antiX

        Parameters
        -------
        substance1: str
            one of the substances name from one of the shelf.
        substance2: str
            one of the substances name from the other shelf.

        Returns
        -------
        bool
            whether the two substances can react or not based on the rule
            that X can react with antiX.

        """
        return (substance1 == "anti" + substance2) or \
            (substance2 == "anti" + substance1)

    def update_shelves(self, substance1, substance2_index):

        """update the content of the shelves after a reaction has happened
        by removing the reacted substances from both shelves

        Parameters
        -------

        substance1: str
            The name of the substance from the lower shelf which reacted
            and to be removed
        substance2_index: int
            index of the substance that reacted from the other shelf (upper
            shelf), which will be removed after updating

        Returns
        -------
        str array
            content of the lower shelf after a reaction
        str array
            content of the upper shelf after a reaction

        """
        # get the index of substance 1 in shelf 1
        index1 = self.shelf1.index(substance1)
        # remove substance 1 from shelf 1
        self.shelf1 = self.shelf1[:index1] + self.shelf1[index1+1:]
        # remove substance 2 from shelf 2
        self.shelf2 = self.shelf2[:substance2_index] + \
            self.shelf2[substance2_index+1:]
        return self.shelf1, self.shelf2

    def do_a_reaction(self):

        """Generate updated shelves contents after a reaction
        have happened between those shelves.

        Returns
        -------
        str array
            Content of one of the shelves after a reaction has happened
        str array
            Content of the other shelf after a reaction has happened

        """
        for substance1 in self.shelf1:
            # get possible reactable substances
            possible_targets = [i for i, target in enumerate(self.shelf2) if
                                self.can_react(substance1, target)]
            # if there is no possible targets, return the original
            # shelf contents with no changes
            if not possible_targets:
                continue
            else:
                # react with possible target
                substance2_index = random.choice(possible_targets)
                return self.update_shelves(substance1, substance2_index)
        return self.shelf1, self.shelf2

    def run_full_experiment(self, reactions):

        """Determine final contents of the shelves and the number of reactions
        happened after all the possible reaction has happened between the
        substances in the two shelves

        Parameters
        -------
        reactions: bool
            whether to return number of the reactions only or the final
            contents of the shelves

        Returns
        -------
        int
            Number of reactions happened between the subtances in the two
            shelves
        str dictionary
            Content of the shelves after all reactions have happened,
            with the key "upper" and "lower"

        """
        count = 0
        ended = False
        while not ended:
            shelf1_old = self.shelf1
            shelf2_old = self.shelf2
            self.do_a_reaction()

            if self.shelf1 != shelf1_old:
                count += 1  # update number of reactions happened
            # stop updating shelves if shelves contents dont change after a
            # reaction
            ended = (shelf1_old == self.shelf1) and (shelf2_old == self.shelf2)
        self.num_react = count

        if reactions:
            print(self.num_react)
            return self.num_react
        else:
            print("lower: {}\nupper: {}".format("[%s]" %
                  (', '.join(self.shelf1)), "[%s]" % (', '.join(self.shelf2))))
            return {"lower": self.shelf1, "upper": self.shelf2}
