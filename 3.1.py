#!/usr/bin/env python3

import csv
import sys

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
    rows = len(motif)
    cols = len(motif[0])
    print(f"Motif with {rows} rows and {cols} cols")
    trees = 0
    pos = [0,0]
    while (pos[0] < rows):
        for i in range(3):
            if (pos[1] + 1 == cols):
                pos[1] = 0
            else:
                pos[1] = pos[1] +1
            # if (motif[pos[0]][pos[1]] == 1):
            #    trees = trees + 1
        pos[0] = pos[0] +1
        if pos[0] == rows:
            break
        if (motif[pos[0]][pos[1]] == 1):
                trees = trees +1
    print(f"Trees: {trees}")


if __name__ == '__main__':
    main()
