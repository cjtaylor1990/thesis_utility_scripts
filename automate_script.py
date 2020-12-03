import os
import sys
from csv_to_npy import read_csv_to_npy

def automate_script(function_to_automate, inputFile, group_by_column=False):
    data = read_csv_to_npy(inputFile, group_by_column=group_by_column)

    for entry in data:
        function_to_automate(entry)

if __name__ == '__main__':
    pythonScript = str(sys.argv[1])
    inputFile = str(sys.argv[2])
    if len(sys.argv) > 3 and sys.argv[3].lower() == 'true':
        group_by_column = True
    else:
        group_by_column = False
    automate_script(lambda x: os.system('python3 ' + pythonScript + ' ' + str(x)), inputFile, group_by_column=group_by_column)