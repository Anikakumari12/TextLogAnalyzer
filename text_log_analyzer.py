import csv
import string
with open('log.txt', 'r') as file:
    text = file.read()
words = text.lower().split()
words = [word.strip(string.punctuation) for word in words]
word_count = dict()
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print("Word frequency count:")
for word, count in word_count.items():
    print(f"{word}: {count}")
with open('word_count.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Word', 'Count'])  # header row
    for word, count in word_count.items():
        writer.writerow([word, count])
print("\nWord counts saved to word_count.csv ✅")

# Sort word counts by highest frequency
sorted_counts = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
words = [word for word in words if word]  # remove empty words

