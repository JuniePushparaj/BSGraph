class Outputter:

    def __init__(self, outFilePath):
        self.outFilePath = outFilePath
    
    def writeOutput(self, data, formatter):
        try:
            outputFile = open(self.outFilePath,'a+')
            if formatter:
                data = f"""
                {formatter.header}
                {data}
                {formatter.footer}
                """
                print (data, file=outputFile)
        except Exception as e:
            print(str(e))
        finally:
            outputFile.close()