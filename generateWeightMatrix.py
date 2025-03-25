import sys
import os
import csv

def getMostFrequentWordCount(words):
    mostFrequentWordCount = 0
    for word in words:
        count = words.count(word)
        if count > mostFrequentWordCount:
            mostFrequentWordCount = count
    return mostFrequentWordCount

def main():
    # get arg1 as input folder
    path = sys.argv[1]
    
    values = {}

    # create CSV file for index
    with open('weightMatrix.csv', 'w', newline='') as csvFile:
        reader = csv.reader(csvFile)

        for filename in os.listdir(path):
            file = open(path + '/' + filename)
            docName = filename[:-4]

            fileContent = file.read()
            words = fileContent.split()
            mostFrequentWordCount = getMostFrequentWordCount(words)
            
            # for each word, add the filename to the weight matrix
            for word in words: 
                if values.get(word) == None:
                    values[word] = {}
                values[word][docName] = words.count(word) / mostFrequentWordCount

            file.close()

        # generate the CSV file
        writer = csv.writer(csvFile)
        writer.writerow([''] + [filename[:-4] for filename in os.listdir(path)])
        for word in values.keys():
            line = [word]
            for filename in os.listdir(path):
                docName = filename[:-4]
                if docName in values[word]:
                    line.append(values[word][docName])
                else:
                    line.append(0)
            writer.writerow(line)
        
        print('weightMatrix.csv generated successfully.')

if __name__ == '__main__':
    main()
