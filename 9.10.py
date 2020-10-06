# David Gonzalez
# 1630338

import csv

name_file = input()

word_freq = {}

with open(name_file, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        for word in row:
            if word not in word_freq.keys():
                word_freq[word] = 1
            else:
                word_freq[word] += 1
for key in word_freq.keys():
    print(key + ' ' + str(word_freq[key]))
