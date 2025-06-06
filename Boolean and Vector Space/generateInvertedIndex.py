import sys
import os
import csv

index = {}

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
    text = text.replace('-', '')
    text = text.replace('"', '')
    text = text.replace('\'', '')
    return text

def indexWords(filePath, i):
    file = open(filePath)
    fileContent = file.read()
    fileContent = sanitizeText(fileContent)
    words = fileContent.split()
    # for each word, add the filename to the inverted index
    for word in words:
        if word in index:
            if str(i) not in index[word]:
                index[word] = index[word] + ' ' + str(i)
        else:
            index[word] = str(i)
    file.close()

def main():
    # get arg1 as input folder
    path = sys.argv[1]

    # create CSV file for index
    with open('generated/index.csv', 'w', newline='') as csvFile:
        fieldnames = ['index', 'document']
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        writer.writeheader()
        i = 1
        for filename in os.listdir(path):
            writer.writerow({'index': i, 'document': filename[:-4] })
            indexWords(path + '/' + filename, i)
            i += 1

    # create CSV file for inverted index
    with open('generated/invertedIndex.csv', 'w', newline='') as csvFile:
        fieldnames = ['word', 'frequency', 'documents']
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
        writer.writeheader()
        for word in index:
            writer.writerow({'word': word, 'frequency': len(index[word].split(' ')), 'documents': index[word]})
    
    print("generated/invertedIndex.csv generated successfully.")

if __name__ == '__main__':
    main()
