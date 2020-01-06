import re
from helper import FileParser;

class BSGraph:
    def __init__(self):
        self.ActMov = []
        self.edges = []

    def readActMovfile(self, inputFilePath):
        try:
            actMovDict = {}
            inputFile = FileParser.FileParser(inputFilePath)
            inputFile.parse() 
            inputFileData = open(inputFile, 'r')
            for line in inputFileData:
                actmovList = list(map(lambda word: word.strip(), line.split('/')))
                if len(actmovList) > 0:
                    movie = "mov_" + actmovList[0]
                    actors = list(map(lambda item: "act_" + item ,actmovList[1:len(actmovList)]))
                    if movie not in self.ActMov:
                        self.ActMov.append(movie)
                    for actor in actors:
                        if actor not in self.ActMov:
                            self.ActMov.append(actor)
                    actMovDict[movie] = actors
            self.edges = [[0] * len(self.ActMov) for i in range(len(self.ActMov))]
            for movie in actMovDict:
                self.createNodeEdge(movie, actMovDict[movie])
        except Exception as e: raise e
        finally: inputFileData.close()

    def createNodeEdge(self, movie, actors):
        movIndex = self.ActMov.index(movie)
        for actor in actors:
            actIndex = self.ActMov.index(actor)
            self.edges[movIndex][actIndex] = 1
            self.edges[actIndex][movIndex] = 1
    
    def displayActMov(self):
        actMovDict = {
            "movies":{
                "count": 0,
                "moviesList": ""
            },
            "actors": {
                "count": 0,
                "actorsList": ""
            },
        }
        for item in self.ActMov:
            if(re.search("^mov_")):
                actMovDict["movies"]["count"] = actMovDict["movies"]["count"] + 1
                actMovDict["movies"]["moviesList"] = actMovDict["movies"]["moviesList"] + "\n" + item.replace("^mov_","")
            else:
                actMovDict["actor"]["count"] = actMovDict["actor"]["count"] + 1
                actMovDict["actor"]["actorList"] = actMovDict["actor"]["actorList"] + "\n" + item.replace("^act_","")

        return f"""
        Total no. of movies: {actMovDict["movies"]["count"]}
        Total no. of actors: { actMovDict["actor"]["count"]}
        List of movies:
        {actMovDict["movies"]["moviesList"]}
        {actMovDict["actor"]["actorList"]}
        """
                


    
