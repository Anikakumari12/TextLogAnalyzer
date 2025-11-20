📘 README.md

🧐Text Log Analyzer

A lightweight Python tool that reads a text file, cleans the content, counts how often each word appears, and exports the result to a CSV.  
This project is built with simplicity in mind and is a great example of practical text processing using only Python’s standard libraries.


🔍 Overview

The Text Log Analyzer takes any plain-text log file and breaks it down into meaningful word-frequency insights. It removes punctuation, handles case sensitivity, and organizes the output in a clean CSV file that you can easily open in Excel or any data tool.

This project is perfect for:
- Beginners practicing Python file handling
- Anyone trying to understand dictionaries and word counting
- Small-scale text analysis work



🧠 How It Works

1. Reads the input file (`log.txt`)
2. Converts everything to lowercase for consistency  
3. Splits the text into individual words  
4. Removes punctuation using `string.punctuation`
5. Counts each word using a dictionary  
6. Prints the results in the terminal  
7. Saves the final output to `word_count.csv`

Simple, clean, and efficient.



📂 Project Structure

TextLogAnalyzer/
│
├── text_log_analyzer.py # Main script
├── log.txt # Input file
├── word_count.csv # Output generated after running the script
└── README.md # Project documentation



🏃🏼▶️ How to Run

Make sure you are inside the project folder:

```bash
cd TextLogAnalyzer
Run the script:
python3 text_log_analyzer.py

🏃After running:
You'll see the word counts printed in the terminal
A new file named word_count.csv will appear in the project folder

📄 Sample Output
Word frequency count:
hello: 4
world: 2
python: 3

Word counts saved to word_count.csv ✔️


📦 Requirements
Python 3.x
No external packages needed



👤 Author
Anika Kumari
Data Engineer | Python Developer | Big Data Enthusiast