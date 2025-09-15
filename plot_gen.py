#!/usr/bin/env python
import sys, time
import numpy as np

def skip_lines(f, num_lines):
    for i in range(num_lines):
        f.readline()

def parse(f):
    file_path = f
    data = np.array([])
    num_data = 0
    write_data = False
    t_start = time.time()
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
                        data = np.fromfile(file = f, dtype = np.float64, sep = ' ')
                    except ValueError:
                        print(f"Error in charge density data found on line {index + 1}, skipping line.")
    except Exception as e:
        print(f"Error reading file: {e}")
    t_elapsed = time.time() - t_start
    print(f"Parsing Process Time: {t_elapsed:.3f}") 