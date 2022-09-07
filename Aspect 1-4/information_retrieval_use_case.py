# this document contains a use case scenario for aspect 1 & 4
import os 
from os import listdir
from os.path import isfile, join
import positional_index_component 
import permuterm_index_component
import wildcard_query_engine_component
import pickle
import time

# the path where the documents can be found
dir_path = os.path.dirname(os.path.realpath(__file__))
# we provided a mini dataset from our original dataset
path = dir_path + "\\mini-dataset\\"

# get document names from path
documentNames = [f for f in listdir(path) if isfile(join(path, f))]

# this is where the positional index component is used to build an positional index for each document
# after that the 
positionalIndex = {}
for documentName in documentNames:
    try:
        file = open(path + documentName, "r")
        documentText = file.read()
        positionalIndex_document = positional_index_component.indexDocument(documentText)
        for term in positionalIndex_document:
            if not term in positionalIndex:
                positionalIndex[term] = {}
                positionalIndex[term][documentName] = positionalIndex_document[term]
            else:
                positionalIndex[term][documentName] = positionalIndex_document[term]
    except Exception as inst:
        print(inst)

print("\nPositional index:")
print(positionalIndex)

permutermIndex = permuterm_index_component.createPermutermIndex(positionalIndex)

print("\nPermuterm index:")
print(permutermIndex)

print("\nResult query:")
print(wildcard_query_engine_component.query('w*rk', permutermIndex, positionalIndex))