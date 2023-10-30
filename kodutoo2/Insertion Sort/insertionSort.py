#Kasutatud allikad: https://www.geeksforgeeks.org/insertion-sort/
#Introduction to algorithms; Thomas H. Cormen, et al; lk. 16, 26

def insertionSort(list):
    for i in range(1, len(list)):

        key = list[i]
        j = i - 1 
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
        print("Iteratsioon ", i)
        print(list)

loend = [12, 11, 13, 5, 6, 7]
loend_boonus = [8, 3, 5, 4, 7, 6, 2]
insertionSort(loend_boonus)
print(loend_boonus)