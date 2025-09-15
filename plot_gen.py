#!/usr/bin/env python
import sys
import numpy as np

def skip_lines(f, num_lines):
    for i in range(num_lines):
        f.readline()

def parse(f):
    file_path = f
    data = np.array([])
    num_data = 0
    write_data = False
    try:
        with open(file_path, 'r') as f:
            for index, line in enumerate(f):
                parts = line.strip().split()
                if not write_data and len(parts) == 3 and parts[0].isdigit():
                    num_data = np.pow(int(parts[0]), 3)
                    print("Parsing", num_data, "charge densities.")
                    write_data = True
                if write_data:
                    try:
                        if(index % (num_data / 50) == 0):
                            print("Progress:", index, "/", num_data)
                        numbers = [float(part) for part in parts]
                        data = np.append(data, numbers)
                    except ValueError:
                        print(f"Error in charge density data found on line {index + 1}, skipping line.")
    except Exception as e:
        print(f"Error reading file: {e}")
    return data
