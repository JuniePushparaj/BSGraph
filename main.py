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
            self.config = JsonParser(self.getAbsoluteFilePath("config.json")) # config
            formatterConfig = self.config.getConfig('formatter') # out file line formater.
            formatter = Formatter(formatterConfig["symbol"], formatterConfig["count"])
             # write given data to output file with given format.
            self.outputter = Outputter(self.getAbsoluteFilePath(self.config.getConfig("outputFile")), formatter)
            self.bsgraph = BSGraph() # Big Screen Graph
            self.bsgraph.readActMovfile(self.getAbsoluteFilePath(self.config.getConfig("inputFile")))
        except Exception as e:
            self.outputter.writeOutput("Exception occured: " + str(e), "Constructor")   
    
    #absolute path of input files and output file to support different machine.
    def getAbsoluteFilePath(self, relativeFilePath):
        CWD = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(CWD, relativeFilePath)
    
    #read prompt file, run each query and write the output to output file.
    def run(self):
        try:
            fnName = ""
            queries = open(self.getAbsoluteFilePath(self.config.getConfig("promptsFile")),'r')
            for query in queries:
                commands = list(map(lambda word: word.strip(), query.split(':')))
                if len(commands)>1 :
                    if commands[0] in self.config.getConfig('operationAllowed'):
                        fnDetails = self.config.getConfig('searchFunc')[commands[0]]
                        fnName = fnDetails["callingFunc"]
                        args = commands[1:len(commands)]
                        if len(args)== fnDetails["param"]:
                            data = self.bsgraph.callFunction(fnName, args)
                            self.outputter.writeOutput(data, f"function {fnName}")
                        else:
                            self.outputter.writeOutput(f"Query: \"{query}\"\nMessage: More or no arguments.", "Invalid query")
                    else:
                        self.outputter.writeOutput(f"Query: \"{query}\"\nMessage: Invalid operation performed.", "Invalid query")
        except Exception as e:
            self.outputter.writeOutput("Exception occured: " + str(e), f"function {fnName}")
        finally:
            queries.close()
# Running program.
program = Program()
program.outputter.writeOutput(program.bsgraph.displayActMov(), "function displayActMov")
program.run()