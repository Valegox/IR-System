import sys
import os
import csv
import math
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def sanitizeText(text):
    text = text.lower()
    charsToRemove = [',', '.', '(', ')', '?', '!', ':', ';', '-', '"', '\'']
    for char in charsToRemove:
        text = text.replace(char, '')
    return text

def main():
    # get arg1 as input folder
    path = sys.argv[1]
    
    values = {}

    # create CSV file for index
    with open('generated/termDocumentMatrix.csv', 'w', newline='') as csvFile:
        reader = csv.reader(csvFile)

        # for each document, calculate the weight of each word
        for filename in os.listdir(path):
            file = open(path + '/' + filename)
            docName = filename[:-4]

            fileContent = file.read()
            fileContent = sanitizeText(fileContent)
            words = fileContent.split()
            words = [word for word in words if word not in stop_words and len(word) > 1] # remove stopwords
            
            # for each word, add the filename to the weight matrix
            for word in words: 
                if values.get(word) == None:
                    values[word] = {}
                values[word][docName] = words.count(word)

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
