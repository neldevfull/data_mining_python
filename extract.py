# coding: utf-8

import os
import zipfile
import sys

def main(path, name):
    try:
        zfile = zipfile.ZipFile(path)
        print("File extracted")
    except (IOError, FileNotFoundError, PermissionError):
        print('There was a problem reading the file')
    else:
        zfile.extractall(name)
        zfile.close()



if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])