from BSGraph import BSGraph
import json
import sys
from constants import fileConstants, searchOperation
import os
import helper
config = helper.ConfigParser.JsonParser(getAbsoluteFilePath("config.json"))
formatterConfig = config.getConfig('formatter')
formatter = helper.Formatter.Formatter(formatterConfig.symbol, formatterConfig.count)
outputter = helper.OutPutter.Outputter(getAbsoluteFilePath(config.getConfig("outputFile")))

def getAbsoluteFilePath(self, relativeFilePath):
        CWD = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(CWD, relativeFilePath)


class Program:
    def __init__(self):
        try:
            self.bsgraph = BSGraph()
            self.bsgraph.readActMovfile(config.getConfig("inputFile"))
        except Exception as e:
            outputter.writeOutput("Exception occured: " + str(e), formatter.getFormat("Constructor"))   
    
    def run(self):
        try:
            fnName = ""
            queries = open(self.promptsFile,'r')
            for query in queries:
                commands = list(map(lambda word: word.strip(), query.split(':')))
                if len(commands)>1 :
                    fnName = self.searchFunc[commands[0]]
                    args = commands[1:len(commands)]
                    fnName(*args) 
        except Exception as e:
            self.writeOutput("Exception occured: " + str(e), self.outputFile, f' function {fnName} ')
        finally:
            queries.close()
    
    def writeOutput(self, data, outputFilePath, functionName):
        try:
            formatter = self.formatter
            footer = '\n' + formatter * '-'
            count = int((formatter - len(functionName)+1)/2) 
            header = count * '-' + functionName + count * '-' + '\n'
            data = header + data + footer
            outputFile = open(outputFilePath,'a+')
            print (data, file=outputFile)
        except Exception as e:
            print(str(e))
        finally:
            outputFile.close()
    
    def buildParams(self):
        print("")
    
    def adjacencyMatrix(self, edges):
        for s in edges:
            print(*s)

program = Program()
program.run()