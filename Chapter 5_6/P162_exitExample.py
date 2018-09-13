def printPicnic(itemDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItem = {'sandwiched': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItem, 12, 5)
printPicnic(picnicItem, 20, 6) 