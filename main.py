from BSGraph import BSGraph
import json
import sys
from constants import fileConstants, searchOperation
import os


class Program:
    def __init__(self):
        try:
            configJson = open(self.getAbsoluteFilePath("config.json"))
            config = json.load(configJson)
            self.inputFile = self.getAbsoluteFilePath(config["inputFile"])
            self.outputFile = self.getAbsoluteFilePath(config["outputFile"])
            self.promptsFile = self.getAbsoluteFilePath(config["promptsFile"])
            self.formatter = config["formatter"]
            self.bsgraph = BSGraph()
            self.searchFunc = {
                searchOperation.searchActor : "displayActMov",
                searchOperation.searchMovie : "displayActorsOfMovie",
                searchOperation.RMovies: "findMovieRelation",
                searchOperation.TMovies: "findMovieTransRelation"
            }
            self.bsgraph.readActMovfile(self.inputFile)
        except Exception as e:
            self.writeOutput("Exception occured: " + str(e), self.outputFile, ' constructor ')
        finally:
            configJson.close()

    def getAbsoluteFilePath(self, relativeFilePath):
        CWD = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(CWD, relativeFilePath)
        
    
    def run(self):
        try:
            queries = open(self.promptsFile,'r')
            for query in queries:
                commands = list(map(lambda word: word.strip(), query.split(':'))) 
        except Exception as e:
            print("Exception occured:" + str(e))
        finally:
            queries.close()
            sys.exit() 
    
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
program.adjacencyMatrix(program.bsgraph.edges)