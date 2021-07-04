# R format - add, and, or, sll, slt, sra, srl, sub, xor, mul, div, rem
# I format - addi, andi, ori, lb, lh, lw, jalr
# S format - sb, sw, sh
# SB format - beq, bne, bge, blt
# U format - auipc, lui
# UJ format - jal

# ALUop       OPCODE        FUN3        FUNC7/FUN6
# 1 - add     0110011       000          0000000
# 2 - and     0110011       111          0000000
# 3 - or      0110011       110          0000000
# 4 - sll     0110011       001          0000000
# 5 - slt     0110011       010          0000000
# 6 - sra     0110011       101          0100000
# 7 - srl     0110011       101          0000000
# 8 - sub     0110011       000          0100000
# 9 - xor     0110011       100          0000000
# 10 - mul    0110011       000          0000001
# 11 - div    0110011       100          0000001
# 12 - rem    0110011       110          0000001

# 13 - addi   0010011       000          NA
# 14 - andi   0010011       111          NA
# 15 - ori    0010011       110          NA

# 16 - lb     0000011       000          NA
# 17 - lh     0000011       001          NA
# 18 - lw     0000011       010          NA

# 19 - jalr   1100111       000          NA

# 20 - sb     0100011       000          NA
# 21 - sw     0100011       010          NA
# 22 - sh     0100011       001          NA

# 23 - beq    1100011       000          NA
# 24 - bne    1100011       001          NA
# 25 - bge    1100011       101          NA
# 26 - blt    1100011       100          NA

# 27 - auipc  0010111       NA           NA

# 28 - lui    0110111       NA           NA

# 29 - jal    1101111       NA           NA

import sys
from .assistFunc import *
from .register import *  # Also Contains Initialization of PC, IR, clock
from .STALLNEW import *
import math

# Initializing Variables
rd = ""
rs1 = ""
rs2 = ""
immediate = ""
ALUop = -1
nALUop = -1
RA = ['0' for i in range(32)]
RB = ['0' for i in range(32)]
RM = ['0' for i in range(32)]
RZ = ['0' for i in range(32)]
nRZ = ['0' for i in range(32)]
nnRZ = ['0' for i in range(32)]
Fetch_IR = ['0' for i in range(32)]
Decode_IR = ['0' for i in range(32)]
MuxASelect = 0
MuxBSelect = 0
MuxINCSelect = 0
isBranch = 0
MuxPCSelect = 0
MuxYSelect = 0
pMuxYSelect = 0
ppMuxYSelect = 0
pppMuxYSelect = 0
MuxRMSelect = 0
MuxMSelect = 0
memRead = 0
pmemRead = 0
ppmemRead = 0
memWrite = 0
pmemWrite = 0
ppmemWrite = 0
loadType = 0
pploadType = 0
ploadType = 0
storeType = 0
ppstoreType = 0
pstoreType = 0
writeRegisterFile = 0
pwriteRegisterFile = 0
ppwriteRegisterFile = 0
pppwriteRegisterFile = 0
isStall = False
MAR = ['0' for i in range(32)]
MDR = ['0' for i in range(32)]
nINC = ['0' for i in range(32)]
PCtemp = ['0' for i in range(32)]
nRB = ['0' for i in range(32)]
RY = ['0' for i in range(32)]
pPC = ['0' for i in range(32)]
ppPC = ['0' for i in range(32)]
cPC = ['0' for i in range(32)]
pPCtemp = ['0' for i in range(32)]
ppPCtemp = ['0' for i in range(32)]
pppPCtemp = ['0' for i in range(32)]
ppppPCtemp = ['0' for i in range(32)]
prevPrevPrevRD = ""
prevPrevRD = ""
prevRD = ""
file_name = ""
display = ""
curIns = ["", ""]
prevIns = ["", ""]
prevPrevIns = ["", ""]
prevPrevPrevIns = ["", ""]
isDependentPrev = False
stallCount = 0
MuxRASelect = 0
MuxRBSelect = 0
isControlStall = 0
flushCount = 0
isInBTB = False
BTB = {}
pRZ = ['0' for i in range(32)]
RZZ = ['0' for i in range(32)]
controlEDType = 0
branchType = 0

TotalCycles = 0  # Done
InstructionsExecuted = 0  # Done
dataTransfer = 0  # Load Store Done
ALUInstructions = 0  # Done
controlInstructions = 0  # Done
numberOfStalls = 0  # Done
dataHazzards = 0  # Done
controlHazzards = 0  # Done
branchMisprediction = 0  # Done
dataHazzardStalls = 0  # Done
controlHazzardStalls = 0  # Done
PC = ['0' for i in range(32)]
IR = ['0' for i in range(32)]
pRY = ['0' for i in range(32)]
clock = 0
isEnding = False
isFirstRowDeleted = True
CPI = 0.0

displayFetch = ""
displayDecode = ""
displayExecute = ""
displayMemory = ""
displayWriteBack = ""

insFetch = ""
insDecode = ""
insExecute = ""
insMemory = ""
insWriteBack = ""

flagPrintRegisters = '0'
flagPrintPipeline = '0'
flagPrintPipelineType = '0'
pipelinePrintInstruction = ''
flagDataForwarding = ''
isCStall = 0

dataMisses = 0
dataHits = 0
dataAccess = 0
dataAssociativity = 0
dataCacheSize = 0
dataCacheBlockSize = 0
dataNoOfBlocks = 0
dataNoOfSets = 0
dataCache = []


insAccess = 0
insHits = 0
insMisses = 0
insAssociativity = 0
insCacheSize = 0
insCacheBlockSize = 0
insNoOfBlocks = 0
insNoOfSets = 0
instructionCache = []

instructionVictimArray = []
dataVictimArray = []

dataiIndex = -1
insiIndex = -1
insVictimiIndex = -1
dataVictimiIndex = -1

#GUI
stepID = 1
isFinalBreak = 0
calledFromGui = 0
isControlHazard = 0
isDataHazard = 0
insVictim = (-1,-1)
dataVictim = (-1,-1)

copyOfl = [['x' for i in range(20)] for j in range(10)]
copyOfDONE = [['x' for i in range(3)] for i in range(5)]

#10000004 00 5 01 6 10 7 11  BlockSize = 4 BlockOffest = 2
#Tag: [Block, RecencyInfo,dirty bit]
#Block : String
#Word1Word2Word3Word4

def assignRegister(registerNum, reqValue):
    temp_assignReg = list(str(bin(int(reqValue, 16))[2:]).zfill(32))
    for i in range(32):
        registerFile[registerNum][i] = temp_assignReg[i]


# Creating RegisterFile
registerFile = [['0' for i in range(32)] for j in range(32)]  # 0-based indexing

# Stack Pointer 0x7FFFFFFC
assignRegister(2, "0x7FFFFFFC")

dataSegment = {}

def loadDataSegment():
    # Address for data segment  "0x10000000"
    file = open(file_name, "r+")
    data = file.readlines()
    for line in data:
        word = list(line.split())
        if (int(word[0], 0) >= int("0x10000000", 0)):
            word[0] = str(bin(int(word[0], 16))[2:]).zfill(32)
            word[1] = str(bin(int(word[1], 16))[2:]).zfill(8)
            dataSegment[word[0]] = word[1]

instructionSegment = {}

def loadInstructionSegment():
    file = open(file_name, "r+")
    data = file.readlines()
    for line in data:
        word = list(line.split())
        # word is in little Indian
        # Convert in Big Indian

        if (int(word[0], 0) < int("0x10000000", 0)):
            big_endian = "0x" + word[1][8] + word[1][9] + word[1][6] + word[1][7] + word[1][4] + word[1][5] + word[1][
                2] + word[1][3]
            word[0] = str(bin(int(word[0], 16))[2:]).zfill(32)
            big_endian = str(bin(int(big_endian, 16))[2:]).zfill(32)
            instructionSegment[word[0]] = big_endian


def printRegisters():
    print("< Cycle Number >", clock)
    print("< PC >", "".join(PC))
    print("< IR >", "".join(Fetch_IR))
    print()
    for i in range(8):
        for j in range(4):
            regNum = 8 * j + i
            if (regNum == 8 or regNum == 9):
                print("x" + str(regNum) + "  = 0x" + str(hex(int("".join(registerFile[regNum]), 2))[2:]).zfill(8),
                      end='      ')
            else:
                print("x" + str(regNum) + " = 0x" + str(hex(int("".join(registerFile[regNum]), 2))[2:]).zfill(8),
                      end='      ')
        print()
    print("\n")


def printPipelineFetchDecode():
    global Decode_IR, Fetch_IR, ppppPCtemp, pppPCtemp, ppPCtemp, pPCtemp, PCtemp, ppPC, pPC, cPC
    print("===================== Inter Stage Buffers Fetch-Decode =====================")

    print("\t\t\tDecode_IR = ", "".join(Decode_IR))
    print("\t\t\tFetch_IR = ", "".join(Fetch_IR))
    print("\t\t\tppppPCtemp = ", "".join(ppppPCtemp))
    print("\t\t\tpppPCtemp = ", "".join(pppPCtemp))
    print("\t\t\tppPCtemp = ", "".join(ppPCtemp))
    print("\t\t\tpPCtemp = ", "".join(pPCtemp))
    print("\t\t\tPCtemp = ", "".join(PCtemp))
    print("\t\t\tppPC = ", "".join(ppPC))
    print("\t\t\tpPC = ", "".join(pPC))
    print("\t\t\tcPC = ", "".join(cPC))



# TotalCycles = 0 # Done
# InstructionsExecuted = 0 # Done
# dataTransfer = 0 # Load Store Done
# ALUInstructions = 0  # Done
# controlInstructions = 0 # Done
# numberOfStalls = 0 # Done
# dataHazzards = 0  # Done
# controlHazzards = 0 # Done
# branchMisprediction = 0 # Done
# dataHazzardStalls = 0 # Done
# controlHazzardStalls = 0 # Done


def printAtSimulationEnd():
    global CPI
    print("Total number of clock cycles = ", clock)
    print("Total number of instructions executed = ", InstructionsExecuted)
    if (InstructionsExecuted > 1):
        CPI = clock / (InstructionsExecuted - 1)
    print("CPI = ", round(CPI, 5))
    print("Number of data-transfer instructions executed = ", dataTransfer)
    print("Number of ALU instructions executed = ", ALUInstructions)
    print("Number of Control instructions executed = ", controlInstructions)
    print("Number of stalls/bubbles in the pipeline = ", numberOfStalls)
    print("Number of data hazards = ", dataHazzards)
    print("Number of control hazards = ", controlInstructions)
    print("Number of branch mispredictions = ", branchMisprediction)
    print("Number of stalls due to data hazards = ", dataHazzardStalls)
    print("Number of stalls due to control hazards = ", controlHazzardStalls)

    print("======================== Cache Info =================================")
    print("==================== INSTRUCTION CACHE ==============================")
    print("No of Access in Instruction Cache = ",insAccess)
    print("No of Hits Instruction Cache = ",insHits)
    print("No of Misses Instruction Cache = ",insMisses)
    print("========================= DATA CACHE ==============================")
    print("No of Access in Data Cache = ",dataAccess)
    print("No of Hits Data Cache = ",dataHits)
    print("No of Misses Data Cache = ",dataMisses)

    for i in range(8):
        for j in range(4):
            regNum = 8 * j + i
            if (regNum == 8 or regNum == 9):
                print("x" + str(regNum) + "  = 0x" + str(hex(int("".join(registerFile[regNum]), 2))[2:]).zfill(8),
                      end='      ')
            else:
                print("x" + str(regNum) + " = 0x" + str(hex(int("".join(registerFile[regNum]), 2))[2:]).zfill(8),
                      end='      ')
        print()
    print("\n")


# Initializing all 32 registers to 0
def resetSimulator():
    global PC, clock, IR, dataSegment, display, l, lastD, DONE
    display = ""
    insFetch = ""
    insDecode = ""
    insExecute = ""
    insMemory = ""
    insWriteBack = ""
    dataSegment = {}
    loadDataSegment()
    clock = 0
    instructionCache = []
    dataCache = []
    for i in range(32):
        PC[i] = '0'
        Fetch_IR[i] = '0'
    for i in range(32):
        assignRegister(i, "0x0")
    assignRegister(2, "0x7FFFFFFC")
    l = [['x' for i in range(20)] for j in range(10)]
    lastD = 0
    DONE = [['x' for i in range(2)] for i in range(5)]


def loadFromInstructionCache(addr):
    global insVictim, insMisses, insHits, insAccess,insiIndex, insVictimiIndex
    insVictin = (-1,-1)
    insAccess+=1
    insBlockOffSetSize = int(math.log(insCacheBlockSize, 2))
    insIndexSize = int(math.log(insNoOfSets, 2))
    insTagSize = len(addr) - insBlockOffSetSize - insIndexSize
    blockOffset = addr[insTagSize + insIndexSize:]
    iBlockOffset = int(blockOffset, 2)
    index = addr[insTagSize:insTagSize + insIndexSize]
    insiIndex = int(index, 2)
    tag = addr[0:insTagSize]
    # 00 - 0   01 - 1   10 - 2  11- 3
    # 0 - 32   32-64    (i * 32 : (i + 1) * 32)
    #Cache contains the block
    if(tag in instructionCache[insiIndex]):
        insHits += 1
        for x in instructionCache[insiIndex]:
            val = instructionCache[insiIndex][x]
            if x == tag:
                val[1] = insAssociativity - 1
                flag = True
            else:
                val[1] = val[1] - 1 if val[1] != 0 else 0
        return instructionCache[insiIndex][tag][0][iBlockOffset * 8 : (iBlockOffset // 4) * 4 *8 + 32]
    else:
        blockAddress = tag + index
        blockData = ""
        for m in range(2 ** (insBlockOffSetSize-2)):
            wordAddress = blockAddress + str(bin(4 * m)[2:]).zfill(insBlockOffSetSize)
            if(wordAddress in instructionSegment):
                blockData += instructionSegment[wordAddress][24 : 32] + instructionSegment[wordAddress][16 : 24] + instructionSegment[wordAddress][8 : 16] + instructionSegment[wordAddress][0 : 8]
            else:
                blockData += '0' * 32

        if (not(len(instructionCache[insiIndex]) < insAssociativity)):
            for x in instructionCache[insiIndex]:
                y = instructionCache[insiIndex][x]
                if y[1] == 0:
                    if(len(instructionVictimArray[insiIndex])==1):
                        instructionVictimArray[insiIndex].clear()
                    instructionVictimArray[insiIndex][x] = y[0]
                    insVictimiIndex = insiIndex
                    del instructionCache[insiIndex][x]
                    break

        for x in instructionCache[insiIndex]:
            y = instructionCache[insiIndex][x]
            y[1] = y[1] - 1 if y[1] != 0 else 0

        #To Identify Victim block for GUi

        instructionCache[insiIndex][tag] = [blockData, insAssociativity-1]
        insMisses += 1
        return instructionCache[insiIndex][tag][0][iBlockOffset * 8 : (iBlockOffset // 4) * 4 * 8 + 32]



# IR - Fetch and Decode
# Registers required - Fetch_IR,Decode_IR
def fetchInstruction():
    global cPC, BTB, isInBTB, PC, InstructionsExecuted, displayFetch, insFetch
    InstructionsExecuted += 1
    isInBTB = False
    global Fetch_IR, PCtemp, display

    temp_IR1 = list(loadFromInstructionCache("".join(PC)))
    temp_IR = temp_IR1[24 : 32] + temp_IR1[16 : 24] + temp_IR1[8 : 16] + temp_IR1[0 : 8]
    insFetch = "0x" + str(hex(int("".join(PC), 2))[2:].zfill(8))
    for i in range(32):
        Fetch_IR[i] = temp_IR[i]
    displayFetch += "FETCH : Fetch instruction " + "0x" + str(
        hex(int("".join(Fetch_IR), 2))[2:].zfill(8)) + " from address 0x" + str(
        hex(int("".join(PC), 2))[2:].zfill(8)) + "\n"
    PCtemp = dec2two(two2dec(PC) + 4)
    cPC = PC[:]
    if ("".join(PC) in BTB):
        isInBTB = True
        PC = (BTB["".join(PC)])[:]


def bufferFetchDecode():
    global Decode_IR, Fetch_IR, ppppPCtemp, pppPCtemp, ppPCtemp, pPCtemp, PCtemp, ppPC, pPC, cPC
    for i in range(32):
        Decode_IR[i] = Fetch_IR[i]
    ppppPCtemp = pppPCtemp
    pppPCtemp = ppPCtemp
    ppPCtemp = pPCtemp
    pPCtemp = PCtemp

    ppPC = pPC[:]
    pPC = cPC[:]

def staller():
    global numberOfStalls, dataHazzardStalls, dataHazzards,prevPrevPrevIns,prevPrevIns,prevIns
    if((rs1 != "" and rs1 == prevIns[1]) or (rs2 != "" and rs2 == prevIns[1])):
        numberOfStalls += 2
        dataHazzardStalls += 2
        dataHazzards += 1
        addStall(1, '*')
        addStall(1, '*')
        prevPrevPrevIns[1] = prevPrevIns[1]
        prevPrevPrevIns[0] = prevPrevIns[0]
        prevPrevIns[1] = prevIns[1]
        prevPrevIns[0] = prevIns[0]
        prevIns[1] = ""
        prevIns[0] = ""

        prevPrevPrevIns[1] = prevPrevIns[1]
        prevPrevPrevIns[0] = prevPrevIns[0]
        prevPrevIns[1] = prevIns[1]
        prevPrevIns[0] = prevIns[0]
        prevIns[1] = ""
        prevIns[0] = ""

    elif((rs1 != "" and rs1 == prevPrevIns[1]) or (rs2 != "" and rs2 == prevPrevIns[1])):
        numberOfStalls += 1
        dataHazzardStalls += 1
        dataHazzards += 1
        addStall(1, '*')
        prevPrevPrevIns[1] = prevPrevIns[1]
        prevPrevPrevIns[0] = prevPrevIns[0]
        prevPrevIns[1] = prevIns[1]
        prevPrevIns[0] = prevIns[0]
        prevIns[1] = ""
        prevIns[0] = ""

def stallerControl():
    global numberOfStalls, dataHazzardStalls, dataHazzards, isCStall, prevPrevIns, prevPrevPrevIns, prevIns
    if((rs1 != "" and rs1 == prevIns[1]) or (rs2 != "" and rs2 == prevIns[1])):
        numberOfStalls += 2
        dataHazzardStalls += 2
        dataHazzards += 1
        addStall(1, '*')
        addStall(1, '$')
        prevPrevPrevIns[1] = prevPrevIns[1]
        prevPrevPrevIns[0] = prevPrevIns[0]
        prevPrevIns[1] = prevIns[1]
        prevPrevIns[0] = prevIns[0]
        prevIns[1] = ""
        prevIns[0] = ""

        prevPrevPrevIns[1] = prevPrevIns[1]
        prevPrevPrevIns[0] = prevPrevIns[0]
        prevPrevIns[1] = prevIns[1]
        prevPrevIns[0] = prevIns[0]
        prevIns[1] = ""
        prevIns[0] = ""
        isCStall = 1

    elif((rs1 != "" and rs1 == prevPrevIns[1]) or (rs2 != "" and rs2 == prevPrevIns[1])):
        numberOfStalls += 1
        dataHazzardStalls += 1
        dataHazzards += 1
        addStall(1, '$')
        prevPrevPrevIns[1] = prevPrevIns[1]
        prevPrevPrevIns[0] = prevPrevIns[0]
        prevPrevIns[1] = prevIns[1]
        prevPrevIns[0] = prevIns[0]
        prevIns[1] = ""
        prevIns[0] = ""
        isCStall = 1

def hazardDetectionUnitPrevPrev():
    global isDataHazard, rs1, rs2, prevPrevIns, MuxASelect, MuxRMSelect, MuxBSelect, dataHazzards, dataHazzardStalls, prevIns, prevPrevIns, prevPrevPrevIns, curIns
    if (rs1 != ""):
        if (rs1 == prevPrevIns[1] and rs1 != "00000"):
            isDataHazard = 1
            # Both are arithmetic
            # add x11, x12, x13
            # addi x0 x0 0
            # add x14, x11, x16
            # M to E forwarding

            # Previous is arithemtic  and current is load
            # add x14, x11, x16 - x14 is available after execute
            # addi x0 x0 0
            # lw x11, 0(x14) - x14 is required before execute
            # M to E forwarding

            # Previous is arithmetic and current is store
            # add x14, x11, x16 - x14 is available after execute
            # sw x11, 0(x14) - x14 is required before execute
            # E to E forwarding

            if ((prevPrevIns[0] == '0' and curIns[0] == '0') or (prevPrevIns[0] == '0' and curIns[0] == '1') or (
                    prevPrevIns[0] == '0' and curIns[0] == '2')):
                MuxASelect = 3
                dataHazzards += 1

            # Previous is load and current is arithmetic
            # lw x11, 0(x12) x11 is available after memory in RY
            # addi x0 x0 0
            # add x14, x11, x16 - x11 is required in execute
            # W to E ( Hence, No forwarding required)

            # Previous is load and current is load
            # lw x11, 0(x12) x11 is available after memory in RY
            # addi x0 x0 0
            # lw x13, 0(x11) - x11 is required in execute
            # W to E ( Hence, No forwarding required)

            # Previous is load and current is store
            # lw x11, 0(x12) x11 is available after memory in RY
            # addi x0 x0 0
            # sw x13, 0(x11) - x11 is required in execute
            # M to M forwarding
            elif ((prevPrevIns[0] == '1' and curIns[0] == '0') or (prevPrevIns[0] == '1' and curIns[0] == '2') or (
                    prevPrevIns[0] == '1' and curIns[0] == '1')):
                MuxASelect = 3

    if (rs2 != "" and rs2 != rs1):
        if (rs2 == prevPrevIns[1] and rs2 != "00000"):
            isDataHazard = 1
            # Both are arithmetic
            # add x11, x12, x13
            # addi x0 x0 0
            # add x14, x16, x11
            # M to E forwarding

            # Previous is arithmetic and current is store
            # add x14, x11, x16 - x14 is available after execute
            # addi x0 x0 0
            # sw x11, 0(x14) - x14 is required before execute
            # M to E forwarding

            if ((prevPrevIns[0] == '0' and curIns[0] == '0')):
                MuxBSelect = 3
                dataHazzards += 1

            elif ((prevPrevIns[0] == '0' and curIns[0] == '2')):
                MuxRMSelect = 2
                dataHazzards += 1

            elif (prevPrevIns[0] == '1' and curIns[0] == '0'):
                MuxBSelect = 3


def hazardDetectionUnitPrev():
    global isDataHazard,prevIns, prevPrevIns, prevPrevPrevIns, curIns, dataHazzardStalls, dataHazzards, numberOfStalls, MuxASelect, MuxBSelect, isStall, MuxMSelect, dataStallCount, MuxRMSelect, isDependentPrev, stallCount
    isDependentPrev = False
    # E to E
    # M to E
    # M to M
    # load and arithmetic

    # AA - E to E
    # AL - E to E
    # AS - E to E
    # LA - M to E with stalling
    # LL - M to E with stalling
    # LS - M to E with stalling
    # SA - No Stalling
    # SL - No Stalling
    # SS - No Stalling
    if (rs1 != ""):
        if (rs1 == prevIns[1] and rs1 != "00000"):
            isDataHazard = 1
            isDependentPrev = True
            # Both are arithmetic
            # add x11, x12, x13
            # add x14, x11, x16
            # E to E forwarding

            # Previous is arithmetic and current is load
            # add x14, x11, x16 - x14 is available after execute
            # lw x11, 0(x14) - x14 is required before execute
            # E to E forwarding

            # Previous is arithmetic and current is store
            # add x14, x11, x16 - x14 is available after execute
            # sw x11, 0(x14) - x14 is required before execute
            # E to E forwarding

            if ((prevIns[0] == '0' and curIns[0] == '0') or (prevIns[0] == '0' and curIns[0] == '1') or (
                    prevIns[0] == '0' and curIns[0] == '2')):
                MuxASelect = 2
                dataHazzards += 1

            # Previous is load and current is arithmetic
            # lw x11, 0(x12) x11 is available after memory in RY
            # add x14, x11, x16 - x11 is required in execute
            # M to E forwarding, with stalling

            # Previous is load and current is load
            # lw x11, 0(x12) x11 is available after memory in RY
            # lw x13, 0(x11) - x11 is required in execute
            # M to E forwarding with stalling

            # Previous is load and current is store
            # lw x11, 0(x12) x11 is available after memory in RY
            # sw x13, 0(x11) - x11 is required in execute
            # M to E forwarding with stalling

            elif ((prevIns[0] == '1' and curIns[0] == '0') or (prevIns[0] == '1' and curIns[0] == '2') or (
                    prevIns[0] == '1' and curIns[0] == '1')):
                # MuxASelect = 3
                # isStall = True
                dataHazzardStalls += 1
                dataHazzards += 1
                numberOfStalls += 1
                prevPrevPrevIns[1] = prevPrevIns[1]
                prevPrevPrevIns[0] = prevPrevIns[0]
                prevPrevIns[1] = prevIns[1]
                prevPrevIns[0] = prevIns[0]
                prevIns[1] = ""
                prevIns[0] = ""
                addStall(1, '*')

    # AA - E to E
    # AL - Load no rs2
    # AS - E to E
    # LA - M to E with stalling
    # LL - No rs2
    # LS - M to E
    # SA - No Stalling
    # SL - No Stalling
    # SS - No Stalling
    if (rs2 != "" and rs2 != rs1):
        if (rs2 == prevIns[1] and rs2 != "00000"):
            isDataHazard = 1
            isDependentPrev = True
            # Both are arithmetic
            # add x11, x12, x13
            # add x14, x16, x11
            # E to E forwarding

            # Previous is arithmetic and current is store
            # add x14, x11, x16 - x14 is available after execute
            # sw x14, 0(x20) - x14 is required before execute/ Memory
            # E to E forwarding

            if ((prevIns[0] == '0' and curIns[0] == '0')):
                MuxBSelect = 2
                dataHazzards += 1

            elif ((prevIns[0] == '0' and curIns[0] == '2')):
                MuxRMSelect = 1
                dataHazzards += 1

            # Previous is load and current is arithmetic
            # lw x11, 0(x12) x11 is available after memory in RY
            # add x14, x16, x11 - x11 is required in execute
            # M to E forwarding, with stalling
            elif (prevIns[0] == '1' and curIns[0] == '0'):
                # MuxBSelect = 3
                # isStall = True
                dataHazzardStalls += 1
                numberOfStalls += 1
                dataHazzards += 1
                prevPrevPrevIns[1] = prevPrevIns[1]
                prevPrevPrevIns[0] = prevPrevIns[0]
                prevPrevIns[1] = prevIns[1]
                prevPrevIns[0] = prevIns[0]
                prevIns[1] = ""
                prevIns[0] = ""
                addStall(1, '*')

            # Previous is load and current is store
            # lw x11, 0(x12) x11 is available after memory in RY
            # sw x11, 0(x14) - x11 is required in memory
            # M to M forwarding
            elif ((prevIns[0] == '1' and curIns[0] == '2')):
                MuxMSelect = 1
                dataHazzards += 1


def hazardDetectionUnitControlPrevPrevPrev():
    global isDataHazard, dataHazzards, MuxRASelect, MuxRBSelect, prevIns, prevPrevIns, prevPrevPrevIns, curIns
    if (rs1 != ""):
        if (rs1 == prevPrevPrevIns[1] and rs1 != "00000"):
            isDataHazard = 1
            # M To D Forwarding
            if (prevPrevPrevIns[0] == '1'):
                MuxRASelect = 2
                dataHazzards += 1
    if (rs2 != "" and rs1 != rs2):
        if (rs2 == prevPrevPrevIns[1] and rs2 != "00000"):
            isDataHazard = 1
            if (prevPrevPrevIns[0] == '1'):
                MuxRBSelect = 2
                dataHazzards += 1


def hazardDetectionUnitControlPrevPrev():
    global isDataHazard, prevIns, prevPrevIns, prevPrevPrevIns, curIns, dataHazzardStalls, dataHazzards, controlHazzards, numberOfStalls, MuxRASelect, MuxRBSelect, stallCount, controlEDType, isControlStall, controlHazzardStalls
    if (rs1 != ""):
        if (rs1 == prevPrevIns[1] and rs1 != "00000"):
            isDataHazard = 1
            if (prevPrevIns[0] == '0'):
                MuxRASelect = 1
                # E to D forwarding with no stall
                dataHazzards += 1
            elif (prevPrevIns[0] == '1'):
                # M to D forwarding with one stall
                # MuxRASelect = 2
                prevPrevPrevIns[1] = prevPrevIns[1]
                prevPrevPrevIns[0] = prevPrevIns[0]
                prevPrevIns[1] = prevIns[1]
                prevPrevIns[0] = prevIns[0]
                prevIns[1] = ""
                prevIns[0] = ""
                # dataHazzards += 1
                dataHazzardStalls += 1
                numberOfStalls += 1
                addStall(1, '$')
                isControlStall = 1

    if (rs2 != "" and rs2 != rs1):
        if (rs2 == prevPrevIns[1] and rs2 != "00000"):
            isDataHazard = 1
            if (prevPrevIns[0] == '0'):
                MuxRBSelect = 1
                dataHazzards += 1
                # E to D forwarding with no stall
            elif (prevPrevIns[0] == '1'):
                # M to D forwarding with one stall
                # MuxRBSelect = 2
                # dataHazzards += 1
                prevPrevPrevIns[1] = prevPrevIns[1]
                prevPrevPrevIns[0] = prevPrevIns[0]
                prevPrevIns[1] = prevIns[1]
                prevPrevIns[0] = prevIns[0]
                prevIns[1] = ""
                prevIns[0] = ""
                numberOfStalls += 1
                dataHazzardStalls += 1
                addStall(1, '$')
                isControlStall = 1


def hazardDetectionUnitControlPrev():
    global prevIns, prevPrevIns, prevPrevPrevIns, curIns, dataHazzardStalls, dataHazzards, numberOfStalls, isDependentPrev, isControlStall, MuxRASelect, stallCount, MuxRBSelect, controlEDType, controlHazzards, controlHazzardStalls
    isDependentPrev = False
    if (rs1 != ""):
        if (rs1 == prevIns[1] and rs1 != "00000"):
            isDataHazard = 1
            isDependentPrev = True
            if (prevIns[0] == '0'):
                # MuxRASelect = 1
                # E to D forwarding with one stall
                prevPrevPrevIns[1] = prevPrevIns[1]
                prevPrevPrevIns[0] = prevPrevIns[0]
                prevPrevIns[1] = prevIns[1]
                prevPrevIns[0] = prevIns[0]
                prevIns[1] = ""
                prevIns[0] = ""
                numberOfStalls += 1
                dataHazzardStalls += 1
                addStall(1, '$')
                isControlStall = 1
            elif (prevIns[0] == '1'):
                # M to D forwarding with two stalls
                # MuxRASelect = 2
                prevPrevPrevIns[1] = prevPrevIns[1]
                prevPrevPrevIns[0] = prevPrevIns[0]
                prevPrevIns[1] = prevIns[1]
                prevPrevIns[0] = prevIns[0]
                prevIns[1] = ""
                prevIns[0] = ""
                numberOfStalls += 1
                dataHazzardStalls += 1
                addStall(1, '*')
                isControlStall = 1

    if (rs2 != "" and rs2 != rs1):
        if (rs2 == prevIns[1] and rs2 != "00000"):
            isDataHazard = 1
            isDependentPrev = True
            if (prevIns[0] == '0'):
                # MuxRBSelect = 1
                # E to D forwarding with one stall
                prevPrevPrevIns[1] = prevPrevIns[1]
                prevPrevPrevIns[0] = prevPrevIns[0]
                prevPrevIns[1] = prevIns[1]
                prevPrevIns[0] = prevIns[0]
                prevIns[1] = ""
                prevIns[0] = ""
                numberOfStalls += 1
                dataHazzardStalls += 1
                addStall(1, '$')
                isControlStall = 1

            elif (prevIns[0] == '1'):
                # M to D forwarding with two stalls
                # MuxRBSelect = 2
                prevPrevPrevIns[1] = prevPrevIns[1]
                prevPrevPrevIns[0] = prevPrevIns[0]
                prevPrevIns[1] = prevIns[1]
                prevPrevIns[0] = prevIns[0]
                prevIns[1] = ""
                prevIns[0] = ""
                dataHazzardStalls += 1
                numberOfStalls += 1
                addStall(1, '*')
                isControlStall = 1


# Decode - Execute buffers
# RD
# W prevPrevPrevRD
# M prevPrevRD
# E prevRD
# D RD
# nALUop
def decodeInstruction():
    global isDataHazard, isControlHazard, MuxRMSelect, isCStall, flagDataForwarding, controlInstructions, ALUInstructions, dataTransfer, branchType, controlEDType, MuxRASelect, MuxRBSelect, isStall, isControlStall, isDependentPrev, ppMuxYSelect, pMuxYSelect, ppstoreType, pstoreType, nALUop, prevPrevPrevRD, prevPrevRD, prevRD, Decode_IR, MuxASelect, ALUop, rd, rs1, rs2, immediate, MuxBSelect, MuxINCSelect, MuxPCSelect, MuxYSelect, memWrite, memRead, RA, RB, RM, writeRegisterFile, loadType, storeType, isBranch, displayDecode
    isStall = False
    isControlHazard = 0
    isDataHazard = 0
    MuxRMSelect = 0
    controlEDType = 0
    isControlStall = 0
    opCode = "".join(Decode_IR[25:32])
    ALUop = -1
    rd = ""
    rs1 = ""
    rs2 = ""
    immediate = ""
    writeRegisterFile = 0
    MuxASelect = 0
    MuxBSelect = 0  # RB is selected(I-type)
    MuxRASelect = 0
    MuxRBSelect = 0
    MuxINCSelect = 0
    isBranch = 0
    MuxPCSelect = 0
    MuxYSelect = 0  # RZ is selected   1 - MDR is selected  2 - PCtemp is selected
    memWrite = 0
    memRead = 0
    loadType = 0
    storeType = 0
    curIns[0] = '0'
    curIns[1] = ""
    isCStall = 0
    displayDecode += "DECODE : Operation is "
    # R-type instruction
    if (opCode == "0110011"):
        func3 = "".join(Decode_IR[17:20])
        func7 = "".join(Decode_IR[:7])
        if (func3 == "000" and func7 == "0000000"):
            ALUInstructions += 1
            ALUop = 1  # add
            displayDecode += "ADD"
            writeRegisterFile = 1
        elif (func3 == "111" and func7 == "0000000"):
            ALUInstructions += 1
            ALUop = 2  # and
            writeRegisterFile = 1
            displayDecode += "AND"
        elif (func3 == "110" and func7 == "0000000"):
            ALUInstructions += 1
            ALUop = 3  # or
            writeRegisterFile = 1
            displayDecode += "OR"
        elif (func3 == "001" and func7 == "0000000"):
            ALUInstructions += 1
            ALUop = 4  # sll
            writeRegisterFile = 1
            displayDecode += "SLL"
        elif (func3 == "010" and func7 == "0000000"):
            ALUInstructions += 1
            ALUop = 5  # slt
            writeRegisterFile = 1
            displayDecode += "SLT"
        elif (func3 == "101" and func7 == "0100000"):
            ALUInstructions += 1
            ALUop = 6  # sra
            writeRegisterFile = 1
            displayDecode += "SRA"
        elif (func3 == "101" and func7 == "0000000"):
            ALUInstructions += 1
            ALUop = 7  # srl
            writeRegisterFile = 1
            displayDecode += "SRL"
        elif (func3 == "000" and func7 == "0100000"):
            ALUInstructions += 1
            ALUop = 8  # sub
            writeRegisterFile = 1
            displayDecode += "SUB"
        elif (func3 == "100" and func7 == "0000000"):
            ALUInstructions += 1
            ALUop = 9  # xor
            writeRegisterFile = 1
            displayDecode += "XOR"
        elif (func3 == "000" and func7 == "0000001"):
            ALUInstructions += 1
            ALUop = 10  # mul
            writeRegisterFile = 1
            displayDecode += "MUL"
        elif (func3 == "100" and func7 == "0000001"):
            ALUInstructions += 1
            ALUop = 11  # div
            writeRegisterFile = 1
            displayDecode += "DIV"
        elif (func3 == "110" and func7 == "0000001"):
            ALUInstructions += 1
            ALUop = 12  # rem
            writeRegisterFile = 1
            displayDecode += "REM"

    # I-type instruction
    elif (opCode == "0010011"):
        func3 = "".join(Decode_IR[17:20])
        if (func3 == "000"):
            ALUInstructions += 1
            ALUop = 13  # addi
            writeRegisterFile = 1
            MuxBSelect = 1
            displayDecode += "ADDi"
        elif (func3 == "111"):
            ALUInstructions += 1
            ALUop = 14  # andi
            writeRegisterFile = 1
            MuxBSelect = 1
            displayDecode += "ANDi"
        elif (func3 == "110"):
            ALUInstructions += 1
            ALUop = 15  # ori
            writeRegisterFile = 1
            MuxBSelect = 1
            displayDecode += "ORi"

    elif (opCode == "0000011"):
        func3 = "".join(Decode_IR[17:20])
        if (func3 == "000"):
            dataTransfer += 1
            displayDecode += "LB"
            ALUop = 16  # lb
            memRead = 1
            MuxYSelect = 1
            MuxBSelect = 1
            writeRegisterFile = 1
            loadType = 0
            curIns[0] = '1'
        elif (func3 == "001"):
            displayDecode += "LH"
            ALUop = 17  # lh
            dataTransfer += 1
            memRead = 1
            MuxYSelect = 1
            MuxBSelect = 1
            writeRegisterFile = 1
            loadType = 1
            curIns[0] = '1'
        elif (func3 == "010"):
            displayDecode += "LW"
            ALUop = 18  # lw
            dataTransfer += 1
            memRead = 1
            MuxYSelect = 1
            MuxBSelect = 1
            writeRegisterFile = 1
            loadType = 2
            curIns[0] = '1'
    elif (opCode == "1100111"):
        func3 = "".join(Decode_IR[17:20])
        if (func3 == "000"):
            displayDecode += "JALR"
            isControlHazard = 1
            controlInstructions += 1
            ALUop = 19  # jalr
            MuxPCSelect = 1
            MuxYSelect = 2
            MuxBSelect = 1
            MuxINCSelect = 1
            isBranch = 1
            branchType = 2
            writeRegisterFile = 1

    # S-type instruction

    elif (opCode == "0100011"):
        func3 = "".join(Decode_IR[17:20])
        if (func3 == "000"):
            displayDecode += "SB"
            dataTransfer += 1
            MuxBSelect = 1
            memWrite = 1
            ALUop = 20  # sb
            storeType = 0
            curIns[0] = '2'
        elif (func3 == "010"):
            dataTransfer += 1
            displayDecode += "SW"
            MuxBSelect = 1
            memWrite = 1
            ALUop = 21  # sw
            storeType = 2
            curIns[0] = '2'
        elif (func3 == "001"):
            dataTransfer += 1
            displayDecode += "SH"
            MuxBSelect = 1
            memWrite = 1
            ALUop = 22  # sh
            storeType = 1
            curIns[0] = '2'

    # SB-type instruction
    elif (opCode == "1100011"):
        func3 = "".join(Decode_IR[17:20])
        if (func3 == "000"):
            displayDecode += "BEQ"
            isControlHazard = 1
            controlInstructions += 1
            ALUop = 23  # beq
            branchType = 0
            isBranch = 1
        elif (func3 == "001"):
            displayDecode += "BNE"
            isControlHazard = 1
            controlInstructions += 1
            branchType = 0
            ALUop = 24  # bne
            isBranch = 1
        elif (func3 == "101"):
            displayDecode += "BGE"
            isControlHazard = 1
            controlInstructions += 1
            branchType = 0
            ALUop = 25  # bge
            isBranch = 1
        elif (func3 == "100"):
            displayDecode += "BLT"
            isControlHazard = 1
            controlInstructions += 1
            branchType = 0
            ALUop = 26  # blt
            isBranch = 1

    # U-type instruction
    elif (opCode == "0010111"):
        displayDecode += "AUIPC"
        ALUop = 27  # auipc
        MuxASelect = 1
        MuxBSelect = 1
        ALUInstructions += 1
        writeRegisterFile = 1

    elif (opCode == "0110111"):
        displayDecode += "LUI"
        ALUop = 28  # lui
        MuxBSelect = 1
        ALUInstructions += 1
        writeRegisterFile = 1

    # UJ-type instruction
    elif (opCode == "1101111"):
        displayDecode += "JAL"
        isControlHazard = 1
        controlInstructions += 1
        ALUop = 29  # jal
        MuxYSelect = 2
        MuxINCSelect = 1
        isBranch = 1
        branchType = 1
        writeRegisterFile = 1

    if (ALUop != -1):
        # 20 - 26 = No rd, both inclusive
        if (not (ALUop >= 20 and ALUop <= 26)):
            rd = "".join(Decode_IR[20:25])
            curIns[1] = rd
            displayDecode += ", destination register x" + str(int(rd, 2))
            # 27-29 = No rs1
        if (not (ALUop >= 27 and ALUop <= 29)):
            rs1 = "".join(Decode_IR[12:17])
            # RA = registerFile[int(rs1, 2)]
            displayDecode += ", first source register x" + str(int(rs1, 2))

        # 13 - 19   27-29 = No rs2
        if ((ALUop >= 1 and ALUop <= 12) or (ALUop >= 20 and ALUop <= 26)):
            rs2 = "".join(Decode_IR[7:12])
            # RB = registerFile[int(rs2, 2)]
            displayDecode += ", second source register x" + str(int(rs2, 2))

        # I-format
        if (ALUop >= 13 and ALUop <= 19):
            temp = "".join(Decode_IR[:12])
            immediate = temp[0] * (32 - len(temp)) + temp
            displayDecode += ", immediate " + str(hex(int(immediate, 2)))
            # S-format
        elif (ALUop >= 20 and ALUop <= 22):
            temp = "".join(Decode_IR[:7]) + "".join(Decode_IR[20:25])
            immediate = temp[0] * (32 - len(temp)) + temp
            displayDecode += ", immediate " + str(hex(int(immediate, 2)))
            # SB-format
        elif (ALUop >= 23 and ALUop <= 26):
            temp = Decode_IR[0] + Decode_IR[24] + "".join(Decode_IR[1:7]) + "".join(Decode_IR[20:24]) + '0'
            immediate = temp[0] * (32 - len(temp)) + temp
            displayDecode += ", immediate " + str(hex(int(immediate, 2)))
            # U-format
        elif (ALUop == 27 or ALUop == 28):
            immediate = "".join(Decode_IR[:20]) + '0' * 12
            displayDecode += ", immediate " + str(hex(int(immediate, 2)))
            # UJ-format
        elif (ALUop == 29):
            temp = Decode_IR[0] + "".join(Decode_IR[12:20]) + Decode_IR[11] + "".join(Decode_IR[1:11]) + '0'
            immediate = temp[0] * (32 - len(temp)) + temp
            displayDecode += ", immediate " + str(hex(int(immediate, 2)))
        displayDecode += "\n"
    if(flagDataForwarding == '1'):
        if (isBranch == 0):
            if (rs1 != "" and rs2 != "" and rs1 == rs2):
                MuxRBSelect = 3
            hazardDetectionUnitPrev()
            if (prevIns[1] != prevPrevIns[1]):
                hazardDetectionUnitPrevPrev()
            instructionAddressGeneration()
            prevPrevPrevIns[1] = prevPrevIns[1]
            prevPrevPrevIns[0] = prevPrevIns[0]
            prevPrevIns[1] = prevIns[1]
            prevPrevIns[0] = prevIns[0]
            prevIns[1] = curIns[1]
            prevIns[0] = curIns[0]
        else:
            if (rs1 != "" and rs2 != "" and rs1 == rs2):
                MuxRBSelect = 3
            hazardDetectionUnitControlPrev()
            hazardDetectionUnitControlPrevPrev()
            if (prevPrevIns[1] != prevPrevPrevIns[1]):
                hazardDetectionUnitControlPrevPrevPrev()
            if (isControlStall == 0):
                decodeBranchResolution()
            prevPrevPrevIns[1] = prevPrevIns[1]
            prevPrevPrevIns[0] = prevPrevIns[0]
            prevPrevIns[1] = prevIns[1]
            prevPrevIns[0] = prevIns[0]
            prevIns[1] = curIns[1]
            prevIns[0] = curIns[0]
    else:
        if(isBranch == 0):
            MuxRASelect = 0
            MuxRBSelect = 0
            MuxRMSelect = 0
            MuxMSelect = 0
            staller()
            instructionAddressGeneration()
            prevPrevPrevIns[1] = prevPrevIns[1]
            prevPrevPrevIns[0] = prevPrevIns[0]
            prevPrevIns[1] = prevIns[1]
            prevPrevIns[0] = prevIns[0]
            prevIns[1] = curIns[1]
            prevIns[0] = curIns[0]
        else:
            MuxRASelect = 0
            MuxRBSelect = 0
            MuxRMSelect = 0
            MuxMSelect = 0
            stallerControl()
            if (isCStall == 0):
                decodeBranchResolution()
            instructionAddressGeneration()
            prevPrevPrevIns[1] = prevPrevIns[1]
            prevPrevPrevIns[0] = prevPrevIns[0]
            prevPrevIns[1] = prevIns[1]
            prevPrevIns[0] = prevIns[0]
            prevIns[1] = curIns[1]
            prevIns[0] = curIns[0]

def MuxRA():
    global RA, MuxRASelect, RZ, pRY, pRZ
    if (MuxRASelect == 0):
        RA = registerFile[int(rs1, 2)]
    elif (MuxRASelect == 1):
        RA = pRZ[:]
    elif (MuxRASelect == 2):
        RA = RY[:]


def MuxRB():
    global RB, MuxRBSelect, RY, RZ, pRZ, RA
    if (MuxRBSelect == 0):
        RB = registerFile[int(rs2, 2)]
    elif (MuxRBSelect == 1):
        RB = pRZ[:]
    elif (MuxRBSelect == 2):
        RB = RY[:]
    elif (MuxRBSelect == 3):
        RB = RA[:]


# called only for branch instructions
def decodeBranchResolution():
    # Resolution of branches
    global isInBTB, displayDecode, RZ, BTB, flushCount, branchMisprediction, branchType, numberOfStalls, controlHazzardStalls, prevIns, prevPrevIns, prevPrevPrevIns, curIns
    displayDecode += "DECODE : "
    if (rs1 != ""):
        MuxRA()
    if (rs2 != ""):
        MuxRB()
    if (ALUop == 23):
        # Input 4 - 0, Input immediate - 1
        if (two2dec(RA) == two2dec(RB)):
            for i in range(32):
                RZZ[i] = '0'
            RZZ[31] = '1'
        else:
            for i in range(32):
                RZZ[i] = '0'
        displayDecode += "CHECK IF " + str(hex(int("".join(RA), 2))) + " EQUAL TO " + str(hex(int("".join(RB), 2)))
    elif (ALUop == 24):
        if (two2dec(RA) != two2dec(RB)):
            for i in range(32):
                RZZ[i] = '0'
            RZZ[31] = '1'
        else:
            for i in range(32):
                RZZ[i] = '0'
        displayDecode += "CHECK IF " + str(hex(int("".join(RA), 2))) + " NOT EQUAL TO " + str(hex(int("".join(RB), 2)))
    elif (ALUop == 25):
        if (two2dec(RA) >= two2dec(RB)):
            for i in range(32):
                RZZ[i] = '0'
            RZZ[31] = '1'
        else:
            for i in range(32):
                RZZ[i] = '0'
        displayDecode += "CHECK IF " + str(hex(int("".join(RA), 2))) + " GREATER THAN EQUAL TO " + str(
            hex(int("".join(RB), 2)))
    elif (ALUop == 26):
        if (two2dec(RA) < two2dec(RB)):
            for i in range(32):
                RZZ[i] = '0'
            RZZ[31] = '1'
        else:
            for i in range(32):
                RZZ[i] = '0'
        displayDecode += "CHECK IF " + str(hex(int("".join(RA), 2))) + " LESS THAN " + str(hex(int("".join(RB), 2)))
    elif (ALUop == 19 or ALUop == 29):
        for i in range(32):
            RZZ[i] = '0'
        RZZ[31] = '1'
        displayDecode += "Branch is taken"
    if (branchType == 0):
        if (immediate[0] == '1'):
            if (not isInBTB):
                BTB["".join(PC)] = dec2two(two2dec(PC) + two2dec(list(immediate.split())))
                flush()
                prevPrevPrevIns[1] = prevPrevIns[1]
                prevPrevPrevIns[0] = prevPrevIns[0]
                prevPrevIns[1] = prevIns[1]
                prevPrevIns[0] = prevIns[0]
                prevIns[1] = curIns[1]
                prevIns[0] = curIns[0]
                curIns[1] = ""
                curIns[0] = ""
                numberOfStalls += 1
                controlHazzardStalls += 1
                instructionAddressGeneration()
            else:
                # Backward branch, it means our prediction was taken
                if (RZZ[31] == '0'):
                    # miss
                    branchMisprediction += 1
                    instructionAddressGeneration()
                    flush()
                    prevPrevPrevIns[1] = prevPrevIns[1]
                    prevPrevPrevIns[0] = prevPrevIns[0]
                    prevPrevIns[1] = prevIns[1]
                    prevPrevIns[0] = prevIns[0]
                    prevIns[1] = curIns[1]
                    prevIns[0] = curIns[0]
                    curIns[1] = ""
                    curIns[0] = ""
                    controlHazzardStalls += 1
                    numberOfStalls += 1
        else:
            if (not isInBTB):
                BTB["".join(PC)] = dec2two(two2dec(PC) + 4)
                flush()
                prevPrevPrevIns[1] = prevPrevIns[1]
                prevPrevPrevIns[0] = prevPrevIns[0]
                prevPrevIns[1] = prevIns[1]
                prevPrevIns[0] = prevIns[0]
                prevIns[1] = curIns[1]
                prevIns[0] = curIns[0]
                curIns[1] = ""
                curIns[0] = ""
                numberOfStalls += 1
                controlHazzardStalls += 1
                instructionAddressGeneration()
            else:
                # Forward branch, it means our prediction was not taken
                if (RZZ[31] == '1'):
                    branchMisprediction += 1
                    # miss
                    instructionAddressGeneration()
                    flush()
                    prevPrevPrevIns[1] = prevPrevIns[1]
                    prevPrevPrevIns[0] = prevPrevIns[0]
                    prevPrevIns[1] = prevIns[1]
                    prevPrevIns[0] = prevIns[0]
                    prevIns[1] = curIns[1]
                    prevIns[0] = curIns[0]
                    curIns[1] = ""
                    curIns[0] = ""
                    numberOfStalls += 1
                    controlHazzardStalls += 1
    elif (branchType == 1):
        # jal
        if (not isInBTB):
            flush()
            prevPrevPrevIns[1] = prevPrevIns[1]
            prevPrevPrevIns[0] = prevPrevIns[0]
            prevPrevIns[1] = prevIns[1]
            prevPrevIns[0] = prevIns[0]
            prevIns[1] = curIns[1]
            prevIns[0] = curIns[0]
            curIns[1] = ""
            curIns[0] = ""
            numberOfStalls += 1
            controlHazzardStalls += 1
            BTB["".join(pPC)] = instructionAddressGeneration()
    elif (branchType == 2):
        flush()
        prevPrevPrevIns[1] = prevPrevIns[1]
        prevPrevPrevIns[0] = prevPrevIns[0]
        prevPrevIns[1] = prevIns[1]
        prevPrevIns[0] = prevIns[0]
        prevIns[1] = curIns[1]
        prevIns[0] = curIns[0]
        curIns[1] = ""
        curIns[0] = ""
        numberOfStalls += 1
        controlHazzardStalls += 1
        controlHazzardStalls += 1
        instructionAddressGeneration()
    displayDecode += "\n"


def printPipelineDecodeExecute():
    global pppMuxYSelect, ppMuxYSelect, pMuxYSelect, ppstoreType, pstoreType, nALUop, prevPrevPrevRD, prevPrevRD, prevRD, pppwriteRegisterFile, ppwriteRegisterFile, pwriteRegisterFile, pploadType, ploadType, ppmemRead, pmemRead, ppmemWrite, pmemWrite
    print("===================== Inter Stage Buffers Fetch-Decode =====================")

    print("\t\t\tprevPrevPrevRD = ",prevPrevPrevRD,"\tprevPrevRD = ",prevPrevRD,"\tprevRD = ",prevRD)
    print("\t\t\tppwriteRegisterFile = ",ppwriteRegisterFile,"\tppwriteRegisterFile = ",ppwriteRegisterFile ,"\tpwriteRegisterFile = ",pwriteRegisterFile )
    print("\t\t\tpppMuxYSelect = ", pppMuxYSelect, "\tppMuxYSelect = ", ppMuxYSelect, "\tpMuxYSelect = ", pMuxYSelect)
    print("\t\t\tpploadType = ", pploadType, "\tploadType = ", ploadType)
    print("\t\t\tppstoreType = ", ppstoreType, "\tpstoreType = ", pstoreType)
    print("\t\t\tppmemRead = ", ppmemRead, "\tpstoreType = ", memRead)
    print("\t\t\tppmemWrite = ", ppmemWrite, "\tpmemWrite = ", pmemWrite)
    print("\t\t\tnALUop = ", nALUop)


def bufferDecodeExecute():
    global pRY, curIns, prevPrevIns, prevIns, prevPrevPrevIns, pRZ, RZ, pppMuxYSelect, ppMuxYSelect, pMuxYSelect, ppstoreType, pstoreType, nALUop, prevPrevPrevRD, prevPrevRD, prevRD, pppwriteRegisterFile, ppwriteRegisterFile, pwriteRegisterFile, pploadType, ploadType, ppmemRead, pmemRead, ppmemWrite, pmemWrite

    prevPrevPrevRD = prevPrevRD
    prevPrevRD = prevRD
    prevRD = rd

    pppwriteRegisterFile = ppwriteRegisterFile
    ppwriteRegisterFile = pwriteRegisterFile
    pwriteRegisterFile = writeRegisterFile

    pploadType = ploadType
    ploadType = loadType

    ppstoreType = pstoreType
    pstoreType = storeType

    ppmemRead = pmemRead
    pmemRead = memRead

    pppMuxYSelect = ppMuxYSelect
    ppMuxYSelect = pMuxYSelect
    pMuxYSelect = MuxYSelect

    ppmemWrite = pmemWrite
    pmemWrite = memWrite

    nALUop = ALUop
    pRZ = RZ[:]


def MuxA():
    global nRA, RA, ppPC, RZ, RY
    if (MuxASelect == 0):
        nRA = RA[:]
    elif (MuxASelect == 1):
        nRA = ppPC[:]
    elif (MuxASelect == 2):
        nRA = RZ[:]
    elif (MuxASelect == 3):
        nRA = RY[:]


def MuxB():
    global nRB, immediate, RZ, RY, RB, nRA
    if (MuxBSelect == 0):
        nRB = RB[:]
    elif (MuxBSelect == 1):
        for i in range(32):
            nRB[i] = immediate[i]
    elif (MuxBSelect == 2):
        nRB = RZ[:]
    elif (MuxBSelect == 3):
        nRB = RY[:]


def MuxRM():
    global RZ, RY, RB, MuxRMSelect, RM
    if (MuxRMSelect == 0):
        RM = RB[:]
    elif (MuxRMSelect == 1):
        RM = RZ[:]
    elif (MuxRMSelect == 2):
        RM = RY[:]


def executeInstruction():
    global ppPCtemp, RZ, nRZ, nALUop, nRA, nRB, MuxINCSelect, displayExecute, RA, RB, ppPC
    # inputs are RA and nRB
    # output is RZ
    # two2dec takes an array(containing 2's complement binary number) and returns equivalent decimal number.

    if (not (nALUop >= 27 and nALUop <= 29)):
        RA = registerFile[int(rs1, 2)]
    if ((nALUop >= 1 and nALUop <= 12) or (nALUop >= 20 and nALUop <= 26)):
        RB = registerFile[int(rs2, 2)]
    MuxA()
    MuxB()
    MuxRM()

    displayExecute += "EXECUTE : "
    if (nALUop == 1 or nALUop == 13 or (nALUop >= 16 and nALUop <= 18) or (nALUop >= 20 and nALUop <= 22)):
        RZ = dec2two(two2dec(nRA) + two2dec(nRB))
        displayExecute += "ADD " + str(hex(int("".join(nRA), 2))) + " and " + str(hex(int("".join(nRB), 2)))

    elif (nALUop == 2 or nALUop == 14):
        RZ = dec2two(two2dec(nRA) & two2dec(nRB))
        displayExecute += "AND " + str(hex(int("".join(nRA), 2))) + " and " + str(hex(int("".join(nRB), 2)))

    elif (nALUop == 3 or nALUop == 15):
        RZ = dec2two(two2dec(nRA) | two2dec(nRB))
        displayExecute += "OR " + str(hex(int("".join(nRA), 2))) + " and " + str(hex(int("".join(nRB), 2)))

    elif (nALUop == 4):
        RZ = dec2two(two2dec(nRA) << (two2dec(nRB) % 32))
        displayExecute += "SHIFT LOGICAL LEFT " + str(hex(int("".join(nRA), 2))) + " by " + str(
            hex(int("".join(nRB), 2)))

    elif (nALUop == 5):
        if (two2dec(nRA) < two2dec(nRB)):
            for i in range(32):
                RZ[i] = '0'
            RZ[31] = '1'
        else:
            for i in range(32):
                RZ[i] = '0'
        displayExecute += "SET IF " + str(hex(int("".join(nRA), 2))) + " LESS THAN " + str(hex(int("".join(nRB), 2)))
    elif (nALUop == 6):
        # sra
        if (RA[0] == '0'):
            RZ = dec2two(two2dec(nRA) >> (two2dec(nRB) % 32))
        else:
            RZ = dec2two(two2dec(nRA) >> (two2dec(nRB) % 32))

            for i in range(32):
                if (RZ[i] == '1'):
                    break
                else:
                    RZ[i] = '1'
        displayExecute += "SHIFT RIGHT ARITHMETIC " + str(hex(int("".join(nRA), 2))) + " by " + str(
            hex(int("".join(nRB), 2)))
    elif (nALUop == 7):
        RZ = dec2two(two2dec(nRA) >> (two2dec(nRB) % 32))  # srl
        displayExecute += "SHIFT RIGHT LOGICAL " + str(hex(int("".join(nRA), 2))) + " by " + str(
            hex(int("".join(nRB), 2)))
    elif (nALUop == 8):
        RZ = dec2two(two2dec(nRA) - two2dec(nRB))  # sub
        displayExecute += "SUB " + str(hex(int("".join(nRB), 2))) + " from " + str(hex(int("".join(nRA), 2)))
    elif (nALUop == 9):
        RZ = dec2two(two2dec(nRA) ^ two2dec(nRB))  # xor
        displayExecute += "XOR " + str(hex(int("".join(nRA), 2))) + " and " + str(hex(int("".join(nRB), 2)))
    elif (nALUop == 10):
        RZ = dec2two(two2dec(nRA) * two2dec(nRB))  # mul
        displayExecute += "MUL " + str(hex(int("".join(nRA), 2))) + " and " + str(hex(int("".join(nRB), 2)))
    elif (nALUop == 11):
        # Check for division of 0
        RZ = dec2two(two2dec(nRA) / two2dec(nRB))  # div
        displayExecute += "DIV " + str(hex(int("".join(nRA), 2))) + " and " + str(hex(int("".join(nRB), 2)))
    elif (nALUop == 12):
        RZ = dec2two(two2dec(nRA) % two2dec(nRB))  # rem
        displayExecute += "REM " + str(hex(int("".join(nRA), 2))) + " and " + str(hex(int("".join(nRB), 2)))

    elif (nALUop == 27):
        RZ = dec2two(two2dec(nRA) + two2dec(nRB))  # auipc
        displayExecute += "ADD PC = " + str(hex(int("".join(nRA), 2))) + " and " + str(hex(int("".join(nRB), 2)))

    elif (nALUop == 28):
        RZ = nRB[:]
        displayExecute += "FORWARD " + str(hex(int("".join(nRB), 2))) + " to RZ"
    elif (nALUop == 29 or nALUop == 19):
        RZ = ppPCtemp[:]
        displayExecute += "No execute operation"
    else:
        displayExecute += "No execute operation"

    displayExecute += "\n"

def printPipelineExecuteMemory():
    global nRZ
    print("===================== Inter Stage Buffers Execute-Memory =====================")

    print("\t\t\tnRZ = ", "0x" + str(hex(int("".join(nRZ), 2))[2:].zfill(8)))


def bufferExecuteMemory():
    global RZ, nRZ
    nRZ = RZ[:]


def MuxM():
    global MuxMSelect, RY, RM, MDR
    if (MuxMSelect == 0):
        MDR = RM[:]
    elif (MuxMSelect == 1):
        MDR = RY[:]

def loadFromDataCache(addr):
    global dataVictim, dataMisses, dataHits, dataAccess, dataiIndex, dataVictimiIndex
    dataAccess+=1
    dataVictim = (-1,-1)
    dataBlockOffSetSize = int(math.log(dataCacheBlockSize, 2))
    dataIndexSize = int(math.log(dataNoOfSets, 2))
    dataTagSize = len(addr) - dataBlockOffSetSize - dataIndexSize
    blockOffset = addr[dataTagSize + dataIndexSize:]
    iBlockOffset = int(blockOffset, 2)
    index = addr[dataTagSize:dataTagSize + dataIndexSize]
    dataiIndex = int(index, 2)
    tag = addr[0:dataTagSize]
    # 00 - 0   01 - 1   10 - 2  11- 3
    # 0 - 32   32-64    (i * 32 : (i + 1) * 32)
    #Cache contains the block
    if(tag in dataCache[dataiIndex]):
        dataHits += 1
        for x in dataCache[dataiIndex]:
            val = dataCache[dataiIndex][x]
            if x == tag:
                val[1] = dataAssociativity - 1
                flag = True
            else:
                val[1] = val[1] - 1 if val[1] != 0 else 0

        return dataCache[dataiIndex][tag][0][(iBlockOffset//4)*4 * 8 : (iBlockOffset//4)*4*8 + 32]
    else:
        blockAddress = tag + index
        blockData = ""
        for m in range(0,2 ** (dataBlockOffSetSize)):
            tempData = ""
            wordAddress = blockAddress + str(bin(m)[2:]).zfill(dataBlockOffSetSize)
            if(wordAddress in dataSegment):
                blockData += dataSegment[wordAddress]
            else:
                blockData += '0' * 8 + tempData
        # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
        if (not(len(dataCache[dataiIndex]) < dataAssociativity)):
            for x in dataCache[dataiIndex]:
                y = dataCache[dataiIndex][x]
                if y[1] == 0:
                    if (len(dataVictimArray[dataiIndex]) == 1):
                        dataVictimArray[dataiIndex].clear()
                    dataVictimArray[dataiIndex][x] = y[0]
                    dataVictimiIndex = dataiIndex
                    del dataCache[dataiIndex][x]
                    break

        for x in dataCache[dataiIndex]:
            y = dataCache[dataiIndex][x]
            y[1] = y[1] - 1 if y[1] != 0 else 0

        dataCache[dataiIndex][tag] = [blockData, dataAssociativity-1]
        dataMisses += 1
        return dataCache[dataiIndex][tag][0][(iBlockOffset//4)*4 * 8 : (iBlockOffset//4)*4*8 + 32]


def writeIntoDataCache(addr):
    global dataMisses, dataHits, dataAccess,ppstoreType,dataiIndex
    dataAccess+=1
    dataBlockOffSetSize = int(math.log(dataCacheBlockSize, 2))
    dataIndexSize = int(math.log(dataNoOfSets, 2))
    dataTagSize = len(addr) - dataBlockOffSetSize - dataIndexSize
    blockOffset = addr[dataTagSize + dataIndexSize:]
    iBlockOffset = int(blockOffset, 2)
    index = addr[dataTagSize:dataTagSize + dataIndexSize]
    dataiIndex = int(index, 2)
    tag = addr[0:dataTagSize]
    addrIndex =  int((addr),2) % 4
    if(tag in dataCache[dataiIndex]):
        # Hit
        tempDataBlock = ""
        dataHits += 1
        if(ppstoreType == 0):
            tempDataBlock +=  "".join(dataCache[dataiIndex][tag][0][0 : iBlockOffset * 8])
            tempDataBlock += "".join(MDR[24 : 32])
            tempDataBlock +=  "".join(dataCache[dataiIndex][tag][0][iBlockOffset*8 + 8 : ])
        elif(ppstoreType == 1):
            if(addrIndex == 3):
                # Store at last 2 index
                tempDataBlock+= "".join(dataCache[dataiIndex][tag][0][0 : (iBlockOffset - 1) * 8])
                tempDataBlock += "".join(MDR[24 : 32]) + "".join(MDR[16 : 24])
                tempDataBlock +=  "".join(dataCache[dataiIndex][tag][0][(iBlockOffset - 1) * 8 + 16 : ])
            else:
                tempDataBlock +=  "".join(dataCache[dataiIndex][tag][0][0 : iBlockOffset * 8])
                tempDataBlock += "".join(MDR[24 : 32]) + "".join(MDR[16 : 24])
                tempDataBlock += "".join(dataCache[dataiIndex][tag][0][iBlockOffset * 8 + 16 : ])

        elif(ppstoreType == 2):
            tempDataBlock +=  "".join(dataCache[dataiIndex][tag][0][0 : (iBlockOffset//4) * 4 * 8])
            tempDataBlock += "".join(MDR[24 : 32]) + "".join(MDR[16 : 24]) + "".join(MDR[8 : 16]) + "".join(MDR[0 : 8])
            tempDataBlock +=  "".join(dataCache[dataiIndex][tag][0][(iBlockOffset//4) * 4 * 8 + 32 : ])


        dataCache[dataiIndex][tag][0] = tempDataBlock
    else:
        dataMisses +=1


def memoryAccess():
    global MAR, ppmemRead, MDR, RM, nRZ, nnRZ, ppmemWrite, dataSegment, pploadType, ppstoreType, displayMemory
    if (ppmemRead == 1):
        MAR = nRZ[:]
        tempMDR = list(loadFromDataCache("".join(MAR)))
        MDRIndex =  int("".join(MAR),2) % 4
        # 0 1 2 3
        # 3 2
        if(pploadType == 0):
            # lb
            tempMDR2 = tempMDR[MDRIndex*8 : MDRIndex * 8 + 8]
            MDR = [tempMDR2[0] for i in range(24) ] + tempMDR2

        if(pploadType == 1):
            # lh
            if(MDRIndex == 3):
                tempMDR2 = tempMDR[24 : 32] + tempMDR[16 : 24]
            else:
                tempMDR2 = tempMDR[(MDRIndex + 1) * 8 : (MDRIndex + 1) * 8 + 8] + tempMDR[MDRIndex * 8 : MDRIndex * 8 + 8]

            MDR = [tempMDR2[0] for i in range(16) ] + tempMDR2

        if(pploadType == 2):
            MDR = tempMDR[24 : 32] + tempMDR[16 : 24] + tempMDR[8 : 16] + tempMDR[0 : 8]

        displayMemory += "MEMORY : The value 0x" + str(hex(int("".join(MDR), 2)))[2:] + " is loaded from address 0x" + str(hex(int("".join(MAR), 2)))[2:]+"\n"


    elif (ppmemWrite == 1):
        MuxM()
        MAR = nRZ[:]
        writeIntoDataCache("".join(MAR))
        temp_str = "00000000"
        dataSegment["".join(MAR)] = "".join(MDR[24:32])
        displayMemory += "MEMORY : The value 0x" + str(hex(int("".join(MDR[24:32]), 2)))[2:].zfill(
            2) + " is stored at address 0x" + str(hex(int("".join(MAR), 2))[2:].zfill(8)) + "\n"

        if ("".join(MDR[24:32]) == temp_str):
            del dataSegment["".join(MAR)]

        if (ppstoreType == 1 or ppstoreType == 2):
            dataSegment["".join(dec2two(two2dec(MAR) + 1))] = "".join(MDR[16:24])
            displayMemory += "MEMORY : The value 0x" + str(hex(int("".join(MDR[16:24]), 2)))[2:].zfill(
                2) + " is stored at address 0x" + str(
                hex(int("".join(dec2two(two2dec(MAR) + 1)), 2))[2:].zfill(8)) + "\n"
            if ("".join(MDR[16:24]) == temp_str):
                del dataSegment["".join(dec2two(two2dec(MAR) + 1))]

        if (ppstoreType == 2):
            dataSegment["".join(dec2two(two2dec(MAR) + 2))] = "".join(MDR[8:16])
            displayMemory += "MEMORY : The value 0x" + str(hex(int("".join(MDR[8:16]), 2)))[2:].zfill(
                2) + " is stored at address 0x" + str(
                hex(int("".join(dec2two(two2dec(MAR) + 2)), 2))[2:].zfill(8)) + "\n"
            if ("".join(MDR[8:16]) == temp_str):
                del dataSegment["".join(dec2two(two2dec(MAR) + 2))]

            dataSegment["".join(dec2two(two2dec(MAR) + 3))] = "".join(MDR[0:8])
            displayMemory += "MEMORY : The value 0x" + str(hex(int("".join(MDR[0:8]), 2)))[2:].zfill(
                2) + " is stored at address 0x" + str(
                hex(int("".join(dec2two(two2dec(MAR) + 3)), 2))[2:].zfill(8)) + "\n"
            if ("".join(MDR[0:8]) == temp_str):
                del dataSegment["".join(dec2two(two2dec(MAR) + 3))]

    elif (ppmemWrite == 0 and ppmemRead == 0):
        displayMemory += "MEMORY : No memory operation\n"

def printPipelineMemoryRegister():
    global nnRZ
    print("===================== Inter Stage Buffers Memory-Register =====================")
    print("\t\t\tnRZ = ", "0x" + str(hex(int("".join(nnRZ), 2))[2:].zfill(8)))

def bufferMemoryRegister():
    global nnRZ, nRZ
    nnRZ = nRZ[:]


def MuxY():
    global pppMuxYSelect, RY, nRZ, MDR, ppppPCtemp
    if (pppMuxYSelect == 0):
        RY = nnRZ[:]
    elif (pppMuxYSelect == 1):
        RY = MDR[:]
    elif (pppMuxYSelect == 2):
        RY = ppppPCtemp[:]


def registerUpdate():
    global ALUop, RY, registerFile, displayWriteBack, prevPrevPrevRD
    MuxY()
    if (pppwriteRegisterFile == 1):
        displayWriteBack += "WRITEBACK : Write " + str(hex(int("".join(RY), 2))) + " to x" + str(
            int(prevPrevPrevRD, 2)) + "\n"
        if (int(prevPrevPrevRD, 2) != 0):
            registerFile[int(prevPrevPrevRD, 2)] = RY[:]

    else:
        displayWriteBack += "WRITEBACK : No write back operation\n"


def INCAndGate():
    global isBranch, MuxINCSelect, RZZ
    MuxINCSelect = isBranch & int(RZZ[31])


def MuxPC():
    global cPC, PC, RA, MuxPCSelect
    if (MuxPCSelect == 0):
        PC = cPC[:]
    elif (MuxPCSelect == 1):  # jalr
        PC = RA[:]


def MuxINC():
    global MuxINCSelect, nINC, immediate
    if (MuxINCSelect == 0):
        for i in range(32):
            nINC[i] = '0'
        nINC[29] = '1'
    elif (MuxINCSelect == 1):
        for i in range(32):
            nINC[i] = immediate[i]


def instructionAddressGeneration():
    global PC, MuxINCSelect, RZZ, pPC, branchType
    INCAndGate()
    MuxPC()
    MuxINC()
    PC = dec2two(two2dec(PC) + two2dec(nINC))
    return PC[:]


def fileUpdate():
    file = open(file_name, "r+")
    file.truncate()
    for i in sorted(instructionSegment):
        temp = "0x" + str(hex(int(instructionSegment[i], 2)))[2:].zfill(8)
        big_endian = "0x" + temp[8] + temp[9] + temp[6] + temp[7] + temp[4] + temp[5] + temp[2] + temp[3]
        file.write(
            "0x" + str(hex(int(i, 2))[2:].zfill(8)) + " " + big_endian + "\n")

    for i in sorted(dataSegment):
        file.write(
            "0x" + str(hex(int(i, 2))[2:].zfill(8)) + " " + "0x" + str(hex(int(dataSegment[i], 2)))[2:].zfill(2) + "\n")


# def printRegisters():
#  output = open("result.txt", "a+")
#  for i in range(32):
#    output.write("x" + str(i) + " = " + hex(int("".join(registerFile[i]), 2)) + #"\n")
#  output.write("\n")
# main

# addi x7, x0, 1
# add x8, x7, x0

# TotalCycles = 0 # Done
# InstructionsExecuted = 0 # Done
# dataTransfer = 0 # Load Store Done
# ALUInstructions = 0  # Done
# controlInstructions = 0 # Done
# numberOfStalls = 0 # Done
# dataHazzards = 0  # Done
# controlHazzards = 0 # Done
# branchMisprediction = 0 # Done
# dataHazzardStalls = 0 # Done
# controlHazzardStalls = 0 # Done

def terminalPhase2():
    global dataiIndex, dataVictimiIndex, insiIndex, insVictimiIndex, isEnding, copyOfl, copyOfDONE, CPI,isFinalBreak,stepID,calledFromGui,file_name,flagPrintPipelineType, flagPrintPipeline, flagDataForwarding, flagPrintRegisters, pipelinePrintInstruction, displayWriteBack, displayMemory, displayFetch, displayExecute, displayDecode, display, insWriteBack, insMemory, insExecute, insDecode, flagPrintRegisters, controlHazzardStalls, dataHazzardStalls, branchMispredictioncontrolHazzards, dataHazzardsnumberOfStalls, controlInstructions, ALUInstructions, dataTransfer, InstructionsExecuted, TotalCycles, clock, PC, Fetch_IR, display, dataStallCount, stallCount, l, isFirstRowDeleted

    file_name = sys.argv[1]
    if (stepID == 1):
        flag = '1'
        flag2 = '1'
    else:
        flag = '2'
        flag2 = '2'

    if(calledFromGui==0):
        print("Select the configuration in which you wish to run the simulator")
        print("Enter 1 to run step by step")
        print("Enter any other key to run at once")
        flag = input("Enter your choice : ")
        flag2 = '1' if (flag == '1') else '2'

        if (flag == '1'):
            print("Enter 1 to print the values in the register file at the end of each cycle")
            print("Enter any other key to disable this")
            flagPrintRegisters = input("Enter your choice : ")

            print(
                "Do you want to print the values in the pipeline registers?\n Enter 1 for YES or any other key for NO : ")
            flagPrintPipeline = input("Enter your choice : ")

            if (flagPrintPipeline == '1'):
                print("Enter 1 to print the values in the pipeline registers at the end of each cycle")
                print("Enter any other key to print the pipeline registers of a specific instruction")
                flagPrintPipelineType = input("Enter your choice : ")

                if (flagPrintPipelineType != '1'):
                    pipelinePrintInstruction = input(
                        "Enter the PC(in hexadecimal) of the instruction for which you want to print the pipeline registers : ")
                    pipelinePrintInstruction = str(bin(int(pipelinePrintInstruction, 16))[2:]).zfill(32)
                    if (pipelinePrintInstruction not in instructionSegment):
                        print("Instruction with the given PC doesn't exist")
                        quit(0)
                    pipelinePrintInstruction = "0x" + str(hex(int(pipelinePrintInstruction, 2))[2:].zfill(8))


    while (True):
        insiIndex = -1
        dataiIndex = -1
        dataVictimiIndex = -1
        insVictimiIndex = -1
        displayFetch = ""
        displayDecode = ""
        displayExecute = ""
        displayMemory = ""
        displayWriteBack = ""
        display = ""
        clock = clock + 1
        if (isFirstRowDeleted and (not isEnding)):
            addInstruction()

        if l[0] == ['x' for i in range(20)]:
            isFinalBreak = 1
            if (InstructionsExecuted > 1):
                CPI = clock / (InstructionsExecuted - 1)
                CPI = round(CPI,5)
            break
        # everything is x, then break the loop
        if (l[0][0] == '5'):
            registerUpdate()
            insWriteBack = insMemory
        if (l[0][0] == '4' or l[1][0] == '4'):
            insMemory = insExecute
            memoryAccess()
        bufferMemoryRegister()

        if (l[0][0] == '3' or l[1][0] == '3' or l[2][0] == '3'):
            insExecute = insDecode
            executeInstruction()
        bufferExecuteMemory()

        if (l[0][0] == '2' or l[1][0] == '2' or l[2][0] == '2' or l[3][0] == '2'):
            decodeInstruction()
            insDecode = insFetch
        if (l[0][0] == '$' or l[1][0] == '$' or l[2][0] == '$' or l[3][0] == '$'):
            decodeBranchResolution()
        bufferDecodeExecute()

        if (l[0][0] == '1' or l[1][0] == '1' or l[2][0] == '1' or l[3][0] == '1' or l[4][0] == '1'):
            fetchInstruction()
        bufferFetchDecode()

        # if (isFirstRowDeleted and (not isEnding)):
        #     insFetchStore.append(str(insFetch))

        display = displayWriteBack + displayMemory + displayExecute + displayDecode + displayFetch

        if (int("".join(Fetch_IR), 2) == 0):
            isEnding = True
            for i in range(5):
                if '1' == l[i][0]:
                    l[i] = ['x' for i in range(20)]

        # Make everthing after and including this instruction as 'x'

        if (flag == '1' and flag2 == '1'):
            print(display)
            if(flagPrintRegisters == '1'):
                printRegisters()
            if(flagPrintRegisters == '1'):
                if(flagPrintPipelineType == '1'):
                    printPipelineMemoryRegister()
                    printPipelineExecuteMemory()
                    printPipelineDecodeExecute()
                    printPipelineFetchDecode()
                else:
                    if (l[0][0] == '4' or l[1][0] == '4'):
                        if(pipelinePrintInstruction == insMemory):
                            printPipelineMemoryRegister()
                    if (l[0][0] == '3' or l[1][0] == '3' or l[2][0] == '3'):
                        if (pipelinePrintInstruction == insExecute):
                            printPipelineExecuteMemory()
                    if (l[0][0] == '2' or l[1][0] == '2' or l[2][0] == '2' or l[3][0] == '2'):
                        if (pipelinePrintInstruction == insDecode):
                            printPipelineDecodeExecute()
                    if (l[0][0] == '$' or l[1][0] == '$' or l[2][0] == '$' or l[3][0] == '$'):
                        if (pipelinePrintInstruction == insDecode):
                            printPipelineDecodeExecute()

                    if (l[0][0] == '1' or l[1][0] == '1' or l[2][0] == '1' or l[3][0] == '1' or l[4][0] == '1'):
                        if (pipelinePrintInstruction == insFetch):
                            printPipelineFetchDecode()

        copyOfl = [l[i] for i in range(len(l))]
        copyOfDONE = [DONE[i] for i in range(len(DONE))]

        isFirstRowDeleted = nextCycle()
        if(stepID==1 and calledFromGui ==1):
            break
        if(calledFromGui==0):
            if (flag == '1' and flag2 == '1'):
                flag2 = input(
                    "Enter 1 for running the next step\nEnter any other key to run the remaining steps at once\nEnter your choice :")

    if (calledFromGui == 0):
        print("\n--------------------------- Code executed succesfully ---------------------------")
        print("\n============================== Final Register File ==============================\n")
        printAtSimulationEnd()
        fileUpdate()
        print(display)

# terminalPhase2()
