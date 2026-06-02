# Word Frequency Analyzer

A simple and efficient Command Line Interface (CLI) tool built with Python. This program takes a paragraph or article as input and instantly calculates how many times each word is used, displaying the top 5 most frequent words.

## How it Works (Under the Hood)
This project uses the **Hash Map (Dictionary)** data structure in Python. 
Instead of checking words one by one using a nested loop ($O(n^2)$ time complexity), it uses a Dictionary to store and update word counts in **$O(1)$ time complexity**. This makes the program incredibly fast, even for large texts!

## Features
- Removes all punctuations and special characters automatically.
- Case-insensitive counting.
- Uses Hash Map logic for highly optimized searching and counting.

## How to Run
1. Clone the repository or download the `word_analyzer.py` file.
2. Run the script in your terminal:
   `python word_analyzer.py`
3. Paste any text and Enter!
