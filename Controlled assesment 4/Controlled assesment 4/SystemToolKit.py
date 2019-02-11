import sys, os, json

class SystemToolKit:
    @staticmethod
    def readFile(FileName):
        Data = ""
        try:
            with open(FileName, 'r') as fp:
                    Data = json.load(fp)
                    return Data

        except:ValueError,IOError
        data = {}
        with open(FileName,"w+") as fp:
                    json.dump(data,fp)
        return Data

