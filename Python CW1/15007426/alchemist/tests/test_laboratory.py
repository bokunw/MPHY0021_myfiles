# -*- coding: utf-8 -*-
"""
Fri Nov 30 2018

@author: Bokun Wei

This file contains the test code for the alchemist package. It tests if various
exceptions are raised under certain conditions and test various test cases.
"""
from pytest import raises
from ..laboratory import Laboratory
import yaml
import os


# get the content in the yaml file
with open(os.path.join(os.path.dirname(__file__),
                       'fixtures.yml')) as fixtures_file:
    test_content = yaml.load(fixtures_file)


def test_empty_input():
    """ Check if the input is completely empty """
    with raises(ValueError) as exception:
        Laboratory(test_content["test_empty_input"])


def test_two_shelves_entered():
    """ Check if there are only two shelves as input """
    for i in test_content["test_two_shelves_entered"]:
        with raises(TypeError) as exception:
            Laboratory(i)


def test_string_in_shelves():
    """check if all the elements in the shelves are string"""
    for i in test_content["test_string_in_shelves"]:
        with raises(TypeError) as exception:
            Laboratory(i)


def test_antianti_substances():
    """check if the substances in the shelves start with antianti"""
    for i in test_content["test_antianti_substances"]:
        with raises(ValueError) as exception:
            Laboratory(i)


def test_shelves_key():
    """check if the shelves have keys upper and lower"""
    for i in test_content["test_shelves_key"]:
        with raises(ValueError) as exception:
            Laboratory(i)


def test_common_cases():
    """test the obvious cases where the substances in the two shelves react
    with each other"""
    for i in test_content["test_common_cases"]:
        answer = i.pop("answer")
        lab = Laboratory(i)
        assert lab.run_full_experiment(False) == answer


def test_empty_shelves():
    """test that the empty shelves case is allowed and will return empty
    shelves"""
    for i in test_content["test_empty_shelves"]:
        answer = i.pop("answer")
        lab = Laboratory(i)
        assert lab.run_full_experiment(False) == answer


def test_num_reactions():
    """test if the experiment return correct number of reactions if the
    --reactions flag is included"""
    for i in test_content["test_num_reactions"]:
        answer = i.pop("answer")
        lab = Laboratory(i)
        assert lab.run_full_experiment(True) == answer


def test_random_selection():
    """test that if there are multiple targets in the upper shelves where
    it can react with one substance in the lower shelf, the selection is
    random and the returned result is one of the possible answers where
    any of the targets in upper shelf is reacted"""
    for i in test_content["test_random_selection"]:
        lower = i["lower"]
        upper = i["upper"]
        # get the target in upper shelf that can be reacted
        if "anti" in lower[0]:
            lower_sol = lower[0].split("anti")
            lower_sol = lower_sol[1]
        else:
            lower_sol = "anti" + lower[0]
        poss_outcomes = []
        index = 0
        # obtain the possible outcomes where one of the target substances
        # in upper shelf is reacted
        for j in upper:
            if j == lower_sol:
                # remove one of the target substances from upper shelf
                poped = upper.pop(index)
                # add this reacted upper shelf to list of possible outcomes
                poss_outcomes.extend(upper)
                # put the target back in for next target to be removed
                upper.insert(index, poped)
            index += 1
        # get an array of the possible outcomes
        upper_options = []
        while poss_outcomes != []:
            upper_options.append(poss_outcomes[:len(upper)-1])
            poss_outcomes = poss_outcomes[len(upper)-1:]

        lab = Laboratory(i)
        assert lab.run_full_experiment(False)["upper"] in upper_options


def test_can_react():
    """test the can_react method in the Laboratory class, which decide
    if 2 substances can react or not"""
    lab = Laboratory({"lower": [], "upper": []})
    for i in test_content["test_can_react"]:
        answer = i.pop("answer")
        assert lab.can_react(i["substance1"], i["substance2"]) == answer


def test_update_shelves():
    """test the update_shelves method in the Laboratory class, which
    update the shelves knowing which substances are reacted"""
    content = test_content["test_update_shelves"]
    answer_lower = content.pop("answer_lower")
    answer_upper = content.pop("answer_upper")
    lab = Laboratory(content)
    assert lab.update_shelves("antipotionx", 0) == (answer_lower, answer_upper)


def test_do_a_reaction():
    """test do_a_reaction method in the Laboratory class, which update the
    shelves after one set of reaction has occured"""
    for i in test_content["test_do_a_reaction"]:
        answer = i.pop("answer")
        lab = Laboratory(i)
        assert lab.do_a_reaction() == (answer["lower"], answer["upper"])
