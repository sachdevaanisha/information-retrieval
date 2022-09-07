from soundex import soundex

import pickle

import re
import sys
pi_soundex = open("pi_soundex.pickle","r+b")

data = pickle.load(pi_soundex)

word_1, word_2 = [x.lower() for x in input("Terms to be searched : ").split()]

#Removing numeric values and special characters from both the terms
soundexed = re.sub('[^A-Za-z]+', '', word_1)
soundex_word_1 = None if soundexed == '' else soundex(soundexed).capitalize()

soundexed = re.sub('[^A-Za-z]+', '', word_2)
soundex_word_2 = None if soundexed == '' else soundex(soundexed).capitalize()

#Taking input from the user
proximity = int(input("Proximity value : "))
option = int(input("Press 1 for 'within' operator or 2 for 'near' operator : "))

if option == 1:
    near = 0
else:
    near = -proximity

candidate_1 = []
candidate_2 = []

#Retrieving all the terms that have same soundex code as for term 1 and term 2
for k,v in data.items():
    if soundex_word_1 == v[0]:
        candidate_1.append(k)
    if soundex_word_2 == v[0]:
        candidate_2.append(k)

#If no soundex code could be found for either or the terms, display the error message
if not candidate_1 or not candidate_2:
    print("No document found with the given terms")
    sys.exit()

flag = False

#Finding intersecting documents
for word_1 in candidate_1:
    for word_2 in candidate_2:

        common_docs = list()

        for i in data[word_1][1].keys():
            for j in data[word_2][1].keys():
                if i==j:
                    common_docs.append(i)

#Checking the condition for 'within' and 'near' operator
        for i in common_docs:
            for j in data[word_2][1][i]:
                for k in data[word_1][1][i]:
                    if near <= j-k <= proximity:
                        flag = True
                        print("Found in '{}','{}' at '{}' and '{}' at '{}'".format(i,word_1,k,word_2,j))

if not flag:
    print("Either there is no common document for the given terms or the terms do not come within or near the specified proximity")
    sys.exit()