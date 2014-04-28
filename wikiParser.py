from lxml import html
import requests
import codecs
import csv

page = requests.get('https://en.wikipedia.org/wiki/List_of_Catholic_saints')
print page
page.encode = 'utf-8'
tree = html.fromstring(page.text)
saints = tree.xpath('//li/a[@title]/text()')

#   print (len(saints))

#   Let remove wikipedia clutters
afterEdit = []

#   Removing edit links
for saint in (saints):
    if (saint != 'edit'):
        afterEdit.append(saint.encode('utf-8'))

def canonize(listed):
    for s in (listed):
        print s

#   Whats the new length
#print len(afterEdit)
#canonize(afterEdit)

#   Removing everything before the list and everithing after the list

def makeSaintList(listed, start, end):
    return listed[start:end]

#   Crude way of removing things

#   Lets get index of some items in the list

def removeIndex(listed, string):
    return listed.index(string)

#   Lets break down list of saints to small lists
end = removeIndex(afterEdit, 'List of early Christian saints')
firstList = makeSaintList(afterEdit, 0, end)
theRest = afterEdit[end:]

start = removeIndex(theRest, 'Fatima')
end = removeIndex(theRest, 'Saints portal')
lastList = makeSaintList(theRest, start, end)

#   Make a new list of the two lists
allSaints = []
allSaints.extend(firstList)
allSaints.extend(lastList)

print len(allSaints)
#   sorting list
allSaints.sort()

#   Print the last list
#canonize(allSaints)

#   Lets write the list into a file so we could use to make
#   Simply turn list to csv

#   using secure way
with open('saintslist.txt', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(allSaints)
