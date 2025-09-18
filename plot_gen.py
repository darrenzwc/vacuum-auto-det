#!/usr/bin/env python
import sys, time
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def skip_lines(f, num_lines):
    for i in range(num_lines):
        f.readline()

def parse(f):
    file_path = f
    raw_data = np.array([])
    num_data = 0
    write_data = False
    t_start = time.time()
    try:
        with open(file_path, 'r') as f:
            for index, line in enumerate(f):
                parts = line.strip().split()
                if not write_data and len(parts) == 3 and parts[0].isdigit():
                    num_data = np.pow(int(parts[0]), 3)
                    print("Parsing", num_data, "charge densities")
                    write_data = True
                if write_data:
                    try:
                        raw_data = np.fromfile(file = f, dtype = np.float64, sep = ' ')
                    except ValueError:
                        print(f"Error in charge density data found on line {index + 1}, skipping line.")
    except Exception as e:
        print(f"Error reading file: {e}")
    t_elapsed = time.time() - t_start
    neg_den = (raw_data < 0).sum()
    data = raw_data[raw_data > 0]
    print(f"Parser Processing Time: {t_elapsed:.3f} \nNegative densities removed from data\n{(neg_den / data.size):.2%} of the charge densities are negative ({neg_den})\n")
    print(f"Stats\nFiltered data: {data.size} densities\nMin Density: {np.min(data)}\nMax Density: {np.max(data)}\nMedian: {np.median(data)}\n")
    plot(data)
    return data 

def plot(data):
    d = data
    if isinstance(data, (str, bytes)) and data.endswith(".npy"):
        d = np.load(data)
    sns.histplot(data = d, bins = 1000, log_scale = True)
    plt.xlabel("Electron Density (1/Å³)")
    plt.ylabel("Frequency")
    plt.title("Log-scaled Electron Density Distribution")
    plt.show()
    

    
        
    
    