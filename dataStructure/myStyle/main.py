from functionCollection import *

myHash = list()


for idx in range(2):
    key = 'key' + str(idx + 1)
    data = list()
    data.append(str(idx+1) + '-1')
    data.append(str(idx+1) + '-2')

    insert(key, data, myHash)
print(myHash)

for idx in range(3):
    key = 'key' + str(idx + 1)
    data = list()
    data.append(str(idx+1) + '-3')
    data.append(str(idx+1) + '-4')

    insert(key, data, myHash)
print(myHash)

