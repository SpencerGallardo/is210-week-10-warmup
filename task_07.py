#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 10 Warmup """


DATA = {
    2: 13,
    75: 24,
    5: 7,
    10: 23,
    8: 29,
    7: 30,
    2: 3,
    6: 25,
    12: 31,
    1: 27
}


def iter_dict_funky_sum(mydict):
    """Loops dictionary extracting keys and values and summing together.
    Args:
       mydict(dict): A dictionary with an int for both key and value.
    Returns:
        int: Sums all values in dictionary minus key
    Examples:
    >>>>> import task_07
>>> task_07.iter_dict_funky_sum(task_07.DATA)
140166242
    """
    total = 0
    for key, value in mydict.iteritems():
        total += value-key
    return total
