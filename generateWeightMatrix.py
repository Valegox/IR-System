import sys
import os
import csv
import math

def getMostFrequentWordCount(words):
    mostFrequentWordCount = 0
    for word in words:
        count = words.count(word)
        if count > mostFrequentWordCount:
            mostFrequentWordCount = count
    return mostFrequentWordCount

def sanitizeText(text):
    text = text.lower()
    text = text.replace(',', '')
    text = text.replace('.', '')
    text = text.replace('(', '')
    text = text.replace(')', '')
    text = text.replace('?', '')
    text = text.replace('!', '')
    text = text.replace(':', '')
    text = text.replace(';', '')
    text = text.replace('-', ' ')
    text = text.replace('"', '')
    text = text.replace('\'', '')
    return text

def main():
    # get arg1 as input folder
    path = sys.argv[1]
    
    values = {}

    # create CSV file for index
    with open('generated/weightMatrix.csv', 'w', newline='') as csvFile:
        reader = csv.reader(csvFile)

        # count the number of documents that contain each word
        wordContainerCounts = {}
        for filename in os.listdir(path):
            file = open(path + '/' + filename)
            fileContent = file.read()
            fileContent = sanitizeText(fileContent)
            words = fileContent.split()
            markedWords = []
            for word in words:
                if wordContainerCounts.get(word) == None:
                    wordContainerCounts[word] = 1
                elif word not in markedWords:
                    wordContainerCounts[word] += 1
                    markedWords.append(word)
            file.close()

        # for each document, calculate the weight of each word
        for filename in os.listdir(path):
            file = open(path + '/' + filename)
            docName = filename[:-4]

            fileContent = file.read()
            fileContent = sanitizeText(fileContent)
            words = fileContent.split()
            mostFrequentWordCount = getMostFrequentWordCount(words)
            
            # for each word, add the filename to the weight matrix
            for word in words: 
                tf = words.count(word) / mostFrequentWordCount
                idf = math.log(len(os.listdir(path)) / wordContainerCounts[word], 2)
                if values.get(word) == None:
                    values[word] = {}
                values[word][docName] = tf * idf

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
        
        print('generated/weightMatrix.csv generated successfully.')

if __name__ == '__main__':
    main()
