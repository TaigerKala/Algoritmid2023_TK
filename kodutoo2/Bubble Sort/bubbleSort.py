#Introduction to algorithms, Thomas H. Cormen, et al, lk. 40
#https://www.geeksforgeeks.org/python-program-for-bubble-sort/


def bubble_sort(list):
    n = len(list)
    swapped = False
    vahetuse_nr = 0
    print("Algne sisend:\n", list)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                swapped = True
                list[j], list[j + 1] = list[j + 1], list[j]
                vahetuse_nr += 1
                print("Vahetus ", vahetuse_nr)
                print("Vahetati element ", list[j+1], " ja element ", list [j], "\n", list, "\n")
               

        if not swapped: 
            return


loend = [64, 34, 25, 12, 22, 11, 90]
loend_boonus = [8, 3, 5, 4, 7, 6, 2]
bubble_sort(loend_boonus)

print("Sorteeritud loend on:")
for i in range(len(loend)):
    print("% d" % loend[i], end=" ")