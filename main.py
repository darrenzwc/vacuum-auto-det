#!/usr/bin/env python
import sys, argparse, os
import numpy as np
from plot_gen import *

def main():
    parser = argparse.ArgumentParser(description="Input a CHGCAR_SUM file with -f argument and output file name with -o argument unless you already have a data file (.npy)")
    parser.add_argument('-f', dest = 'filename', required= True, help = 'file path')
    parser.add_argument('-o', dest = 'dataname', required = False, help = 'output file name')
    args = parser.parse_args()
    if len(sys.argv) == 5 or len(sys.argv) == 3:
        if sys.argv[1] != '-f':
            print("Incorrect usage. Please use the -f argument followed by the filename.")
            sys.exit(1)
        if len(sys.argv) == 5:
            if(sys.argv[3] != '-o'):
                print("Incorrect usage. Please use the -o argument followed by the output file name.")
                sys.exit(1)
        if not os.path.isfile(args.filename):
            print(f"Error: File '{args.filename}' does not exist.")
            sys.exit(1)
        if len(sys.argv) == 5:
            data = parse(args.filename)
            np.save(args.dataname, data)
            print("data file", args.dataname, "saved.")
        else:
            print("Loading data file...")
            plot(args.filename)
    else:
        print("Please input the correct number of arguments.")
        sys.exit(1)

if __name__ == "__main__":
    main()
