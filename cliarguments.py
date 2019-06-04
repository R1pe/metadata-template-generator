import os
import glob
import argparse

DESCRIPTION = 'Generate metadata files from existing R-function files'
FOLDER_HELP = 'The folder containing R-files'
EXT_DEFAULT = '.R'
EXT_HELP = 'The extensions of the input files (default is .R)'
OUTPUT_DEFAULT = 'FHK'
OUTPUT_HELP = 'Name of the output directory'

def getFiles():
    args = getCLIArgs() # Solve CLI arguments
    path = args.folder + '\\*'  + args.extension
    return glob.glob(path) # Returns a list of files

def getCLIArgs():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('folder', help=FOLDER_HELP, type=isDirectory)
    parser.add_argument('-ext', '--extension', help=EXT_HELP, default=EXT_DEFAULT)
    parser.add_argument('-o', '--output', help=OUTPUT_HELP, default=OUTPUT_DEFAULT)
    return parser.parse_args()

def isDirectory(dirname):
    if not os.path.isdir(dirname):
        message = dirname + ' is not a directory'
        raise argparse.ArgumentTypeError(message)
    else:
        return dirname