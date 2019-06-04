import os
from cliarguments import get_args

def createMetadataFiles(templates):
    outputDir = get_args().output
    createOutputDir(outputDir)
    createMetafiles(outputDir, templates)

def createOutputDir(dirName):
    # Generate the output directory
    if not os.path.exists(dirName):
        os.makedirs(dirName)

def createMetafiles(folder, templates):
    # create as many output files as we have function declarations in R -files
    for template in templates:
        outputFile = str(folder + "\\" + template.title + ".txt")   # Add extensio TODO: Make extension an CLI argument
        f = open(outputFile, "w+")
        f.write( template.generateTemplate() )