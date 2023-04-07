items = [3, 5, 1, 8, 4, 9, 6]
def mergesort(list):
    if len(list) > 1:
        mid = len(list) // 2
        leftarr = list[:mid]
        rightarr = list[mid:]
        print("place inside", list)
        print("\nleft", leftarr)
        print("\nright", rightarr)
    #reccursively lets break down the arrays
        mergesort(leftarr)
        mergesort(rightarr)
        print("place 1", list)
        print("\nleft", leftarr)
        print("\nright", rightarr)
        i = 0 #index for left array
        j = 0 #index for right array
        k = 0 #index for merged array

    #while both arrays have content
        while i < len(leftarr) and j<len(rightarr):
            if leftarr[i]<rightarr[j]:
                list[k] = leftarr[i]
                i+=1
            elif rightarr[j]<leftarr[i]:
                list[k] = rightarr[j]
                j+=1
            k+=1
    
        #If left array still has elements left
        while i < len(leftarr):
            list[k] = leftarr[i]
            i+=1
            k+=1
    
    #If right array still has elements left
        while j < len(rightarr):
            list[k] = rightarr[j] 
            j+=1
            k+=1
        print("place 2", list)
        print("\nleft 2", leftarr)
        print("\nright 2", rightarr)
#testing the data
print(items)
mergesort(items)
print(items)