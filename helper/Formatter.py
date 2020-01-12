# Line formatter of outputter. Draw header and footer with given symbol and count.
class Formatter:
    def __init__(self, symbol, count):
        self.symbol = symbol
        self.count = int(count)
    
    def getHeader(self, fnName):
        headSymCount = int((self.count - (len(fnName)+2))/2)
        return headSymCount * self.symbol + ' ' + fnName + ' ' + headSymCount * self.symbol
    
    def getFooter(self):
        return self.count * self.symbol
    
    def getFormat(self, fnName):
        return {
            "header": self.getHeader(fnName),
            "footer": self.getFooter()
        }
    