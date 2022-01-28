"""
Matt Russell
Ranum and Miller "Problem Solving with Data Structures and Algorithms"
Self Check Challenge 1.4.5, p.29 - 30
Infinite Monkey Theorem - Simplified Version
Hill Climbing Extension

Objective:
Generate random sentences, and then score via comparison to "methinks it is like a weasel" 
Goal is to see how long it takes to produce an exact match
Basic characters are the 26 from the lowercase latin alphabet + blank (whitespace)

Hill-Climbing:
Use the current best string to generate new sentences, keeping the letters that are correct, 
and only modifying one character in the best string so far.

# I think there is a logic error somewhere
# Need to write unit tests
"""
import random

def generate_hc(basicCharacters,bestString,correctLetters):
    # Strictly speaking, I don't think this is hill-climbing as the book describes,
    # because it modifies more than one character at a time.
    """ Function """
    # Constructs a candidate string according to hill-climbing principles
    """ Inputs """
    # basicCharacters - list of characters from which sentence is constructed
    # bestString - the current highest-scoring string
    # correctLetters - list containing indices corresponding to the correct letters in bestString
    candidateString = [None] * len(bestString)
    for sidx in range(len(candidateString)):
        if(sidx in correctLetters):
            candidateString[sidx] = bestString[sidx]
        else:
            rndInt = random.randint(0,len(basicCharacters)-1)
            candidateString[sidx] = basicCharacters[rndInt]
    return candidateString
def generate_rand(basicCharacters,strngLen):
    """ Function """
    # Randomly construct a candidate string out of the basic character set (really a list)
    """ Inputs """
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

def score_hc(candidateString,magicString):
    """ Function """
    # Scores candidateString against magicString and returns grade, as well as list of correct indices
    """ Inputs """
    # candidateString - string constructed from 'hill-climbing' routine
    # magicString - string that we wish to construct
    """ Outputs """
    # points - grade assigned to candidateStrong based on how closely it matches magicString
    # correctLetters - list of correct indices
    if(len(candidateString) != len(magicString)):
        raise RuntimeError("Strings are not the same length, and therefore cannot be compared.")
    points = 0.0
    correctLetters = []
    for k in range(len(candidateString)):
        if(candidateString[k] == magicString[k]):
            points = points + 1.0
            correctLetters.append(k)
    points = points / float(len(candidateString))
    return points, correctLetters
    

def monkeyBusiness(basicCharacters,magicString):
    # The initial monkeying around
    randomSentence = generate_rand(basicCharacters,len(magicString))
    strScore = score(randomSentence,magicString)
    return strScore, randomSentence

def monkeyBusiness_hc(basicCharacters,bestString,magicString):
    #
    strScore, correctLetters = score_hc(bestString,magicString)
    newBestString = generate_hc(basicCharacters,bestString,correctLetters)
    return strScore, newBestString
    

magicString = "methinks it is like a weasel"
basicCharacters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

highScore = 0.0
bestString = ""

nTries = 0

tmpScore, tmpString = monkeyBusiness(basicCharacters,magicString) # missing correct letters
"""
tmpLetters = []
for sidx in range(len(tmpString)):
    if(tmpString[sidx] == magicString[sidx]):
        tmpLetters.append(sidx)
"""

while(tmpScore != 1.0):
    nTries += 1
    if(tmpScore > highScore):
        highScore = tmpScore
        bestString = tmpString
    elif(nTries % 1000 == 0):
        print(nTries, "tries have elapsed")
        print("The best string so far is ",bestString,"with a score of",highScore)
    tmpScore, tmpString = monkeyBusiness_hc(basicCharacters,bestString,magicString)
    
print("Success after", nTries, "tries!")
