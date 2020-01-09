import re
from constants import searchItem
from helper.BFS import BFS


class BSGraph:
    def __init__(self):
        self.ActMov = []
        self.edges = []

    def callFunction(self, fnName, args):
        return getattr(self, fnName)(*args)

    def findActorsRMovies(self, actmov, category):
        scrchItem = category + actmov
        output = ""
        displayMsg1 = "Actor" if category == searchItem.actor.value else "Movie"
        displayMsg2 = "Movies" if category == searchItem.actor.value else "Actors"
        matchText = searchItem.movie.value  if category == searchItem.actor.value else searchItem.actor.value 
        if scrchItem not in self.ActMov:
            return f"{displayMsg1} \"{actmov}\" not found."
        else:
            output = ""
            index = self.ActMov.index(scrchItem)
            searchedItemIndex = list(filter(lambda item: item!=-1, map(lambda tuple: tuple[0] if tuple[1]==1 else -1, enumerate(self.edges[index]))))
            if len(searchedItemIndex)>0:
                for index in searchedItemIndex:
                    output = output + self.ActMov[index].replace(matchText,"") + "\n"
            return f"{displayMsg1} name: {actmov}\nList of {displayMsg2}:\n{output}"
    
    def readActMovfile(self, inputFile):
        try:
            actMovDict = {}
            inputFileData = open(inputFile, 'r')
            for line in inputFileData:
                actmovList = list(
                    map(lambda word: word.strip(), line.split('/')))
                if len(actmovList) > 0:
                    movie = "mov_" + actmovList[0]
                    actors = list(map(lambda item: "act_" + item,
                                      actmovList[1:len(actmovList)]))
                    if movie not in self.ActMov:
                        self.ActMov.append(movie)
                    for actor in actors:
                        if actor not in self.ActMov:
                            self.ActMov.append(actor)
                    actMovDict[movie] = actors
            self.edges = [[0] * len(self.ActMov)
                          for i in range(len(self.ActMov))]
            for movie in actMovDict:
                self.createNodeEdge(movie, actMovDict[movie])
        except Exception as e:
            raise e
        finally:
            inputFileData.close()

    def createNodeEdge(self, movie, actors):
        movIndex = self.ActMov.index(movie)
        for actor in actors:
            actIndex = self.ActMov.index(actor)
            self.edges[movIndex][actIndex] = 1
            self.edges[actIndex][movIndex] = 1

    def displayActMov(self):
        try:
            actMovDict = {
                "movies": {
                    "count": 0,
                    "moviesList": ""
                },
                "actors": {
                    "count": 0,
                    "actorsList": ""
                },
            }
            for item in self.ActMov:
                if(re.search("^mov_", item)):
                    actMovDict["movies"]["count"] = actMovDict["movies"]["count"] + 1
                    actMovDict["movies"]["moviesList"] = actMovDict["movies"]["moviesList"] + \
                        "\n" + item.replace("mov_", "")
                else:
                    actMovDict["actors"]["count"] = actMovDict["actors"]["count"] + 1
                    actMovDict["actors"]["actorsList"] = actMovDict["actors"]["actorsList"] + \
                        "\n" + item.replace("act_", "")
            movCount = actMovDict["movies"]["count"]
            actCount = actMovDict["actors"]["count"]
            movList = actMovDict["movies"]["moviesList"]
            actList = actMovDict["actors"]["actorsList"]

            return f"Total no. of movies: {movCount}\nTotal no. of actors: {actCount}\n\nList of movies:\n{movList}\n\nList of actors:\n{actList}"
        except Exception as e:
            raise e
    
    def displayActorsOfMovie(self, movie):
        return self.findActorsRMovies(movie, searchItem.movie.value)
    
    def displayMoviesOfActor(self, actor):
        return self.findActorsRMovies(actor, searchItem.actor.value)
    
    def findMovieTransRelation(self, movA, movB):
        try:
            bfs = BFS()
            movAIndex = self.ActMov.index("mov_" + movA)
            movBIndex = self.ActMov.index("mov_" + movB)
            pathList = bfs.getPath(self.edges, movAIndex, movBIndex)
            if len(pathList) > 0:
                path = "->".join(map(lambda index: re.sub(searchItem.movie.value + "|" + searchItem.actor.value,"",self.ActMov[index]),pathList))
                return f"Movie A: {movA}\nMovie B: {movB}\nRelated: Yes, {path}"
            else:
                return f"No relation exist between {movA} and {movB}."
        except ValueError:
            return "Any one of the movie may not be present."
        except Exception as e:
            raise e
