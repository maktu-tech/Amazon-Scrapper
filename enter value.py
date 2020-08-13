import csv
get_list = []
with open("Details.csv", 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        print(row[2], float(row[2]))
csvfile.close()
print(get_list)
