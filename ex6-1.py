tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    colWidths = [0]*len(data)
    for j in range(len(data[:])):
        for i in range(len(data)):
            colWidths[i] = len(max(data[i]))
            print(data[i][j].rjust(colWidths[i]+1),end='')
        print()

printTable(tableData)
