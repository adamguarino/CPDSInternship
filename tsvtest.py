import tsv
def main():
    #Creates a file called example.tsv, "w" means you can write to the file
    myFile = open('example.tsv', 'w')
    with myFile:
        #Writes to the file and includes whatever data you put in here
        writer = tsv.TsvWriter(myFile)
        writer.line("first_name", "second_name", "Grade")
        writer.line('Alex', 'Brian', 'A')
        writer.line('Tom', 'Smith', 'B')

main()
