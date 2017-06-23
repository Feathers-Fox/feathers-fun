# REVIEW: Conditionals, for loops, lists, and functions

#INSTRUCTIONS:

#PartI:

#Make the string "sentence_string" into a list called "sentence_list"
#Use a for loop and an append function like this: list.append(something)

sentence_string = "Hello, my name is Monty Python."

sentence_list=[]



for letters in sentence_string:

    sentence_list.append(letters)

print sentence_list


#PartII:
# Print every item of the list using a for loop

for letters in sentence_string:
    print letters


#PartIII:
# write a for loop to find the index of 'b' in the list "vowels"
vowels = ['a', 'b', 'i', 'o', 'u', 'y']

index = 0
for letters in vowels:
    if letters == "b":
        print index
    index= index + 1




#PartIV:
# use the index found above to change 'b' to 'e'

#list vowels==
#b==e

vowels[1] = "e"
print vowels

#PartV:
# Using a for statement and an if statement, print all the vowels from the sentence




list_vowels=[]

for letters in sentence_list:
    if letters in vowels:
        list_vowels.append(letters)
print list_vowels



#PartVI:
#Make a new function called "vowelFinder" that will return a list that holds all the vowels found in a list (no duplicates).
#The function's parameters should be "list" and "vowels."

"""





Example:

vowelList = vowelFinder(sentence_string, vowels)
print vowelList

would print:
['a', 'e', 'i', 'o', 'y']
"""

#and if the letter is not in answerlist

#voewlFinder(vowelList)

