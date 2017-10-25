import json

class jsonManager:

    def __init__(self):
    	pass

    def readFile(self):
        with open('./Data/AbioticsData.json') as json_data:
            dataFileAbiotics = json.load(json_data)
        return dataFileAbiotics
    
    def saveData(self, data, maintainer):
     #   print maintainer
        for z in data:
            for k in data[z]['tags']:
                if k=='unUsed':
                    continue
                maintainer[z][k].append(data[z]['tags'][k]['value'])
        with open('./Data/LogData.json', 'w') as outfile:
            json.dump(maintainer, outfile)
        with open('./Data/AbioticsData.json', 'w') as outfile:
            json.dump(data, outfile)
        return maintainer