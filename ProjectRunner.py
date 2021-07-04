import sys

if (len(sys.argv) > 2):
    print("Invalid input file, Re-enter File name")
    exit(0)
elif (not (sys.argv[1][-1] == 'c' and sys.argv[1][-2] == 'm' and sys.argv[1][-3] == '.')):
    print("Invalid file format, Re-enter .mc file")
    exit(0)
else:
    try:
        f = open(sys.argv[1], 'r')
    except OSError:
        print("Invalid input file, Re-enter File name")
        exit(0)
    else:
        print("Enter 1 to Enable Pipelining")
        print("Enter any other key to disable Pipelining")
        flagTogglePipelining = input("Enter your choice : ")

        if(flagTogglePipelining!='1'):
            from Phase1 import GUI
        else:
            print("Enter 1 to run Pipeline with Caches")
            print("Enter any other key to run Pipeline without Caches")
            flagIsWithCaches = input("Enter your choice : ")
            if(flagIsWithCaches!='1'):
                from Phase2 import GUI
            else:
                from Phase3 import GUI