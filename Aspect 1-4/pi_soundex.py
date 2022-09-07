import pickle
import re

from soundex import soundex


#To generate the pickle and text file containing the soundex code for all the terms in the positional index
file = open("positional index with stopwords and wo stemming.pickle","r+b")
output = open("pi_soundex.txt","w+")
pi_soundex = open("pi_soundex.pickle","w+b")

data = pickle.load(file)
i = 0

#Removing numeric values and special characters from the terms in positional index and generating soundex code for strings containing only alphabets
#Generated soundex code for all the terms are added to the positional index (including stop words and without stemming)
for k in sorted(data):

    data[k] = [data[k]]

    soundex_word = re.sub('[^A-Za-z]+', '', k)
    soundexed = None if soundex_word == '' else soundex(soundex_word).capitalize()

    data[k].insert(0,soundexed)

    out = "Entry no : "+str(i)+"\n "+ str(k) + ":" + str(data[k]) + "\n"+("*"*30)+"\n"
    output.write(out)
    print(out)
    i+=1

print(type(data))
pickle.dump(data,pi_soundex)


