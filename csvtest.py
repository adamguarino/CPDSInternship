import csv
def main():
    myData = [["first_name", "second_name", "Grade"],
              ['Alex', 'Brian', 'A'],
              ['Tom', 'Smith', 'B']]
    print("Declaring file object")
    myFile = open('example.csv', 'w')
    print("Writing data")
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)

    print("Writing complete")
main()      
