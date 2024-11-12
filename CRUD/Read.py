import csv
def read():
    with open('full_grouped.csv','r') as file:
        reader=csv.reader(file)
        for row in reader:
            print(row)
if __name__=="__main__":
    read()
