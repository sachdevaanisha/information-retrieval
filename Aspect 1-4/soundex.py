def soundex(term):

#Retaining the first alphabet of the term
    soundex = term[0]

#Mapping of similar sounding alphabets to numeric values
    mapping =  {"aeiouhwy":"0" ,
                "bfpv": "1",
                "cgjkqsxz":"2",
                "dt":"3",
                "l":"4",
                "mn":"5",
                "r":"6"}

#Generating the soundex code
    for i in term[1:]:
        for j in mapping.keys():
            if i in j:
                code = mapping[j]
                if soundex[-1] != code:
                    soundex = soundex + code

#Removing 0 from the resulting string
    soundex = soundex.replace("0","")
    soundex = soundex[:4]

#Appending 0, if the length of the resulting string is not 4
    while len(soundex)<4:
        soundex = soundex+"0"

    return soundex


# list = ["stuart","stewart"]
# print("Term\t\tSoundex")
# for name in list:
#      print("%s\t\t%s" % (name, soundex(name)))