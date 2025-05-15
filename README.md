# IR System

## Introduction

This project aims to create an Information Retrevial System using 3 models:
- Boolean Model
- Vector Space Model
- LSI Model

## Data sources

Data sources are 1000 song lyrics in text format and located under the `data` directory.

Data retrieved from [this API](https://lyricsovh.docs.apiary.io/#).

  
## How to use Boolean and Vector Space Model 

### Prerequisite
- python3

### Generate required files

Generate inverted index and weight matrix under the `Boolean and Vector Space/generated` directory (CSV files):
```
$ cd "Boolean and Vector Space"
$ python3 generateInvertedIndex.py ../data
$ python3 generateWeightMatrix.py ../data
```

### Run the program

```
$ python3 script.py
```

- Type **1** if you want to use the **boolean model**
- Type **2** if you want to use the **vector space model**

You can then type a query and expect results according to the model you chose. 

### Example

<img width="540" alt="Capture d’écran 2025-03-25 à 18 15 16" src="https://github.com/user-attachments/assets/26a790f9-7c81-4738-baf7-40bbb2764c65" />

## How to use LSI Model

### Prerequisites
- python3
- nltk (used to filter stopwords)
- numpy (used for matrix calculation)

### Generate required files

Generate term document matrix under the `LSI/generated` directory (CSV file):
```
$ cd LSI
$ python3 generateTermDocumentMatrix.py ../data
```

### Run the program

```
$ python3 script.py
```

You can then type a query.
