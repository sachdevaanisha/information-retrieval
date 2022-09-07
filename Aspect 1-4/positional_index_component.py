import string
import nltk

from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords

# This method will convert the text to lowercase
def lowercase(text):
    return text.lower()

# This method will remove all the punctuations
def removePunctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

# This method will preprocess the text
def preprocess(text):
    text = lowercase(text)
    text = removePunctuation(text)
    return text

# This method will tokenize the text
def tokenize(text):
    return text.split()

# This method will remove all the english stop words in a text
def removeStopWords(words):
    # Retrieve a collection of stopwords from the ntlk library
    stop_words = set(stopwords.words('english'))
    # Return each word which is not a stopword
    return [word for word in words if not word in stop_words]

# This method will apply stemming to the array of words/tokens
def applyStemming(words):
    # Creating a porterStemmer from the ntlk library
    ps = PorterStemmer()
    # Return a array of terms
    return list(map(lambda word: ps.stem(word), words))

# This method will normalize the words
def normalize(words):
    words = removeStopWords(words)
    #words = applyStemming(words)
    return words

# This method will index a collection of words
def index(words):
    indx = {}
    for position, word in enumerate(words):
        if not word in indx:
            indx[word] = [position]
        else:
            indx[word].append(position)
    return indx

def indexDocument(text):
    text = preprocess(text)
    tokens = tokenize(text)
    terms = normalize(tokens)
    return index(terms)




