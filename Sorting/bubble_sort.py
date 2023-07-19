def main():
    x = [4, 2, 8, 3, 9, 1]
    bubble(x)
def bubble(list):
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
        print("Current state", list)

if __name__ == '__main__':
    main()