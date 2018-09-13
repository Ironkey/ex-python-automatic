tableData = [['apples', 'oranges', 'cherres', 'banana'],
			 ['Alice', 'Bob', 'Carol', 'David'],
			 ['dogs', 'cats', 'moose', 'goose']]


def printTable():
    colWidths = [0] * len(tableData)

    for i in range(3):
        for j in range(3):
            if colWidths[i] <= len(tableData[j][i]):
                colWidths[i] = len(tableData[j][i])
            print(tableData[j][i].rjust(colWidths[i]), end='')
        print()

printTable()