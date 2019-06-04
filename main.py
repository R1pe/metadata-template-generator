# This Python file uses the following encoding: utf-8
import re
from cliarguments import getFiles
from utils.templateparser import parseFileAndGenerateTemplate
from utils.filehandler import createMetadataFiles

def main():
    files = getFiles()
    metaTemplates = parseFileAndGenerateTemplate(files)
    createMetadataFiles(metaTemplates)

if __name__ ==  "__main__":
    main()
    