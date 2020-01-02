from BSGraph import BSGraph
import json
import sys
from constants import fileConstants, searchOperation

class Program:
    def __init__(self):
        try:
            configJson = open('config.json','r')
            self.config = json.load(configJson)
            self.bsgraph = BSGraph()
            self.searchFunc = {
                searchOperation.searchActor : "displayActMov",
                searchOperation.searchMovie : "displayActorsOfMovie",
                searchOperation.RMovies: "findMovieRelation",
                searchOperation.TMovies: "findMovieTransRelation"
            }
            self.bsgraph.readActMovfile(self.config.inputFile)
        except Exception as e:
            self.writeOutput(str(e), self.config.outputFilePath, 'constructor')
        finally:
            configJson.close()
    
    def run(self):
        try:
            queries = open(self.config[fileConstants.promtFile],'r')
            for query in queries:
                commands = list(map(lambda word: word.strip(), query.split(':')))

                
        except Exception as e:
            print("Exception occured:" + str(e))
        finally:
            queries.close()
            sys.exit() 
    
    def writeOutput(self, data, outputFilePath, functionName):
        try:
            formatter = self.config.formatter
            footer = '\n' + formatter * '-'
            header = (formatter - len(functionName)+1) * '-' + functionName + (formatter - len(functionName)+1) * '-' + '\n'
            data = header + data + footer
            outputFile = open(outputFilePath,'a+')
            print >> outputFile, data
            print(data)
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