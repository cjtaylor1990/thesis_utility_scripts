import numpy as np
import csv
import sys

def read_csv_to_npy(inputFile, group_by_column=False, delimiter=' '):
    """
    This function was created to read in the common CSV text files
    that other scripts produce as output. The CSV is assumed to be uniform,
    that is each row has the same number of columns.

    Required Variables:
    inputFile = string that contains path to file that will be read

    Optional Variables:
    delimiter = string with character that seperates column in CSV
    group_by_column = if true, this will transpose the input, grouping by column

    Example 1:
    ./inputFile.txt
    0 0 0
    1 1 1

    read_csv_to_npy('./inputFile.txt') => numpy.array([["0", "0", "0"], ["1", "1", "1"]])
    
    read_csv_to_npy('./inputFile.txt', group_by_column=True) => numpy.array([["0", "1"], ["0", "1"], ["0", "1"]])

    """
    data = csv.reader(open(inputFile, 'r'), delimiter=delimiter)
    output = np.array([row for row in data])
    return np.transpose(output) if (group_by_column) else output

def convert_csv_to_npy(inputFile, outputFile, group_by_column=False, delimiter=' '):
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
    np.save(outputFile, read_csv_to_npy(inputFile, group_by_column=group_by_column, delimiter=delimiter))

if __name__=="__main__":
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
    if len(sys.argv) > 3 and sys.argv[3].lower() == "true":
        group_by_column = True
    else:
        group_by_column = False

    convert_csv_to_npy(inputFile, outputFile, group_by_column=group_by_column)

