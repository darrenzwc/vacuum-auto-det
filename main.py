#!/usr/bin/env python
import sys, argparse, os
import numpy as np
from plot_gen import *

def main():
    parser = argparse.ArgumentParser(description="Input a CHGCAR_SUM file with -f argument.")
    parser.add_argument('-f', dest='filename', required=True, help='Input file path')
    args = parser.parse_args()

    if len(sys.argv) != 3 or sys.argv[1] != '-f':
        print("Incorrect usage. Please use the -f argument followed by the filename.")
        sys.exit(1)

    if not os.path.isfile(args.filename):
        print(f"Error: File '{args.filename}' does not exist.")
        sys.exit(1)
    data = parse(args.filename)
    np.save('CHGCAR_sum_data', data)
if __name__ == "__main__":
    main()
