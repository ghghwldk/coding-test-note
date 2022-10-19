myDictionary = dict()
list1 = list()
list1.append('1-1')
list1.append(1)

list2 = list()
list2.append('2-1')
list2.append('2-2')


myDictionary['key1'] = list1
myDictionary['key2'] = list2

print(myDictionary)

for key in myDictionary.keys():
    print(key + '의 value는?')
    print(myDictionary[key])

