class FileParser:
    def __init__(self, filePath):
        self.filePath = filePath
    
    def parse(self, callback):
        try:
            inputFileData = open(self.filePath, 'r')
            for line in inputFileData:
                callback(line)
        except Exception as e:
            raise e
        finally:
            inputFileData.close()
        