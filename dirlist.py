import os
from collections import namedtuple
import csv
import sys


def make_serch(path, method, value):
    """
    Exports data file for the requested search.

    :param path: The path which we will begin to search
    :param method: method search
    :param value: Search value

    """
    list_op = {"substring": False, "exrension": False, "folders_that_start_with": False, "folders_that_end_with": False}
    try:
        if method in list_op:
            list_op[method] = True
    except:
        print("error")
        exit()

    filetuple = namedtuple('file_details', ['FolderPath', 'FileName', 'CreationDate', 'ModifiedDate', 'DateAccessed'])
    headerList = ['FolderPath', 'FileName', 'CreationDate', 'ModifiedDate', 'DateAccessed']

    with open("listDir.csv", 'w') as f:
        dw = csv.DictWriter(f, delimiter=',', fieldnames=headerList)
        dw.writeheader()
        writer = csv.writer(f)

        for (root, dirs, files) in os.walk(path, topdown=True):
            if list_op["substring"] == True:
                for file in files:
                    if value in file:
                        writer.writerow(filetuple(FolderPath=root, FileName=file,
                                                  CreationDate=os.stat(f'{root}\\{file}').st_atime,
                                                  ModifiedDate=os.path.getmtime(f'{root}\\{file}'),
                                                  DateAccessed=os.path.getatime(f'{root}\\{file}')))

            if list_op["exrension"] == True:
                for file in files:
                    suffix = file[file.rfind("."):]
                    if value == suffix:
                        writer.writerow(filetuple(FolderPath=root, FileName=file,
                                                  CreationDate=os.stat(f'{root}\\{file}').st_atime,
                                                  ModifiedDate=os.path.getmtime(f'{root}\\{file}'),
                                                  DateAccessed=os.path.getatime(f'{root}\\{file}')))
            if list_op["folders_that_start_with"] == True:
                for directory in dirs:
                    if directory.startswith(value):
                        for file in files:
                            writer.writerow(filetuple(FolderPath=root + "\\" + directory, FileName=file,
                                                      CreationDate=os.stat(f'{root}\\{file}').st_atime,
                                                      ModifiedDate=os.path.getmtime(f'{root}\\{file}'),
                                                      DateAccessed=os.path.getatime(f'{root}\\{file}')))

            if list_op["folders_that_end_with"] == True:
                for directory in dirs:
                    if directory.endswith(value):
                        print(directory)
                        print(root)
                        for file in files:
                            writer.writerow(filetuple(FolderPath=root + "\\" + directory, FileName=file,
                                                      CreationDate=os.stat(f'{root}\\{file}').st_atime,
                                                      ModifiedDate=os.path.getmtime(f'{root}\\{file}'),
                                                      DateAccessed=os.path.getatime(f'{root}\\{file}')))


def main():
    make_serch(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == '__main__':
    main()
