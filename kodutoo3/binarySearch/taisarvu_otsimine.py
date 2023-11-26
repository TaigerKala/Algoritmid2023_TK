#kood kirjutatud kodutöö 1 jaoks

def binaar_otsing(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1 



taisarvu_list = [3, 40, 79, 84, 119, 160, 306, 340, 348, 459, 466, 526, 556, 663, 681, 813, 874, 891, 921, 964, 976, 1059, 1078, 1095, 1200, 1258, 1267, 1271, 1334, 1366, 1491, 1592, 1667, 1712, 1760, 1768, 1772, 1829, 1842, 1861, 1943, 1980, 2012, 2028, 2031, 2042, 2081, 2148, 2261, 2354, 2379, 2587, 2611, 2619, 2622, 2635, 2717, 2773, 2794, 2868, 2915, 2971, 3002, 3033, 3146, 3185, 3202, 3337, 3432, 3504, 3513, 3733, 3748, 3820, 3857, 3885, 3986, 4024, 4074, 4108, 4127, 4151, 4297, 4312, 4345, 4390, 4410, 4422, 4479, 4503, 4506, 4555, 4557, 4669, 4676, 4680, 4782, 4819, 4886, 4964]


otsing = int(input("Sisesta taisarv mida listist otsida: "))
result = binaar_otsing(taisarvu_list, otsing)

if result != -1:
    print("Element on indeksil ", str(result))
else:
    print("Elementi pole listis")

