import sys
from automate_script import automate_script
import csv_to_npy

inputFile = sys.argv[1]
csvList = csv_to_npy.read_csv_to_npy(inputFile)

def convert_file(csv_file):
    npy_file = csv_file[0][:-3] + 'npy'
    csv_to_npy.convert_csv_to_npy(csv_file[0], npy_file)

if __name__ == '__main__':
    inputFile = sys.argv[1]
    automate_script(convert_file, inputFile)