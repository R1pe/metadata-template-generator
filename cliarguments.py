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
    args = get_args() # Solve CLI arguments
    path = args.folder + '\\*'  + args.extension
    return glob.glob(path) # Returns a list of files

class FullPaths(argparse.Action):
    """Expand user- and relative-paths"""
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, os.path.abspath(os.path.expanduser(values)))

def is_dir(dirname):
    """Checks if a path is an actual directory"""
    if not os.path.isdir(dirname):
        msg = "{0} is not a directory".format(dirname)
        raise argparse.ArgumentTypeError(msg)
    else:
        return dirname

def get_args():
    """Get CLI arguments and options"""
    parser = argparse.ArgumentParser(description=DESCRIPTION)

    parser.add_argument('folder', help=FOLDER_HELP, action=FullPaths, type=is_dir)
    parser.add_argument('-ext', '--extension', help=EXT_HELP, default=EXT_DEFAULT)
    parser.add_argument('-o', '--output', help=OUTPUT_HELP, default=OUTPUT_DEFAULT)
    return parser.parse_args()