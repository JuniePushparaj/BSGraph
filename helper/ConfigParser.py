import json

class JsonParser:
    def __init__(self, jsonFilePath):
        try:
            configJson = open(jsonFilePath)
            self.config = json.load(configJson)
        except Exception as e:
            print(str(e))
        finally:
            configJson.close()
    
    def getConfig(self, key):
        if key in self.config:
            return self.config[key]
        else:
            raise Exception("key not found in config")

