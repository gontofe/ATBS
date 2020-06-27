#! /usr/bin/python
# Displays a well-organised table with right justified columns

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):

# set up an empty list for the lengths, with entries for each column
    colWidths = [0] * len(data)
# loop through the outer list
    for i in range(len(data)):
# for each item in the inner list, set the max length if it is longer than the stored value
        for j in range(len(data[i])):
            if len(data[i][j]) > colWidths[i]:
                colWidths[i] = len(data[i][j])

#for the length of the inner list, print a padded string in each column
#followed by a line break
    for j in range(len(data[0])):
        for k in range(len(data)):
            print(data[k][j].rjust(colWidths[k]), end=' ')
        print(' \n')

printTable(tableData)
            
