# Json Input Structure
# [
#  {
#     "date":"2016-03-17T13:59:11+0000",
#     "from":{
#        "name":"First Last",
#        "user_id":650669
#      },
#      "message":"message contents"
#     },
#     ...
# ]

# Read through all files in the ./rooms

# Interested on in emoji statistics
# - Also want to keep track of emoji uses per room & user
# - Also also want to know total days and messages per room & user

# Start with total messages per room
# Two dicts holding key -> value of room name -> count and room name -> days

## TODO
# - Graphs
# - Whitelist/blacklist emojis and users
# - Provide input/output dirs as program arg


import json
import os
import re
import time
from collections import defaultdict
from datetime import datetime

INPUT_DIR = "hipchat_export"
OUTPUT_DIR = "output"

OUTPUT_FILENAME = "analysis.json"

def getAllEmojis(s):
    return re.findall(r"\(([A-Za-z0-9]+)\)", s)

# Editing global variables here, ahh
def processInput(s):
    count = 0
    parsedJson = json.loads(s)

    for x in parsedJson:
        if x == []:
            print("Bad input")
            continue
        # if(x is [] or x[u'date'] is None or x[u'from'][u'name'] is None or x[u'message'] is None):
        #     print("Problem with: " + x)
        #     continue
        date = datetime.strptime(x[u'date'], "%Y-%m-%dT%H:%M:%S%z")
        hour = date.hour
        user = x[u'from'][u'name']
        message = x[u'message']

        emojis = getAllEmojis(message)

        for e in emojis:
            emojiCount[e] += 1
            userCount[user] += 1
            hourCount[hour] += 1
            count += 1

    return count

def writeOutAnalyzedValue(userDict, emojiDict, hourDict, totalCount):
    outputDict = dict()
    outputDict["user"] = userDict
    outputDict["emoji"] = emojiDict
    outputDict["hour"] = hourDict
    outputDict["total"] = totalCount

    outFile = open(os.path.join(OUTPUT_DIR, OUTPUT_FILENAME), 'w')
    outFile.write(json.dumps(outputDict))

sampleInput = """[
{
    "date":"2016-03-17T13:59:11+0000",
    "from":{
        "name":"Patrick",
        "user_id":1234
    },
    "message":"@here (test-emoji) (sample-emoji)"
    },
{
    "date":"2016-03-17T14:00:15+0000",
    "from":{
        "name":"Chris",
        "user_id":4567
    },
    "message":"yes? (test-emoji)"
}]"""

userCount = defaultdict(int)
emojiCount = defaultdict(int)
hourCount = defaultdict(int)

totalCount = 0

start_time = time.time()

for root, directories, files in os.walk(INPUT_DIR):
    for file in files:
        if "json" in file:
            f = open(os.path.join(root, file), 'r')
            print("Processing file: " + root + "/" + file)
            totalCount += processInput(f.read())
            f.close()

end_time = time.time()

elapsed_time = end_time - start_time

print("\nElapsed Time: " + str(elapsed_time))

writeOutAnalyzedValue(userDict=userCount, emojiDict=emojiCount, hourDict=hourCount, totalCount=totalCount)