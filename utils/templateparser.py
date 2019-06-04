import re
from template import Template

functionDeclarationLinePattern = re.compile(".*\s*<-\s*function\(.*\)") # Regex for the function declaration line
functionNamePattern = re.compile("(.*?)\s*<-\s*function\(.*\)") # Extracting the function names
argumentsPattern = re.compile("function\s*(?:\()(.*)(?:\))") # Extracting the functions arguments from the function line
componentsPattern = re.compile("([a-z]+[0-9|A-Z|_|a-z]*)(?=\s*[,|\n|\r\n]|\s|$)") # Extracts all components except the model coefficients from function agruments

def parseFileAndGenerateTemplate(files):
    templates = list()
    for f in files:
        fp = open(f) # Read the file
        for i, line in enumerate(fp): # Read file line-by-line
            if isFunctionDeclaration(line):
                template = parseLineAndCreateTemplate(line)
                templates.append(template)
        fp.close()
    return templates

def isFunctionDeclaration(line):
    return functionDeclarationLinePattern.match(line)

def parseLineAndCreateTemplate(line):
    title = parseTitle(line)
    components = parseComponents(line)
    return Template(title, components)

def parseTitle(line):
    """ Extract the function name from the line """
    return functionNamePattern.match(line).group(1)
    # return line.split(" ")[0] # Parse line to the first " "

def parseComponents(line):
    # Extract the components from the arguments
    argsStr = argumentsPattern.search(line).group(1)
    components = componentsPattern.findall(argsStr)
    return components
