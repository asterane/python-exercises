import sys

import csv
import sqlite3


def main():
    '''Accepts a comma separated value file as a command line argument,
        and imports the student data to an sqlite3 database.'''

    # check for correct number of arguments
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} data.csv")
        sys.exit(1)

    # connect to the target database using an sqlite3 instance
    database = sqlite3.connect('students.db')
    c = database.cursor()

    # open the csv file to import information from
    with open(sys.argv[1], newline='') as csvfile:
        reader = csv.reader(csvfile)

        # discard first row (headings)
        next(reader)

        # prepare each row for insertion into the database
        for row in reader:
            name = row[0].split()
            house = row[1]
            birth = int(row[2])

            # use different SQL queries depending on middle name presence
            if len(name) == 2:
                c.execute('''INSERT INTO students(first,last,house,birth)
                             VALUES (?,?,?,?)''',
                          (name[0], name[1], house, birth))
            elif len(name) == 3:
                c.execute('''INSERT INTO students(first,middle,last,house,birth)
                             VALUES (?,?,?,?,?)''',
                          (name[0], name[1], name[2], house, birth))

    database.commit()
    database.close()
    sys.exit(0)


main()
