def insert(key, data, myHash):
    if hasKey(key, myHash):
        beforeData = getDataByKey(key, myHash)
        listAppend(beforeData, data)
    else:
        keyAndValue = dict()
        keyAndValue[key] = data
        myHash.append(keyAndValue)

def getDataByKey(key, myHash):
    for i in range(len(myHash)):
        keyAndValue = dict(myHash[i])
        keys = list(keyAndValue.keys())
        if keys.__contains__(key):
            key = keys[0]
            return keyAndValue[key]
    return None

def listAppend(list1, list2):
    for i in range(len(list2)):
        list1.append(list2[i])

def hasKey(key, myHash):
    for i in range(len(myHash)):
        keyAndValue = dict(myHash[i])
        keys = list(keyAndValue.keys())
        if keys.__contains__(key):
            return True
    return False

