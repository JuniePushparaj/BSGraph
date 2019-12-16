class BSGraph:
    def __init__(self):
        self.ActMov = [];
        self.edges = [];

    def readActMovfile(self, inputfile):
        inputFileData = open(inputfile,'r');
        for line in inputFileData:
            actmovList = line.split('/');
            if len(actmovList)>0 :
                movie = actmovList[0];
                for i in range(1, len(actmovList)):
                    createNodeEdge(movie,actmovList[i]);
    
    def createNodeEdge(self, movie, actor):
        movIndex = None;
        actIndex = None;
        if movie not in self.ActMov:
            self.ActMov.append(movie);
            movIndex = len(self.ActMov)-1;
        if actor not in self.ActMov:
            self.ActMov.append(actor);
            actIndex = len(self.ActMov)-1;
        
        if (movIndex is not None && actIndex is not None):
            self.edges[movIndex]
