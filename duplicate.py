with open ('names.txt','r',encoding = 'utf-8') as f:
    lines = f.readlines()
    nameList=[]
    tupleList=[]
    #print (type(nameList))
    for line in lines:
        content=line.strip()
        print (content)
        nameList.append(content)
    sortedList=sorted(nameList)
    #print(sortedList)
    for i in sortedList:
        count = nameList.count(i)
        if count > 1:
            x= (i, count)
            #print(x)
            tupleList.append(x)
    withoutDuplicate=set(tupleList)
    print(withoutDuplicate)
