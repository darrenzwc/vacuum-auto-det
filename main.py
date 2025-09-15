#!/usr/bin/env python
import sys, argparse, os
import numpy as np
from plot_gen import *

def main():
    parser = argparse.ArgumentParser(description="Input a CHGCAR_SUM file with -f argument and output file name with -o argument.")
    parser.add_argument('-f', dest = 'filename', required= True, help = 'Input file path')
    parser.add_argument('-o', dest ='dataname', required = True, help = 'Input output file name')
    args = parser.parse_args()
    if len(sys.argv) != 5:
        print("Please input the correct number of arguments.")
    if(sys.argv[1] != '-f'):
            print("Incorrect usage. Please use the -f argument followed by the filename.")
            sys.exit(1)
    if(sys.argv[3] != '-o'):
            print("Incorrect usage. Please use the -f argument followed by the filename.")
            sys.exit(1)

    if not os.path.isfile(args.filename):
        print(f"Error: File '{args.filename}' does not exist.")
        sys.exit(1)
    data = parse(args.filename)
    np.save(args.dataname, data)
    print("data file", args.dataname, "saved.")

if __name__ == "__main__":
    main()
