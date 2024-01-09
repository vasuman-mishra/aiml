import csv
hypo = ['%','%','%','%','%','%']

with open('//home/kakashi/Downloads/trainingdata.csv') as csv_file:
    readcsv = csv.reader(csv_file, delimiter=',')
    print(readcsv)
    
    data = []
    print("\nThe given training examples are:")
    for row in readcsv:
        print(row)
        if row[-1] == "Yes":
            data.append(row)

print("\nThe positive examples are:")
for x in data:
    print(x)
print("\n")

for i in range(len(data)):
    for k in range(len(data[i])-1):
        if hypo[k]=='%':
            hypo[k]=data[i][k]
        elif hypo[k]!=data[i][k]:
            hypo[k]='?'
            k=k+1        
        else:
            hypo[k]=hypo[k]
    print(hypo)

print("\nThe maximally specific Find-s hypothesis for the given training examples is :")
print(hypo)
