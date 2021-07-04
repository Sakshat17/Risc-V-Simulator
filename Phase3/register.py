def assignRegister(registerNum, reqValue):
    temp_assignReg = list(str(bin(int(reqValue, 16))[2:]).zfill(32))
    for i in range(32):
        registerFile[registerNum][i] = temp_assignReg[i]

def printRegisters():
    print("< Cycle Number >", clock)
    print("< PC >", "".join(PC))
    print("< IR >", "".join(IR))
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

    
PC = ['0' for i in range(32)]
IR = ['0' for i in range(32)]
clock = 0

#Creating RegisterFile
registerFile = [['0' for i in range(32)] for j in range(32)]  # 0-based indexing

# Stack Pointer 0x7FFFFFFC
assignRegister(2, "0x7FFFFFFC")