#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description="Draw a board.")
parser.add_argument('row', type=int, help='Number of rows')
parser.add_argument('col', type=int, help='Number of columns')
parser.add_argument('start', type=int, help='Start of number sequence labeling')

args = parser.parse_args()
board_row = args.row
board_column = args.col
board_start = 2

for i in range(board_row):
    row = "{:d}| ".format(args.start + i)
    for index, j in enumerate(range(board_column)):
       row += "|"
       if index != board_column - 1: 
           row += "_"
    print(row)
