# coding: utf-8

import os
import zipfile
import sys

def main(path, name):
    if not os.path.exists(path):
        print("File {} not exist".format(path))
        sys.exit(-1)
    else:
        zfile = zipfile.ZipFile(path)
        zfile.extractall(name)
        print("File extracted")


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])