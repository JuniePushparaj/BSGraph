class BSGraph:
    def __init__(self):
        self.ActMov = []
        self.edges = []

    def readActMovfile(self, inputFile):
        try:
            actMovDict = {}
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


    
