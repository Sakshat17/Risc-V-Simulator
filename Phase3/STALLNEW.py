l = [['x' for i in range(20)] for j in range(10)]
lastD = 0
DONE = [['x' for i in range(3)] for i in range(5)]


def addInstruction():  # kis row_index par instruction add kar rahe hai
    global lastD, l
    for p in range(len(l)):
        if (l[p] == ['x' for j in range(20)]):
            i = p
            break

    if (lastD != 0):
        lastD = l[i - 1].index('2')
    l[i][lastD] = '1'
    l[i][lastD + 1] = '2'
    l[i][lastD + 2] = '3'
    l[i][lastD + 3] = '4'
    l[i][lastD + 4] = '5'
    lastD += 1


def addStall(s, chrToInsert):  # s = number of stalls
    global l
    insToStall = 0
    posToInsert = 1
    for i in range(len(l)):
        if (l[i][0] == '2'):
            insToStall = i
            if(l[i][1] == '*'):
                posToInsert = 2
            break

    l[insToStall].insert(posToInsert, chrToInsert)
    l[insToStall].pop()

    if (len(l) - 1 > insToStall):
        for k in range(insToStall + 1, len(l)):
            for x in range(s):
                l[k].insert(0, 'x')
                l[k].pop()


def flush():
    global l
    i = len(l)
    for b in range(len(l)):
        if (l[b][0] == '2' or l[b][0] == '$'):
            i = b
            break

    for k in range(i + 1, len(l)):
        l[k].insert(0, 'x')
        l[k].pop()


def nextInst():
    global l
    DONE.pop(0)
    DONE.append(['x','x','x'])
    l.pop(0)
    l.append(['x' for i in range(20)])


def nextCycle():
    global l
    for i in range(len(l)):
        if(i<5):
            DONE[i].append(l[i].pop(0))
            DONE[i].pop(0)
        else:
            l[i].pop(0)
        l[i].append('x')
    if (l[0] == ['x' for i in range(20)]):
        nextInst()
        isFirstRowDeleted = True
    else:
        for i in range(len(l)):
            if(l[i] == ['x' for k in range(20)]):
                m = i
                break
        if(m <= 4):
            isFirstRowDeleted = True
        else:
            isFirstRowDeleted = False
    return isFirstRowDeleted

def printlist(g):
    print('----------------------------')
    print('----------------------------', end="\n")
    for i in range(len(g)):
        for j in range(len(g[i])):
            print(g[i][j], end=" ")
        print("\n")


stallCount = 0

# while(True):
#     i = int(input())
#     prev = 0
#     if(i==2): # Stall
#         ins = int(input()) # Which instruction
#         how = int(input())
#         whe = int(input()) #
#         addStall(l, ins, whe, how)
#         prev = how
#         stallCount = how
#     if(i==3):
#         ins = int(input())
#         flush(l,ins)
#     print(stallCount)
#
#     if(stallCount==0):
#         addInstruction(l,z)
#         if(z!=len(l)-1):
#             z+=1
#     else:
#         stallCount-=1
#     nextCycle(l)
#     printlist(l)
#
#
# print('----------------------------')
# print('----------------------------', end="\n")

