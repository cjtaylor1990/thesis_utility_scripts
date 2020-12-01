import numpy as np
import csv
import sys

def read_txt_to_npy(inputFile, delimiter=' '):
    """
    This function was created to read in CSV .txt files. It
    assumes that all rows in the file have the same number of
    columns. The output is a numpy array that is grouped by
    column.

    Required Variables:
    inputFile = string that contains path to file that will be read
    
    Optional Variables:
    delimiter = string with character that seperates column in CSV

    Example:
    ./inputFile.txt
    0 0 0
    1 1 1

    convert_txt_to_npy('./inputFile.txt')
    => numpy.array([0, 1], [0, 1], [0, 1])
    """
    data = csv.reader(open(inputFile, 'r'), delimiter=delimiter)

    output = np.array([row for row in data])
    output = np.transpose(output)

    return output

def convert_txt_to_npy(inputFile, outputFile, delimiter=' '):
    """
    This function was created to smoothly convert CSV .txt files that
    are the outputs of other scripts and convert them to easily manipulated
    .npy files. The CSV assumes that the data is uniform, as in each row
    has the same number of columns.

    Required Variables:
    inputFile = string that contains path to file that will be read
    outputFile = string that contains path to the file that will be written

    Optional Variables:
    delimiter = string with character that seperates column in CSV

    Example:
    ./inputFile.txt
    0 0 0
    1 1 1

    convert_txt_to_npy('./inputFile.txt', './outputFile.npy')

    ./outputFile.npy
    numpy.array([0, 1], [0, 1], [0, 1])
    """
    np.save(outputFile, read_txt_to_npy(inputFile))


if __name__=="__main__":
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]

    convert_txt_to_npy(inputFile, outputFile)

