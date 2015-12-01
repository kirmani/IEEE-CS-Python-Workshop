#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 kirmani <sean@kirmani.io>
#
# Distributed under terms of the MIT license.
"""IEEE Computer Society: Python Workshop Practice Problems

These are some practice problems for the Python workshop hosted by the IEEE
Computer Society at The University of Texas at Austin on November 30th, 2015.

Try out these problems and try to solve them the Python-ic way!
"""

def not_string(string):
    """Given a string, return a new string where "not" has been added to the
    front. However, if the string already begins with "not", return the string
    unchanged.

    not_string('candy') --> 'not candy'
    not_string('x') --> 'not x'
    not_string('not bad') --> 'not bad'
    """
    pass

def array_count9(nums):
    """Given an array of ints, return the number of 9's in the array.

    array_count9([1, 2, 9]) --> 1
    array_count9([1, 9, 9]) --> 2
    array_count9([1, 9, 9, 3, 9]) --> 3
    """
    pass

def without_end(string):
    """Given a string, return a version without the first and last char, so
    "Hello" yields "ell". The string length will be at least 2.

    without_end('Hello') --> 'ell'
    without_end('java') --> 'av'
    without_end('coding') --> 'odin'
    """
    pass

def common_end(list1, list2):
    """Given 2 arrays of ints, list1 and list2, return True if they have the
    same first element or they have the same last element. Both arrays will be
    length 1 or more.

    common_end([1, 2, 3], [7, 3]) --> True
    common_end([1, 2, 3], [7, 3, 2]) --> False
    common_end([1, 2, 3], [1, 3]) --> True
    """
    pass

def love6(num1, num2):
    """The number 6 is a truly great number. Given two int values, num1 and
    num2, return True if either one is 6. Or if their sum or difference is 6.
    Note: the function abs(num) computers the absolute value of a number.

    love6(6, 4) --> True
    love6(4, 5) --> False
    love6(1, 5) --> True
    """
    pass

def round_sum(num1, num2, num3):
    """For this problem, we'll round an int value up to the next multiple of 10
    if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternatively,
    rounds down to a previous multiple 10 if it's rightmost digit is less than
    5, so 12 rounds down to 10. Given 3 ints, num1 num2 num3, returns the sum of
    their rounded values. To avoid code repitition, write a separate helper "def
    round10(num):" and call it 3 times. Write the helper entirely below and at
    the same indent level as round_sum().

    round_sum(16, 17, 18) --> 60
    round_sum(12, 13, 14) --> 30
    round_sum(6, 4, 4) --> 10
    """
    pass

def count_code(string):
    """Return the number of times that the string "code" appears anywhere in the
    given string, except we'll accept any letter for the 'd', so "cope" and
    "cooe" count.

    count_code('aaacodebbb') --> 1
    count_code('codexxcode') --> 2
    count_code('cozexxcope') --> 2
    """
    pass

def centered_average(nums):
    """Return the "centered" average of an array of ints, which we'll say is the
    mean average of the values, except ignoring the largest and smallest value
    in the array. If there are multiple copies of the smallest value, ignore
    just one copy, and likewise for the largest value. Use int division to
    produce the final average. You may assume that the array is length 3 or
    more.

    centered_average([1, 2, 3, 4, 100]) --> 3
    centered_average([1, 1, 5, 5, 10, 8, 7]) --> 5
    centered_average([-10, -4, -2, -4, -2, 0]) --> -3
    """
    pass
