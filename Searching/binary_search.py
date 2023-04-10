#Searching for an item in an ordered list using Binary Search

items = [3, 4, 6, 7, 8, 9, 12, 53, 66, 68]
def binarySearch(item, itemList):
    list_size = len(itemList) - 1
    lowerindx = 0
    upperindx = list_size

    while lowerindx <= upperindx:
        midpt = (lowerindx+upperindx) // 2

        if itemList[midpt] == item:
            return midpt
        elif item < itemList[midpt]:
            upperindx = itemList[midpt-1]
        else:
            lowerindx = itemList[midpt+1]
    
    if lowerindx > upperindx:
        return None

print(binarySearch(7, items))