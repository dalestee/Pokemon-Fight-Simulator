import csv
a = []
with open('pokemon-gen2-data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        if line[2] not in a:
            a.append(line[2])
        elif line[3] not in a:
            a.append(line[3])
    print(a)