import sys
import random

# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))

if len(sys.argv) != 5:
    print("Usage: board.py Prob nRows nCols outFile")
    sys.exit(1)

prob = int(sys.argv[1])
nRows = int(sys.argv[2])
nCols = int(sys.argv[3])
outFfile = sys.argv[4]


with open(outFfile, 'w') as f:
    print("Rows: {0}".format(nRows))
    print("Cols: {0}".format(nCols))
    f.write(f'Rows: {nRows}')
    f.write(f'Cols: {nRows}')
    for i in range(0, nRows):
        for j in range(0, nCols):
            v = random.randint(0, 100)
            if v <= prob:
                print("#", end='')
                f.write("#")
            else:
                print(".", end='')
                f.write(".")
        print("")
        f.write("\n")
