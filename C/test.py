import ctypes as C

lib = C.CDLL("shared/game_of_life_algorithm.so")

l = [
        [0,0,0],
        [1,1,1],
        [0,0,0]
    ]

entrylist = []

for sub_l in l:
    entrylist.append((C.c_ubyte*len(sub_l))(*sub_l))


c_l = (C.POINTER(C.c_ubyte) * len(entrylist))(*entrylist)


for i in range(100):
    lib.nextGeneration(c_l, 3, 3)
    print 
    for i in range(3):
        print
        for j in range(3):
            print c_l[i][j],