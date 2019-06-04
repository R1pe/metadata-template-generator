# This Python file uses the following encoding: utf-8
import glob
import os
import re
from cliarguments import get_args
from template import Template


outputDir = "fhk" # Output directory
templates = list()
patrnFuncLine = re.compile(".*\s*<-\s*function\(.*\)") # Regex for the function declaration line
patrnFuncName = re.compile("(.*?)\s*<-\s*function\(.*\)") # Extracting the function names
patrnFuncArgs = re.compile("function\s*(?:\()(.*)(?:\))") # Extracting the functions arguments from the function line
patrnFuncVars = re.compile("([a-z]+[0-9|A-Z|_|a-z]*)(?=\s*[,|\n|\r\n]|\s|$)") # Extracts all components except the model coefficients from function agruments

def getFiles():
    args = get_args() # Solve CLI arguments
    path = args.alignments + '\\*'  + args.extension
    return glob.glob(path) # Returns a list of files

def parseFunctionNames(files):
    for f in files:
        fp = open(f) # Read the file
        for i, line in enumerate(fp): # Read file line-by-line
            if patrnFuncLine.match(line):
                # Extract the file name from the line
                parsedLine = line.split(" ")[0] # Parse line to the first " "
                # Extract the components from the arguments
                strFuncArgs = patrnFuncArgs.search(line).group(1)
                funcArgs = patrnFuncVars.findall(strFuncArgs)
                templates.append( Template(parsedLine, funcArgs) )
        fp.close()

def createMetadataFiles():
    # Generate the output directory
    if not os.path.exists(outputDir):
        os.makedirs(OutputDir)
    # create N number of files based len(fileNames)
    for template in templates:
        outputFile = str(outputDir + "\\" + template.title + ".txt")   # Liitä extensio
        f = open(outputFile, "w+")
        f.write( template.generateTemplate() )

def main():
    files = getFiles()
    metaFileNames = parseFunctionNames(files)
    # createTemplate()
    createMetadataFiles()

if __name__ ==  "__main__":
    main()
    