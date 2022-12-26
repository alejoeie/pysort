import sys
import os
from os.path import isfile, join, isdir
import shutil
import json

dir_name = sys.argv[1]


def setFormatFilesToDir():
    with open('supportedFormats.json') as formatFile:
        jsonFile = json.load(formatFile)
    fileTypes = list(jsonFile.keys())
    fileFormats = list(jsonFile.values())
    joinedList = [s for s in list(jsonFile.values())]
    formats = []
    for index, formatList in enumerate(joinedList):
        for formt in formatList:
            formats.append(formt)
    return formats, fileTypes, fileFormats


def organizeDirectory(dir_name: str) -> str:
    """Gets formats from json file, iterate over the directory,
    and moves files.

    @type dir_name: str
    @param dir_name: The directry location you want to sort.
    @returns: None
    """
    formats, fileTypes, fileFormats = setFormatFilesToDir()
    destination = ""
    fileLists = [f for f in os.listdir(dir_name) if isfile(join(dir_name, f))]
    for fname in fileLists:
        filebreaker = fname.split('.')
        formatfile = filebreaker[-1]
        print(formatfile)
        for formats in fileFormats:
            if formatfile in formats:
                folderName = fileTypes[fileFormats.index(formats)]
                destination = f'{dir_name}/{folderName}'
                src_path = dir_name + '/' + fname
                print(isdir(src_path))
                print(src_path)
                if isdir(f'{dir_name}/{folderName}') is True:
                    print("Directory already exists.")
                else:
                    os.mkdir(f'{dir_name}/{folderName}')
                shutil.move(src_path, destination)


if __name__ == '__main__':
    organizeDirectory(dir_name)
