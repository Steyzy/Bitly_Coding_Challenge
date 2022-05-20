from itertools import count
import json
import pandas as pd
from script import readFile, countLinks

############## test the data import ##############

decodes, encodes = readFile('decodes.json', 'encodes.csv')
#make sure data has the correct length and format
print("The file contains %d entries, and the data is of type %s" % (len(decodes), type(decodes)))   
print("Here are the first 5 entires of decodes.json file:") 
print([i['bitlink'] for i in decodes[:5]])    #print first 5 bitlinks and compare to decodes.json

#read the csv file and check output
encodes = pd.read_csv('encodes.csv')
print("Here is the encodes.csv table:")
print(encodes)

############## test the calculation part ##############
test_data = decodes[:20]    #take the first 20 entries in json file as test data
result = countLinks(test_data, encodes)
print(result)   #check the first 20 and see if result is correct

test_data2 = []     #create another test data
hashes = encodes['hash'].values
domain = encodes['domain'].values
long_url = encodes['long_url'].values 
for i in range(len(hashes)):
    url = 'https://'+domain[i]+'/'+hashes[i]
    test_data2.append({'bitlink':url, 'timestamp':'2021'})
result2 = countLinks(test_data2, encodes)
print(result2)  #we should expect each link to be exactly 1 count
