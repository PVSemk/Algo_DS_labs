import argparse
import os


def parse_arguments():
    parser = argparse.ArgumentParser(description='Horse movements')
    parser.add_argument('--infile', default='lab_1.txt', type=str, help='Input file')
    parser.add_argument('--outfile', default='out.txt', type=str, help='Output file')

    args = parser.parse_args()

    if not os.path.isfile(args.infile):
        raise FileNotFoundError('Input file wasn\'t found')

    return args
