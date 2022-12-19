import sys
import os
from os.path import isfile, join, isdir
import shutil
import itertools
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

def organizeDirectory(dir_name):
    formats, fileTypes, fileFormats = setFormatFilesToDir()
    names = []
    extensions = []
    destination = ""
    fileLists = [filen for filen in os.listdir(dir_name) if isfile(join(dir_name, filen))]
    print(fileLists)
    
    for file_name in fileLists:
        filebreaker = file_name.split('.')
        filename, formatfile = filebreaker[0], filebreaker[-1]
        for formats in fileFormats:
            if formatfile in formats:
                folderName = fileTypes[fileFormats.index(formats)]
                if isdir(folderName) == True:
                    continue                     
                else:
                    os.mkdir(f'{dir_name}/{folderName}')
                    # destination=f'{dir_name}/{folderName}'
                    # print(file_name + destination)
                    # try:
                    #     shutil.move(file_name, destination)
                    # except:
                    #     continue
if __name__ == '__main__':
    organizeDirectory(dir_name)