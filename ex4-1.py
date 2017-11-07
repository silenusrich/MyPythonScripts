def listPrint(items):
    for i in range(len(items)-1):
        items[i] += ', '
    items.insert(len(items)-1,'and ')
    for i in range(len(items)):
        print((items[i]),end = '')

spam = ['apples', 'bananas', 'tofu', 'cats']
listPrint(spam)
