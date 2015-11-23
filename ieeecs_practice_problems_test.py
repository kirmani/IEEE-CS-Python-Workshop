#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 sean <sean@wireless-10-146-149-144.public.utexas.edu>
#
# Distributed under terms of the MIT license.
"""TODO(sean): DO NOT SUBMIT without one-line documentation for test

TODO(sean): DO NOT SUBMIT without a detailed description of test.
"""

import argparse
import sys
import time

import ieeecs_practice_problems as prog

def main():
    """TODO(sean): Do something more interesting here..."""
    _test_not_string()
    _test_array_count9()
    _test_without_end()
    _test_common_end()
    _test_love6()
    _test_round_sum()
    _test_count_code()
    _test_centered_average()

def _test_not_string():
    """Tests the not_string method"""
    _test_method(prog.not_string('candy'), 'not candy',
                 "not_string('candy') --> 'not_candy'")
    _test_method(prog.not_string('x'), 'not x',
                 "not_string('x') --> 'not x'")
    _test_method(prog.not_string('not bad'), 'not bad',
                 "not_string('not bad') --> 'not bad'")

def _test_array_count9():
    """Tests the array_count9 method"""
    _test_method(prog.array_count9([1, 2, 9]), 1,
                 "array_count9([1, 2, 9]) --> 1")
    _test_method(prog.array_count9([1, 9, 9]), 2,
                 "array_count9([1, 9, 9]) --> 2")
    _test_method(prog.array_count9([1, 9, 9, 3, 9]), 3,
                 "array_count9([1, 9, 9, 3, 9]) --> 3")

def _test_without_end():
    """Tests the without_end method"""
    _test_method(prog.without_end('Hello'), 'ell',
                 "without_end('Hello') --> 'ell'")
    _test_method(prog.without_end('java'), 'av',
                 "without_end('java') --> 'av'")
    _test_method(prog.without_end('coding'), 'odin',
                 "without_end('coding') --> 'odin'")

def _test_common_end():
    """Tests the common_end method"""
    _test_method(prog.common_end([1, 2, 3], [7, 3]), True,
                 "common_end([1, 2, 3], [7, 3]) --> True")
    _test_method(prog.common_end([1, 2, 3], [7, 3, 2]), False,
                 "common_end([1, 2, 3], [7, 3, 2]) --> False")
    _test_method(prog.common_end([1, 2, 3], [1, 3]), True,
                 "common_end([1, 2, 3], [1, 3]) --> True")

def _test_love6():
    """Tests the love6 method"""
    _test_method(prog.love6(6, 4), True, "love6(6, 4) --> True")
    _test_method(prog.love6(4, 5), False, "love6(4, 5) --> False")
    _test_method(prog.love6(1, 5), True, "love6(1, 5) --> True")

def _test_round_sum():
    """Tests the round_sum method"""
    _test_method(prog.round_sum(16, 17, 18), 60, "round_sum(16, 17, 18) --> 60")
    _test_method(prog.round_sum(12, 13, 14), 30, "round_sum(12, 13, 14) --> 30")
    _test_method(prog.round_sum(6, 4, 4), 10, "round_sum(6, 4, 4) --> 10")

def _test_count_code():
    """Tests the count_code method"""
    _test_method(prog.count_code('aaacodebbb'), 1,
                 "count_code('aaacodebbb') --> 1")
    _test_method(prog.count_code('codexxcode'), 2,
                 "count_code('codexxcode') --> 2")
    _test_method(prog.count_code('cozexxcope'), 2,
                 "count_code('cozexxcope') --> 2")

def _test_centered_average():
    """Tests the centered_average method"""
    _test_method(prog.centered_average([1, 2, 3, 4, 100]), 3,
                 "centered_average([1, 2, 3, 4, 100]) --> 3")
    _test_method(prog.centered_average([1, 1, 5, 5, 10, 8, 7]), 5,
                 "centered_average([1, 1, 5, 5, 10, 8, 7]) --> 5")
    _test_method(prog.centered_average([-10, -4, -2, -4, -2, 0]), -3,
                 "centered_average([-10, -4, -2, -4, -2, 0]) --> -3")

def _test_method(expected, actual, message=""):
    """Prints output for a test"""
    if expected == actual:
        print "Passed Test: %s" % message
    else:
        print "----------"
        print "FAILED TEST: %s" % message
        print "Expected: %s" % expected
        print "Actual: %s" % actual
        print "----------\n"

if __name__ == '__main__':
    try:
        START_TIME = time.time()
        PARSER = argparse.ArgumentParser()
        PARSER.add_argument('-v', '--verbose', action='store_true',
                            default=False, help='verbose output')
        PARSER.add_argument('-d', '--debug', action='store_true',
                            default=False, help='debug output')
        ARGS = PARSER.parse_args()
        # if len(ARGS) < 1:
        #   PARSER.error('missing argument')
        if ARGS.verbose:
            print time.asctime()
        main()
        if ARGS.verbose:
            print time.asctime()
        if ARGS.verbose:
            print 'TOTAL TIME IN MINUTES:'
        if ARGS.verbose:
            print (time.time() - START_TIME) / 60.0
        sys.exit(0)
    except KeyboardInterrupt, error: # Ctrl-C
        raise error
    except SystemExit, error: # sys.exit()
        raise error
