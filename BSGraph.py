class BSGraph:
    def __init__(self):
        self.ActMov = []
        self.edges = []

    def readActMovfile(self, inputFile):
        try:
            inputFileData = open(inputFile, 'r')
            for line in inputFileData:
                actmovList = list(map(lambda word: word.strip(), line.split('/')))
                if len(actmovList) > 0:
                    movie = "mov_" + actmovList[0].strip()
                    for i in range(1, len(actmovList)):
                        self.createNodeEdge(movie, "act_" + actmovList[i].strip())
        except Exception as e: raise e
        finally: inputFileData.close()

    def createNodeEdge(self, movie, actor):
        movIndex = None
        actIndex = None
        if movie not in self.ActMov:
            self.ActMov.append(movie)
            movIndex = len(self.ActMov)-1
        if actor not in self.ActMov:
            self.ActMov.append(actor)
            actIndex = len(self.ActMov)-1
        if (movIndex is not None and actIndex is not None):
            self.edges[movIndex][actIndex] = 1
            self.edges[actIndex][movIndex] = 1
            self.edges[movIndex][movIndex] = 0
            self.edges[actIndex][actIndex] = 0


    
