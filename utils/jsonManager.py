import json

class jsonManager:

    def __init__(self):
    	pass

    def readFile(self):
        with open('./Data/AbioticsData.json') as json_data:
            dataFileAbiotics = json.load(json_data)
        return dataFileAbiotics
    
    def saveData(self, data):
        with open('./Data/LogData.json', 'a') as outfile:
            json.dump(data, outfile)
        with open('./Data/AbioticsData.json', 'w') as outfile:
            json.dump(data, outfile)
