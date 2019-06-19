# This Python file uses the following encoding: utf-8
import glob
import os
from cliarguments import solveCLIargs
from utils.templateparser import parseFileAndGenerateTemplate
from template import OutputHolder 

argsCLI = solveCLIargs()
outputData = OutputHolder() # Everything that is necessary will be stored in this object

def main():
    files = getFiles()
    outputData.templatesList = parseFileAndGenerateTemplate(files)
    createMetadataFiles()

def getFiles():
    path = argsCLI.folder + '\\*'  + argsCLI.extension
    listOfFiles = glob.glob(path) 
    return listOfFiles

def createMetadataFiles():
    outputData.outputDir = generateOutputDir()
    generateMetadataTemplateFilesIntoDir()

def generateOutputDir():
    '''create output filder based on CLI arguments'''
    if not os.path.exists(argsCLI.output):
        os.makedirs(argsCLI.output)
    return argsCLI.output

def generateMetadataTemplateFilesIntoDir():
    '''create as many output files as we have function declarations in R -files'''
    for template in outputData.templatesList:
        outputFile = str(outputData.outputDir + "\\" + template.title + ".txt")
        f = open(outputFile, "w+")
        f.write( template.generateTemplate() )    

if __name__ ==  "__main__":
    main()
    