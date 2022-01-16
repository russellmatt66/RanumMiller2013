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
import infMnk_functions as imf

magicString = "methinks it is like a weasel"
basicCharacters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

highScore = 0.0
bestString = ""

nTries = 0

tmpScore, tmpString = imf.monkeyBusiness(basicCharacters,magicString) # missing correct letters
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
    tmpScore, tmpString = imf.monkeyBusiness_hc(basicCharacters,bestString,magicString)
    
print("Success after", nTries, "tries!")
