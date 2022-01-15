"""
Matt Russell
1/14/22
Ranum and Miller
Self Check 1.4.3 - p.26
"""

# Given code to be modified:
word_list = ['cat','dog','rabbit']
letter_list = [ ]
for a_word in word_list:
    for a_letter in a_word:
        letter_list.append(a_letter)

print("Original list of letters is: ", letter_list)

# Exercise 1: Modify the given code so that the final list only contains a single copy of each letter
# Implementation idea: Use .count() to find duplicates, and .remove() until all the items only have a single occurrence
i = 0
while(i < len(letter_list)):
    if(letter_list.count(letter_list[i]) == 1):
       i += 1
    else:
       letter_list.remove(letter_list[i])

print("List of unique letters is: ", letter_list) # Destroys original copy - would need to run loop to get back. How to create a copy?

# Exercise 2: Redo the given code using list comprehension
