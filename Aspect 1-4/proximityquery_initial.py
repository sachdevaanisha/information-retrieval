import pickle
import sys
pi = open("positional index.pickle","r+b")

data = pickle.load(pi)

common_docs = []

#Taking input from user
word_1, word_2 = [x.lower() for x in input("Terms to be searched : ").split()]

proximity = int(input("Proximity value : "))
option = int(input("Press 1 for 'within' operator or 2 for 'near' operator : "))

if option == 1:
    near = 0
else:
    near = -proximity

flag = False
#Finding intersecting documents
if word_1 in data and word_2 in data:
    for i in data[word_1].keys():
        for j in data[word_2].keys():
            if i==j:
                common_docs.append(i)

#Checking the condition for 'within' and 'near' operator
    for i in common_docs:
        for j in data[word_2][i]:
            for k in data[word_1][i]:
                if near <= j-k <= proximity:
                    flag = True
                    print("Found in '{}','{}' at '{}' and '{}' at '{}'".format(i,word_1,k,word_2,j))

else:
    print("No document found with the given terms")
    sys.exit()

if not flag:
    print("Either there is no common document for the given terms or the terms do not come within or near the specified proximity")
    sys.exit()