import tsv
def main():
    myFile = open('example.tsv', 'w')
    with myFile:
        writer = tsv.TsvWriter(myFile)
        writer.line("first_name", "second_name", "Grade")
        writer.line('Alex', 'Brian', 'A')
        writer.line('Tom', 'Smith', 'B')

main()