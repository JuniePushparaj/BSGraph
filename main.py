from BSGraph import BSGraph
import json
import sys
from constants import fileConstants

class Main:
    def __init__(self,config):
        try:
            configJson = open('config.json','r')
            self.config = json.load(configJson)
        except Exception as e:
            print("Exception occured:" + str(e))
        finally:
            config.close()
            sys.exit()
    
    def run(self):
        try:
            queries = open(self.config[fileConstants.promtFile],'r')
            for query in queries:
                query = query.strip()
        except Exception as e:
            print("Exception occured:" + str(e))
        finally:
            queries.close()
            sys.exit() 
            
    



bsgraph = BSGraph()
bsgraph.readActMovfile(r".\InputFiles\inputPS2.txt")