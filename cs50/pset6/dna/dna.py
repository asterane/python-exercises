from sys import argv, exit
import csv


def main():
    # ensure that the user provided the correct no of args
    if len(argv) != 3:
        print(f"Usage: python {argv[0]} data.csv sequence.txt")
        exit(1)

    # read the DNA sequence into a file for later use
    with open(argv[2], "r") as file:
        seq = file.read()

    with open(argv[1], newline='') as csvfile:
        # create dict of STR counts, with the CSV headings as keys
        read = csv.reader(csvfile)
        strs = {key: runcount(seq, key) for key in next(read)[1::]}
        csvfile.seek(0)

        # check STR counts from sequence against forensic data
        reader = csv.DictReader(csvfile)
        for row in reader:
            match = True
            for s in strs.keys():
                if int(strs[s]) != int(row[s]):
                    match = False
            if match:
                print(row['name'])
                exit(0)

        print("No match")
        exit(0)


def runcount(seq, str):
    # Calculates the longest run of a particular
    # Short Tandem Repeat in the sequence
    end = False
    pos, ind, cnt, mxm = 0, 0, 0, 0
    while not end:
        # find next STR instance
        ind = seq.find(str, pos)
        if ind == -1:
            mxm = cnt if cnt >= mxm else mxm
            break
        # inc count if next follows last immediately
        if ind == pos:
            cnt += 1
            pos = ind + len(str)
        # reset count if next is in a separate run
        else:
            mxm = cnt if cnt >= mxm else mxm
            cnt = 1
            pos = ind + len(str)
    # return the longest run found
    return mxm


main()
