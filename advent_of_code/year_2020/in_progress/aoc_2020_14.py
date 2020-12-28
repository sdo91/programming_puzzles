#!/usr/bin/env python3

def addToPath(relPath):
    from os import path
    import sys
    dirOfThisFile = path.dirname(path.realpath(__file__))
    dirToAdd = path.normpath(path.join(dirOfThisFile, relPath))
    if dirToAdd not in sys.path:
        print('adding to path: {}'.format(dirToAdd))
        sys.path.insert(0, dirToAdd)
    else:
        print('already in path: {}'.format(dirToAdd))


addToPath('../../..')

### IMPORTS ###

import time
import traceback
from collections import defaultdict

import aocd

from advent_of_code.util import aoc_util
from advent_of_code.util.aoc_util import AocLogger
from advent_of_code.util.grid_2d import Grid2D

### CONSTANTS ###
TEST_INPUT = [
    """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
    """, """

    """, """

    """
]

TEST_OUTPUT_1 = [
    165,
    0,
    0,
]

TEST_OUTPUT_2 = [
    0,
    0,
    0,
]


class AdventOfCode(object):
    """
    https://adventofcode.com
    """

    def __init__(self):
        print('starting {}'.format(__file__.split('/')[-1]))

        try:
            self.puzzle_input = aocd.data
        except aocd.exceptions.AocdError:
            error_msg = traceback.format_exc()
            print(error_msg)
            self.puzzle_input = 'unable to get input:\n\n{}'.format(error_msg)
        aoc_util.write_input(self.puzzle_input, __file__)

    def run(self):
        start_time = time.time()

        self.run_tests()

        AocLogger.verbose = False

        aoc_util.assert_equal(
            0,
            self.solve_part_1(self.puzzle_input)
        )

        # aoc_util.assert_equal(
        #     0,
        #     self.solve_part_2(self.puzzle_input)
        # )

        elapsed_time = time.time() - start_time
        print('elapsed_time: {:.3f} sec'.format(elapsed_time))

    def run_tests(self):
        AocLogger.verbose = True
        aoc_util.run_tests(self.solve_part_1, TEST_INPUT, TEST_OUTPUT_1)
        # aoc_util.run_tests(self.solve_part_2, TEST_INPUT, TEST_OUTPUT_2)

    def solve_part_1(self, text: str):
        solver = Solver(text)

        part_1_result = solver.p1()

        print('part_1_result: {}\n'.format(part_1_result))
        return part_1_result

    def solve_part_2(self, text: str):
        solver = Solver(text)

        part_2_result = solver.p2()

        print('part_2_result: {}\n'.format(part_2_result))
        return part_2_result


class Solver(object):

    def __init__(self, text: str):
        self.text = text.strip()
        self.lines = aoc_util.lines(text)
        AocLogger.log(str(self))

        self.mask_1 = 0x00
        self.mask_0 = 0x00

        self.memory = {}

    def __repr__(self):
        return '{}:\n{}\n'.format(
            type(self).__name__, self.text)

    def p1(self):
        for line in self.lines:
            if line.startswith('mask'):
                mask = line.split()[-1]
                self.parse_mask(mask)
            elif line.startswith('mem'):
                ptr, value = aoc_util.ints(line)
                value |= self.mask_1
                value &= ~self.mask_0
                self.memory[ptr] = value
            else:
                assert False

        # return sum
        return sum(self.memory.values())

    def parse_mask(self, mask):
        # reset
        self.mask_1 = 0x00
        self.mask_0 = 0x00

        place = 1
        for c in reversed(mask):
            if c != 'X':
                AocLogger.log('{} @ {}'.format(c, place))

            if c == '1':
                self.mask_1 += place
            elif c == '0':
                self.mask_0 += place

            place *= 2

    def p2(self):
        """

        """
        z = 0
        return 2


if __name__ == '__main__':
    instance = AdventOfCode()
    instance.run()
