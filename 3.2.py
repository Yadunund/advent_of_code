#!/usr/bin/env python3

import csv
import sys

def get_trees(right, down, motif):
    rows = len(motif)
    cols = len(motif[0])
    trees = 0
    pos = [0,0]
    while (pos[0] < rows):
        for i in range(right):
            if (pos[1] + 1 == cols):
                pos[1] = 0
            else:
                pos[1] = pos[1] +1
            # if (motif[pos[0]][pos[1]] == 1):
            #    trees = trees + 1
        for i in range(down):
            pos[0] = pos[0] + 1
        if pos[0] >= rows:
            break
        if (motif[pos[0]][pos[1]] == 1):
                trees = trees +1
    print(f"[{down}, {right}]:{trees}")
    return trees

def main():
    if (len(sys.argv)) < 2:
        print(f"Usage: 1.py [input_file_path]")
        return
    file_path = sys.argv[1].strip()
    print(f"Processing file {file_path}")
    
    motif = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            text = row[0].strip()
            row_motif = []
            for char in text:
                if char == '.':
                    row_motif.append(0)
                else:
                    row_motif.append(1)
            motif.append(row_motif)

    tree_prod = 1
    tree_prod = tree_prod * get_trees(1,1,motif)
    tree_prod = tree_prod * get_trees(3,1, motif)
    tree_prod = tree_prod * get_trees(5,1,motif)
    tree_prod = tree_prod * get_trees(7,1,motif)
    tree_prod = tree_prod * get_trees(1,2,motif)
    print(f"Prod: {tree_prod}")


if __name__ == '__main__':
    main()
