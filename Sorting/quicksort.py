#Implement a QuickSort

items = [20, 6, 8, 53, 56, 23, 97, 87]

def quicksort(dataset, first, last):
    if first < last:
        #calculate the split point
        pivotIdx = partition(dataset, first, last)

        #Now sort the two partitions
        quicksort(dataset, first, pivotIdx-1)
        quicksort(dataset, pivotIdx+1, last)
    
def partition(datavalues, first, last):
    #choose the first item as the pivot value
    pivotvalue = datavalues[first]
    #Establish the upper and lower indexes
    lower = first + 1
    upper = last

    #start searching for a crossing point
    done = False
    while not done:
        #Advance the lower index
        while lower <= upper:
        #Advance the upper index

        #If the two indexes cross, we have found the split point
        pass
    
    #When the split point is found, exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp



