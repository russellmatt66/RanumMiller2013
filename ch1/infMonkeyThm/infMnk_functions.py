"""
Matt Russell
module file for Infinite Monkey Theorem project
"""

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
