import re
from helper.Constants import SearchItem
from helper.Stack import Stack

# Big Screen Graph (BSGraph)
class BSGraph:

    # constructor
    def __init__(self):
        self.ActMov = [] #list for actors and movies
        self.edges = [] # adjacency matrix or connection between movie and actor

    # call BSGraph's function with required argument based on function Name
    def callFunction(self, fnName, args):
        return getattr(self, fnName)(*args)

    # find actors of given movie and vice-versa
    def findActorsRMovies(self, actmov, category):
        scrchItem = category + actmov #adding prefix ac_ or mov_
        output = ""
        displayMsg1 = "Actor" if category == SearchItem.actor.value else "Movie"
        displayMsg2 = "Movies" if category == SearchItem.actor.value else "Actors"
        matchText = SearchItem.movie.value  if category == SearchItem.actor.value else SearchItem.actor.value 
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
    
    # read the input file for big screen graph
    def readActMovfile(self, inputFile):
        try:
            actMovDict = {}
            inputFileData = open(inputFile, 'r')
            for line in inputFileData:
                actmovList = list(
                    map(lambda word: word.strip(), line.split('/'))) # split each line in input file into array.
                if len(actmovList) > 0 and len(actmovList) <= 3: # limit atmost 2 actor for movie
                    movie = "mov_" + actmovList[0] #adding prfeix to differetiate actor and movie
                    actors = list(map(lambda item: "act_" + item,
                                      actmovList[1:len(actmovList)]))
                    if movie not in self.ActMov:
                        self.ActMov.append(movie)
                    for actor in actors:
                        if actor not in self.ActMov:
                            self.ActMov.append(actor)
                    actMovDict[movie] = actors # dictionary to create adjacency matrix
            self.edges = [[0] * len(self.ActMov)
                          for i in range(len(self.ActMov))]
            for movie in actMovDict:
                self.createNodeEdge(movie, actMovDict[movie]) # create adjacency matrix for actors and movies
        except Exception as e:
            raise e
        finally:
            inputFileData.close()
    
    # create adjacency matrix for actors and movies
    def createNodeEdge(self, movie, actors):
        movIndex = self.ActMov.index(movie)
        for actor in actors:
            actIndex = self.ActMov.index(actor)
            self.edges[movIndex][actIndex] = 1
            self.edges[actIndex][movIndex] = 1

    # display all actors and movies
    def displayActMov(self):
        try:
            # using dictionary to differetiate actors and movies and count 
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
    
    # find actors of given movie
    def displayActorsOfMovie(self, movie):
        return self.findActorsRMovies(movie, SearchItem.movie.value)
    
    # find movies of given actor and vice-versa
    def displayMoviesOfActor(self, actor):
        return self.findActorsRMovies(actor, SearchItem.actor.value)
    
    # find relation between two movies using Depth First Search algorithm. Stack is used to trace path.
    def findMovieTransRelation(self, movA, movB):
        try:
            movAIndex = self.ActMov.index("mov_" + movA) 
            movBIndex = self.ActMov.index("mov_" + movB) 
            visitedNodes = [movAIndex]
            pathExists = False # boolean to find path exist.
            stack = Stack() 
            stack.push(movAIndex) # push source
            while(not stack.isempty()): #run until stack is empty.
                currentNode = stack.peek()
                if currentNode == movBIndex: #if current node is destination exit from traversal.
                    pathExists = True
                    break
                #find the find unvisited reachable node.
                adjacentNode = next((index for index,value in enumerate(self.edges[currentNode]) if value ==1 and index not in visitedNodes),None)
                if adjacentNode is not None:
                    visitedNodes.append(adjacentNode) #mark node as visited
                    stack.push(adjacentNode) #addding to stack to visit its reachable unvisited node.
                else:
                    stack.pop() #removing if no path
            if(pathExists):
                path = list(stack.container) # getting stack to know the path.
                path = "->".join(map(lambda  index: re.sub(SearchItem.movie.value + "|" + SearchItem.actor.value,"",self.ActMov[index]), path)) # converting index to text.
                return f"Movie A: {movA}\nMovie B: {movB}\nRelated: Yes, {path}"
            else:
                return f"No relation exist between {movA} and {movB}."
        except ValueError:
            return "Any one of the movie may not be present."
        except Exception as e:
            raise e
    
    # find relation between two movie using Breadth First Search upto level 2. 
    def findMovieRelation(self, movA, movB):
        try:
            movAIndex = self.ActMov.index("mov_" + movA)
            movBIndex = self.ActMov.index("mov_" + movB)
            visitedNodes = [movAIndex]
            pathExists = False # boolean to find path exist.
            relation = None
            currentNode = movAIndex
            adjacentNodes = [index for index, value in enumerate( self.edges[currentNode]) if value == 1 and index not in visitedNodes] # return all possible node from current node. BFS(Level 1).
            visitedNodes.extend(adjacentNodes)
            for node in adjacentNodes:
                childNodes = [index for index, value in enumerate( self.edges[node]) if value == 1 and index not in visitedNodes] # Adjacent nodes of current node adjacent node.  BFS(Level 2).
                if movBIndex in childNodes:
                    relation = node
                    pathExists = True
            if(pathExists):
                relation = re.sub(SearchItem.movie.value + "|" + SearchItem.actor.value,"" ,self.ActMov[relation])
                return f"Movie A: {movA}\nMovie B: {movB}\nRelated: Yes, {relation}"
            else:
                return f"No relation exist between {movA} and {movB}."
        except ValueError:
            return "Any one of the movie may not be present."
        except Exception as e:
            raise e

