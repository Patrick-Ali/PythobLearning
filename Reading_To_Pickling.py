import pickle

f = open("DataStore.txt", "rb")
sp2eng = pickle.load(f)

DiceCombos = pickle.load(f)

f.close()

print (sp2eng, DiceCombos)
