def insSort(lis):
    srt = []
    lngth = len(lis)
    
    for item in lis:
        if len(srt) == 0:
            srt.append(item) #if it's the first item, put in list.
        elif item in srt:
            ndx = srt.index(item)
            srt.insert(ndx, item) #if it already exists, put by itself.
        else:
            l = len(srt) 
            for i in range(l): #for each item in the sorted list
                if srt[i] > item: #when you find a num larger than the item
                    srt.insert(i, item) #insert in front of that item, and escape
                    break
                if i == l-1:
                    srt.append(item)
    return srt
        


def insertSort(lis):
    ln = len(lis)
    for j in range(1, ln): #for each element in the list, starting with the second
        key = lis[j]  #the item to sort is the jth item, remember it.
        i = j-1  #initialize counter to one before the item being sorted. 
        while i > -1 and lis[i]>key: #while counter isn't negative, and the item found there is bigger than the key
           lis[i+1] = lis[i]  #set the 
           i -= 1
        lis[i+1] = key
    return lis
        
     
        
                    
            
