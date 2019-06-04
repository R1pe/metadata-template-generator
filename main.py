# This Python file uses the following encoding: utf-8
import glob
import os
import re
from cliarguments import get_args
from template_utils import parseFileAndGenerateTemplate

def getFiles():
    args = get_args() # Solve CLI arguments
    path = args.folder + '\\*'  + args.extension
    return glob.glob(path) # Returns a list of files

def createMetadataFiles(templates):
    # Generate the output directory
    outputDir = get_args().output
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    # create as many output files as we have function declarations in R -files
    for template in templates:
        outputFile = str(outputDir + "\\" + template.title + ".txt")   # Liitä extensio
        f = open(outputFile, "w+")
        f.write( template.generateTemplate() )

def main():
    files = getFiles()
    metaTemplates = parseFileAndGenerateTemplate(files)
    createMetadataFiles(metaTemplates)

if __name__ ==  "__main__":
    main()
    