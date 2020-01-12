#Write data to configured output file with formatter.
class Outputter:

    def __init__(self, outFilePath, formatter):
        self.outFilePath = outFilePath
        self.formatter = formatter
    
    def writeOutput(self, data, fnName):
        try:
            outputFile = open(self.outFilePath,'a+')
            data = f"{self.formatter.getHeader(fnName)}\n{data}\n{self.formatter.getFooter()}"
            print (data, file=outputFile)
        except Exception as e:
            print(str(e))
        finally:
            outputFile.close()