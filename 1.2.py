#!/usr/bin/env python3

import csv
import sys

def main():
    if (len(sys.argv)) < 2:
        print(f"Usage: 1.py [input_file_path]")
        return
    file_path = sys.argv[1].strip()
    print(f"Processing file {file_path}")
    numbers = []
    
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            numbers.append(int(row[0].strip()))  

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            for k in range(len(numbers)):
                if (i != j and i!=k and j!=k):
                    sum = numbers[i]+numbers[j]+numbers[k]
                    if(sum == 2020):
                        prod=numbers[i]*numbers[j]*numbers[k]
                        print(f"The winning numbers are [{numbers[i]},{numbers[j]},{numbers[k]}] with prod: {prod}")
                        return prod


if __name__ == '__main__':
    main()
