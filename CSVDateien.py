import csv

with open('muster.txt','r') as file:
    rdr = csv.reader(file, delimiter=',')
    heads = next(rdr)


    for line in rdr:
        for i in range(len(heads)):
            print(heads[i]+':', line[i])
        print()

