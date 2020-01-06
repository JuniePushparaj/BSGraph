import enum

class fileConstants(enum.Enum):
    inputFile = 'inputFile'
    promtFile = 'promptsFile'
    outputFile = 'outputFile'

class searchOperation(enum.Enum):
    searchActor = 'searchActor'
    searchMovie = 'searchMovie'
    RMovies = 'RMovies'
    TMovies = 'TMovies'
    