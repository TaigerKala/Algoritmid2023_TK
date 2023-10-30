
def selectionSort(list):
    #i = 0
    n = len(list)
    print("Algne sisend: ", list)

    for i in range(n - 1):
        minIndeks = i

        for j in range(i + 1, n):

            if list[j] < list[minIndeks]:
                minIndeks = j

        list[i], list[minIndeks] = list[minIndeks], list[i]

        print("Iteratsioon ", i)
        print("Vahetati elemendid ", list[i], " ja ", list[minIndeks])
        print(list)
        i += 1

loend = [29, 15, 56, 77, 18]
loend_boonus = [8, 3, 5, 4, 7, 6, 2]

selectionSort(loend_boonus)

print("Sorteeritud loend\n", loend_boonus)