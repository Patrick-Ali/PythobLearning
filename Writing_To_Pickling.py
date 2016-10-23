import pickle

f = open("DataStore.txt", "wb")

eng2sp = { "one": "uno", "four": "cuatro", "three": "tres", "two": "dos"}

sp2eng = { "cinco": "five", "seis": "six", "siete": "seven", "ocho": "eight"}

DiceCombos = { "12": "6+6", "11": "6+5", "10": "5+5", "9": "5+4",
               "7": "4+3", "6": "3+3", "5": "3+2", "8": "4+4",
               "4": "2+2", "3": "2+1", "2": "1+1"}


pickle.dump(sp2eng, f)

pickle.dump(DiceCombos, f)

f.close()

