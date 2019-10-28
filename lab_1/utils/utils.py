import argparse
import os


def parse_arguments():
    parser = argparse.ArgumentParser(description='Horse movements')
    parser.add_argument('--indir', default='in.txt', type=str, help='Input file')
    parser.add_argument('--outdir', default='out.txt', type=str, help='Output file')

    args = parser.parse_args()

    if not os.path.isfile(args.indir):
        raise FileNotFoundError('Input file wasn\'t found')

    return args