#!/usr/bin/env python3

import csv
import sys

def main():
    if (len(sys.argv)) < 2:
        print(f"Usage: 1.py [input_file_path]")
        return
    file_path = sys.argv[1].strip()
    print(f"Processing file {file_path}")
    
    valid_count = 0
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            text = row[0].strip()
            blocks = text.split(' ')
            range_block = blocks[0]
            char = blocks[1][0]
            pwd = blocks[2]
            bound_blocks = range_block.split('-')
            lb = int(bound_blocks[0])
            ub = int(bound_blocks[1])
            char_count = 0
            for i in pwd:
                if(char == i):
                    char_count = char_count +1
            if (char_count >= lb and char_count <= ub):
                valid_count = valid_count + 1

    print(f"Valid count: {valid_count}")
    return valid_count


if __name__ == '__main__':
    main()
