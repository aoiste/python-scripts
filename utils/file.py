import sys
import getopt
import os
from utils import print_to_line


def get_files(path='./'):
    result = []
    if os.path.exists(path):
        for (root, dummy, files) in os.walk(path):
            for file in files:
                result.append(os.path.join(root, file))
    return result


def get_dirs(path='./'):
    result = []
    if os.path.exists(path):
        for (root, dirs, dummy) in os.walk(path):
            for dir_name in dirs:
                result.append(os.path.join(root, dir_name))
    return result


def read_lines(path, count: int):
    file = open(path, "rt", encoding="utf-8")
    return file.readlines(count)


def read_all(path):
    file = open(path, "rt", encoding="utf-16-le")
    return file.read()


def __main__(argv=sys.argv):
    if (len(argv) > 1):
        print_to_line(get_files(argv[1]))
    else:
        print_to_line(get_files())

def check_path(path):
    return os.path.exists(path)


if __name__ == "__main__":
    __main__()
