#!/usr/bin/python3
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Checks if a list of numbers can be\
    divided to two same-length same-sum lists", epilog='(C) 2019 -- Amr Ayman')

    parser.add_argument(nargs='+', type=int, help='List numbers', dest='numbers')
    options = parser.parse_args()

    if len(options.numbers) % 2 != 0:
        parser.error('The list must have an even number of numbers.')

    return options

if __name__ == '__main__':
    options = parse_args()
    nums = sorted(options.numbers)
    evens = [nums[x] for x in range(0, len(options.numbers), 2)]
    odds = [nums[x] for x in range(1, len(options.numbers), 2)]

    i = 0
    while sum(evens) < sum(odds):
        evens[i], odds[i] = odds[i], evens[i]
        i += 1

    if sum(evens) == sum(odds):
        print('They can be! Here\'s how:\n%s\n%s' % (evens, odds))
    else:
        print('They cannot be!')
