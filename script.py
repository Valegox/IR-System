import sys
import csv
import math

def removeSurroundingSpaces(self):
    return "".join(self.rstrip().lstrip())

def getDocumentsIncludingWord(word):
    reader = csv.reader(open('generated/invertedIndex.csv', 'r'))
    for row in reader:
        if row[0].lower() == word.lower():
            return row[2].split(' ')
    return []

def getDocumentNames():
    docs = {}
    reader = csv.reader(open('generated/index.csv', 'r'))
    for row in reader:
        if row[0] != 'index': 
            docs[row[0]] = row[1]
    return docs

docNames = getDocumentNames()

class BooleanModel:

    def __init__(self):
        print("Search documents by words. You can use AND, OR and NOT operators.")
        query = str(input("▶  ")).lower()
        result = self.processQuery(query)
        print(f"----- {len(result)} unsorted results: -----")
        for doc in result:
            print(f'{doc} {docNames[doc]}')
        print("--------------------")

    def processQuery(self, query):
        if " or " in query:
            query = query.split(" or ", 1)
            return self.processOR(query[0], query[1])
        if " and " in query:
            query = query.split(" and ", 1)
            return self.processAND(query[0], query[1])
        if "not " in query:
            query = query.split("not ", 1)
            return self.processNOT(query[1])

        query = removeSurroundingSpaces(query)
        if " " in query:
            query = query.split(" ", 1)
            return self.processAND(query[0], query[1])
        return getDocumentsIncludingWord(query)

    # This method retrieves all the documents that contain either wordA or wordB
    def processOR(self, partA, partB):
        # print(f'[{partA}] OR [{partB}]')
        docsA = self.processQuery(partA)
        docsB = self.processQuery(partB)
        result = docsA + docsB
        # Merge and remove duplicates:
        return list(dict.fromkeys(result))

    # This method retrieves all the documents that contain both wordA and wordB
    def processAND(self, partA, partB):
        # print(f'[{partA}] AND [{partB}]')
        docsA = self.processQuery(partA)
        docsB = self.processQuery(partB)
        result = []
        # Find the intersection of the two lists:
        for doc in docsA:
            if doc in docsB:
                result.append(doc)
        return result

    # This method retrieves all the documents that do not contain the wordB
    def processNOT(self, query):
        # print(f'NOT {query}')
        docs = self.processQuery(query)
        result = []
        for docName in docNames:
            if docName not in docs:
                result.append(docName)
        return result

class VectorSpaceModel:
    def __init__(self):
        print("Search documents by words.")
        query = str(input("▶  ")).lower()
        result = self.processQuery(query)
        print(f"----- {len(result)} sorted results: -----")
        for (index, docName) in enumerate(result):
            print(f'{index + 1}. {docName}')
        print("--------------------")
    
    def processQuery(self, query):
        words = query.split(' ')
        pertinences = {}
        for docIndex, doc in enumerate(docNames.values()):
            docVector = self.getDocumentVector(docIndex + 1, words)
            docVectorLength = self.getVectorLength(docVector)
            if docVectorLength > 0:
                pertinences[doc] = docVectorLength
        # Create a sorted list of docs
        result = sorted(pertinences.keys(), key=lambda k: pertinences[k], reverse=True)
        return result
    
    def getDocumentVector(self, docIndex, words):
        docVector = []
        reader = csv.reader(open('generated/weightMatrix.csv', 'r'))
        for row in reader:
            if row[0].lower() in words:
                docVector.append(float(row[docIndex]))
        return docVector
    
    def getVectorLength(self, vector):
        squareSum = 0
        for value in vector:
            squareSum += value * value
        return math.sqrt(squareSum)

def main():
    while True:
        try:
            print("Type '1' for Boolean Model or '2' for Vector Space Model.")
            print("Type 'exit' to quit the program.")
            # Get lowered case input from the user
            cmd = str(input("▶  ")).lower()
            cmd = removeSurroundingSpaces(cmd)
            # Handle the command:
            if cmd == "1":
                while True:
                    model = BooleanModel()
            elif cmd == "2":
                while True:
                    model = VectorSpaceModel()
            elif cmd == "exit":
                sys.exit(1)
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            # Prevent any input issue from crashing the program
            continue
        except KeyboardInterrupt:
            # Handle keyboard interrupts such as CTRL+C
            sys.exit(1)

if __name__ == '__main__':
    main()
