import json
import os

OUTPUT_DIR = "output"

OUTPUT_FILENAME = "analysis.json"

def printSortedValue(d):
    numberToOuput = 24
    for x in sorted(d, key=d.get, reverse=True):
        print(x, d[x])
        numberToOuput -= 1
        if(numberToOuput <= 0):
            break

dataFile = open(os.path.join(OUTPUT_DIR, OUTPUT_FILENAME), 'r')

jsonData = json.loads(dataFile.read())

usersDict = jsonData["user"]
emojiDict = jsonData["emoji"]
hourDict = jsonData["hour"]

print("\nUsers:")
printSortedValue(usersDict)
print("\nEmojis:")
printSortedValue(emojiDict)
print("\nHours:")
printSortedValue(hourDict)
print("\nTotal:")
print(jsonData["total"])