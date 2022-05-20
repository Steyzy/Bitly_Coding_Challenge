import json
import pandas as pd

def readFile(json_file, csv_file):
    #open the JSON file and read data
    file = open(json_file)
    decodes = json.load(file)
    #read the csv file
    encodes = pd.read_csv(csv_file)
    return decodes, encodes

def countLinks(decodes, encodes):
    #prepare the data
    hashes = encodes['hash'].values
    long_url = encodes['long_url'].values 

    #build hash tables to speed up calculations
    hash_url, counter = dict(), dict()
    for i in range(len(hashes)):
        hash_url[hashes[i]] = long_url[i]
        counter[hashes[i]] = 0  #initialize all links to 0 count

    #traverse the JSON data and count 
    for i in range(len(decodes)):
        entry = decodes[i]
        key = entry['bitlink'][-7:]     #assume all hashes are 7 bits
        if key in counter and entry['timestamp'][:4]=='2021':
            counter[key]+=1   

    #sort the counter array and print out the result in specified format
    temp, result = [], []
    for key, val in counter.items():
        temp.append((val, key))
    temp = sorted(temp, key=lambda tuple: tuple[0], reverse=True)     #sort the array based on counts
    for i in range(len(temp)):
        count, key = temp[i]
        result.append({hash_url[key]: count})     #append to result in specified format

    return result

if __name__=='__main__':
    decodes, encodes = readFile('decodes.json', 'encodes.csv')  #get data
    result = countLinks(decodes, encodes)   #count links
    print(result)
