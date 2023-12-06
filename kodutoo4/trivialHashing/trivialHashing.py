#Kasutatud allikad: https://www.geeksforgeeks.org/index-mapping-or-trivial-hashing-with-negatives-allowed/
#Koodi autor Rituraj Jain
#Kood võetud analüüsiks ja big-o notatsiooni analüüsiks


def search(otsitav_suurus):
    if otsitav_suurus >= 0:
        return has[otsitav_suurus][0] == 1

    otsitav_suurus = abs(otsitav_suurus)
    return has[otsitav_suurus][1] == 1

def insert(tabel, tabeli_suurus):
    for i in range(0, tabeli_suurus):
        if tabel[i] >= 0:
            has[tabel[i]][0] = 1
        else:
            has[abs(tabel[i])][1] = 1


tabel = [3, 40, 79, 84, 119, 160, 306, 340, 348, 459, 466, 526, 556, 663, 681, 813, 874, 891, 921, 964, 976, 1059, 1078, 1095, 1200, 1258, 1267, 1271, 1334, 1366, 1491, 1592, 1667, 1712, 1760, 1768, 1772, 1829, 1842, 1861, 1943, 1980, 2012, 2028, 2031, 2042, 2081, 2148, 2261, 2354, 2379, 2587, 2611, 2619, 2622, 2635, 2717, 2773, 2794, 2868, 2915, 2971, 3002, 3033, 3146, 3185, 3202, 3337, 3432, 3504, 3513, 3733, 3748, 3820, 3857, 3885, 3986, 4024, 4074, 4108, 4127, 4151, 4297, 4312, 4345, 4390, 4410, 4422, 4479, 4503, 4506, 4555, 4557, 4669, 4676, 4680, 4782, 4819, 4886, 4964]

n = len(tabel)

MAX = 5000

has = [[0 for i in range(2)]
            for j in range(MAX + 1)]
insert(tabel, n)

x = 3337

if search(x) == True:
    print("Olemas")
else:
    print("Ei leia")




