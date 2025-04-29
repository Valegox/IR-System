import sys
import csv
import math
import numpy as np

def getTerms():
    result = []
    reader = csv.reader(open('generated/termDocumentMatrix.csv', 'r'))
    for row in reader:
        if reader.line_num == 1:
            continue
        result.append(row[0])
    return result

def getDocumentNames():
    reader = csv.reader(open('generated/termDocumentMatrix.csv', 'r'))
    result = next(reader)
    result.pop(0)
    return result

def getTermDocumentMatrix():
    result = []
    reader = csv.reader(open('generated/termDocumentMatrix.csv', 'r'))
    for row in reader:
        if reader.line_num == 1:
            continue
        convertedRow = [int(i) for i in row[1:]]
        result.append(convertedRow)
    return result

docNames = getDocumentNames()
terms = getTerms()

# Step 1: get the term document matrix
termDocumentMatrix = getTermDocumentMatrix()

# Step 2: Decompose matrix A and find U, S, V
U, S, Vt = np.linalg.svd(termDocumentMatrix, full_matrices=False)
V = Vt.T
S_mat = np.diag(S) # convert S to a diagonal matrix

# Step 3: implement rank k approximation
k = 90
U2 = U[:, :k]
S2 = S_mat[:k, :k]
V2 = V[:, :k]
VT2 = Vt[:k, :]

# Get S2 inverse
S2_inv = np.linalg.inv(S2)

def sanitizeText(text):
    text = text.lower()
    charsToRemove = [',', '.', '(', ')', '?', '!', ':', ';', '-', '"', '\'']
    for char in charsToRemove:
        text = text.replace(char, '')
    return text

class LSIModel:
    def __init__(self):
        try:
            print("Search documents by words.")
            query = str(input("▶  "))
            query = sanitizeText(query)
            result = self.processQuery(query)
            if len(result) == 0:
                print("No results found.")
                return
            print(f"-------- {len(result)} sorted results: --------")
            for (index, (i, score)) in enumerate(result):
                print(f"{index + 1}. {docNames[i]} (score: {score:.4f})")
            print("-----------------------------------")
        except ValueError:
            # Prevent any input issue from crashing the program
            return
        except KeyboardInterrupt:
            # Handle keyboard interrupts such as CTRL+C
            sys.exit(1)
    
    def processQuery(self, query):
        words = query.split(' ')
        queryMatrix = self.getQueryMatrix(words)
        # Calculate the query vector:
        queryVector = (queryMatrix @ U2) @ S2_inv

        pertinences = []
        for i, docVector in enumerate(V2):
            score = self.cosine_similarity(queryVector, docVector)
            if score > 0:
                pertinences.append((i, score))

        pertinences = sorted(pertinences, key=lambda x: x[1], reverse=True)
        return pertinences
    
    def getQueryMatrix(self, words):
        queryMatrix = [0 for i in range(len(terms))]
        for word in words:
            if word in terms:
                index = terms.index(word)
                queryMatrix[index] += 1
        return queryMatrix
    
    def cosine_similarity(self, a, b):
        if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
            return 0
        else:
            return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def main():
    while True:
        LSIModel()

if __name__ == '__main__':
    main()
