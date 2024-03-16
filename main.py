import csv


with open('languages.txt', encoding='utf8') as file:
    file.readline()
    read = list(csv.reader(file, delimiter='$'))
print(read)