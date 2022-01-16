"""
Matt Russell
Ranum and Miller Self Check 1.4.5, p.29
Infinite Monkey Theorem - Simplified Version

Generate random sentences, and then score via comparison to "methinks it is like a weasel" 
Goal is to see how long it takes to produce an exact match
Basic characters are the 26 from the lowercase latin alphabet + blank (whitespace)
"""
import random

def generate(basicCharacters,strngLen):
    # basicCharacters - list from which to build sentence
    # strngLen - how long to make the sentence
    randomString = basicCharacters[random.randint(0,len(basicCharacters)-1)] # create randomString
    for sidx in range(strngLen-1):
        rndInt = random.randint(0,len(basicCharacters)-1)
        randomString = randomString + basicCharacters[rndInt]
    return randomString

def score(randomString,magicString):
    # randomString - string built randomly from the list of basic characters
    # magicString - string that we wish to construct
    if(len(randomString) != len(magicString)):
        raise RuntimeError("Strings are not the same length, and therefore cannot be compared.")
    points = 0.0
    for k in range(len(randomString)):
        if(randomString[k] == magicString[k]):
            points = points + 1.0
    points = points / float(len(randomString))
    return points

def monkeyBusiness(basicCharacters,magicString):
    randomSentence = generate(basicCharacters,len(magicString))
    strScore = score(randomSentence,magicString)
    return strScore, randomSentence

magicString = "methinks it is like a weasel"
basicCharacters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

highScore = 0.0
bestString = ""

nTries = 0

tmpScore, tmpString = monkeyBusiness(basicCharacters,magicString)

while(tmpScore != 1.0):
    nTries += 1
    if(tmpScore > highScore):
        highScore = tmpScore
        bestString = tmpString
    elif(nTries % 1000 == 0):
        print(nTries, "tries have elapsed")
        print("The best string so far is ",bestString,"with a score of",highScore)
    tmpScore, tmpString = monkeyBusiness(basicCharacters,magicString)
    
print("Success after", nTries, "tries!")
