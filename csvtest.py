import csv
def main():
    #Creates an array with hard-coded data to be stored
    myData = [["first_name", "second_name", "Grade"],
              ['Alex', 'Brian', 'A'],
              ['Tom', 'Smith', 'B']]
    print("Declaring file object")
    #Creates a file called example.csv, "w" means you can write to the file  
    myFile = open('example.csv', 'w')
    print("Writing data")
    #Writes the above data to the file
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)

    print("Writing complete")
main()      
