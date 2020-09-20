import sys
import sqlite3


def main():
    '''Accepts the name of a Hogwarts house as a command line argument,
        and uses a database to report sorted student information'''

    # check for correct number of arguments
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} house")
        sys.exit(1)

    # connect to the target database using an sqlite3 instance
    database = sqlite3.connect('students.db')
    c = database.cursor()

    # pull rows of pertinent data, already sorted
    for row in c.execute('''SELECT first, middle, last, birth
                            FROM students WHERE house LIKE ?
                            ORDER BY last, first''', (sys.argv[1].lower(), )):
        # display names properly based on middle name presence
        if row[1] is None:
            print(f"{row[0]} {row[2]}, born {row[3]}")
        else:
            print(f"{row[0]} {row[1]} {row[2]}, born {row[3]}")

    c.close()


main()
