# IR System

## Introduction

This project aims to create an Information Retrevial System using 2 models:
- Boolean Model
- Vector Space Model

## Data sources

Data sources are in text format and located under the `data` directory. In this example, song informations are provided:
- Title
- Artist
- Year
- Genre
- Album name
- Lyrics 

## How to use

### Prerequisite
- python3

### Generate required files

Generate inverted index and weight matrix under the `generated` directory (CSV files):
```
$ python3 generateInvertedIndex.py data
$ python3 generateWeightMatrix.py data
```

### Run the program

Run the IR program:
```
$ python3 script.py
```

- Type **1** if you want to use the **boolean model**
- Type **2** if you want to use the **vector space model**

You can then type a query and expect results according to the model you chose. 
  

## Example

<img width="540" alt="Capture d’écran 2025-03-25 à 18 15 16" src="https://github.com/user-attachments/assets/26a790f9-7c81-4738-baf7-40bbb2764c65" />
