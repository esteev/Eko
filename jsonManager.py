import json

class jsonManager:

    def __init__(self):
    	pass

    def readFile(self):
        with open('AbioticsData.json') as json_data:
            dataFileAbiotics = json.load(json_data)
        return dataFileAbiotics
    
    def saveData(self, data):
        with open('LogData.json', 'a') as outfile:
            json.dump(data, outfile)
        with open('AbioticsData.json', 'w') as outfile:
            json.dump(data, outfile)
