from BSGraph import BSGraph
import json
import sys
import os
from helper.ConfigParser import JsonParser
from helper.Formatter import Formatter
from helper.OutPutter import Outputter

class Program:
    def __init__(self):
        try:
            self.config = JsonParser(self.getAbsoluteFilePath("config.json"))
            formatterConfig = self.config.getConfig('formatter')
            formatter = Formatter(formatterConfig["symbol"], formatterConfig["count"])
            self.outputter = Outputter(self.getAbsoluteFilePath(self.config.getConfig("outputFile")), formatter)
            self.bsgraph = BSGraph()
            self.bsgraph.readActMovfile(self.getAbsoluteFilePath(self.config.getConfig("inputFile")))
        except Exception as e:
            self.outputter.writeOutput("Exception occured: " + str(e), "Constructor")   
    
    def run(self):
        try:
            fnName = ""
            queries = open(self.getAbsoluteFilePath(self.config.getConfig("promptsFile")),'r')
            for query in queries:
                commands = list(map(lambda word: word.strip(), query.split(':')))
                if len(commands)>1 :
                    fnName = self.config.getConfig('searchFunc')[commands[0]]
                    args = commands[1:len(commands)]
                    data = self.bsgraph.callFunction(fnName, args)
                    self.outputter.writeOutput(data, f"function {fnName}")
        except Exception as e:
            self.outputter.writeOutput("Exception occured: " + str(e), f"function {fnName}")
        finally:
            queries.close()
    
    def getAbsoluteFilePath(self, relativeFilePath):
        CWD = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(CWD, relativeFilePath)
    
    def adjacencyMatrix(self, edges):
        for s in edges:
            print(*s)

program = Program()
program.outputter.writeOutput(program.bsgraph.displayActMov(), "function displayActMov")
program.run()