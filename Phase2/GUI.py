#MAINWINDOW
#WIDGETWINDOW
#TABWINDOW
#SIMULATORTAB
#SETTINGSTAB
#PIPELINEINFO
#REGISTERBOX, REGISTERS
#INSTRUCTIONBOX, INSTRUCTIONSEGMENT
#STAGEBOX, FETCH, DECODE, MEMORYACCESS, REGISTERUPDATE, LABELS
#BUTTONS, RUN, STEP, RESET, UPLOADFILE, BUTTONTEXT
#CLOCKPCIR, CLOCK, PC, IR

#insFetch 0         1 2 3 4 5 ~0

#iF 4               2 3 4 5 ~0
#iD 0               1 2 3 4 5 ~4

#iF 8               3 4 5 ~0
#iD 4               2 x 3 4 5 ~4
#iE 0               x 1 2 3 4 5 ~8

#iF 8               4 5
#iD 8               x 3 4 5
#iE 4               1 2 3 4 5
#iM 0               x 1 2 3 4 5




from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from . import main

_translate = QtCore.QCoreApplication.translate

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        #INITIALIZING VARIABLES
        self.green = QtGui.QColor(80, 220, 120) #COLOR FOR INSTRUCTIONS
        self.white = QtGui.QColor('white')
        self.yellow = QtGui.QColor(255, 234, 167) #COLOR FOR REGISTERS

        self.resetID = 0
        self.currentInstruction = -1
        self.nextInstruction = 0

        # MAINWINDOW SIZE
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1264, 923)
        mainWindow.setMinimumSize(QtCore.QSize(1264, 923))
        mainWindow.setMaximumSize(QtCore.QSize(1264, 923))

        #COLOR STYLING OF MAINWINDOW
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        mainWindow.setPalette(palette)

        #WIDGETWINDOW
        self.mainWidget = QtWidgets.QWidget(mainWindow)
        self.mainWidget.setObjectName("mainWidget")
        # mainWindow.setCentralWidget(self.mainWidget)

        #######################################################################

        #ADDING TABWINDOW TO WIDGETWINDOW
        self.tabWindow = QtWidgets.QTabWidget(self.mainWidget)
        self.tabWindow.setGeometry(QtCore.QRect(14, 9, 1241, 901))

        #SETTING STYLE FOR TABWINDOW
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tabWindow.setPalette(palette)

        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.tabWindow.setFont(font)

        self.tabWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWindow.setObjectName("tabWindow")

        #MAKING SIMULATORTAB
        self.simulator = QtWidgets.QWidget()
        self.simulator.setObjectName("simulator")
        self.tabWindow.addTab(self.simulator, "")

        # MAKING PIPELINEINFO
        self.pipelineInfo = QtWidgets.QWidget()
        self.pipelineInfo.setObjectName("pipelineInfo")
        self.tabWindow.addTab(self.pipelineInfo, "")

        ###########################REGISTER/PIPELINEINFO ~ SIMULATOR TAB############################

        #MAKING REGISTERPIPELINEINFO TAB

        self.regPipelineInfo = QtWidgets.QTabWidget(self.simulator)
        self.regPipelineInfo.setGeometry(825, 30, 350, 800)

        self.regTab = QtWidgets.QWidget()
        self.regTab.setObjectName("regTab")
        self.regPipelineInfo.addTab(self.regTab, "")

        self.pipelineTab = QtWidgets.QWidget()
        self.pipelineTab.setObjectName("pipelineTab")
        self.regPipelineInfo.addTab(self.pipelineTab, "")

        ###########################REGISTERS ~ SIMULATOR TAB############################
        #MAKING REGISTERS IN REGISTERBOX
        self.registers = QtWidgets.QListWidget(self.regTab)
        self.registers.setAlternatingRowColors(True)
        self.registers.setGeometry(QtCore.QRect(5, 5, 302, 757))
        self.registers.setObjectName("registers")
        for i in range(32):
            item = QtWidgets.QListWidgetItem()
            self.registers.addItem(item)

        ###########################INSTRUCTION SEGMENT ~ SIMULATOR TAB############################

        #MAKING INSTRUCTIONBOX
        self.instructionBox = QtWidgets.QGroupBox(self.simulator)
        self.instructionBox.setGeometry(QtCore.QRect(520, 30, 260, 410))
        self.instructionBox.setAlignment(QtCore.Qt.AlignCenter)
        self.instructionBox.setObjectName("instructionBox")

        #MAKING INSTRUCTIONSEGMENT
        self.instructions = QtWidgets.QListWidget(self.instructionBox)
        self.instructions.setAlternatingRowColors(True)
        self.instructions.setGeometry(QtCore.QRect(5, 30, 250, 371))
        self.instructions.setStyleSheet("QListWidget{}")
        self.instructions.setObjectName("instructions")

        ###########################DATA SEGMENT ~ SIMULATOR TAB############################

        # MAKING DATABOX
        self.dataBox = QtWidgets.QGroupBox(self.simulator)
        self.dataBox.setGeometry(QtCore.QRect(520, 450, 260, 377))
        self.dataBox.setAlignment(QtCore.Qt.AlignCenter)
        self.dataBox.setObjectName("dataBox")

        # MAKING DATASEGMENT
        self.data = QtWidgets.QListWidget(self.dataBox)
        self.data.setAlternatingRowColors(True)
        self.data.setGeometry(QtCore.QRect(5, 30, 250, 340))
        self.data.setObjectName("data")

        ###########################BUTTONS ~ SIMULATOR TAB############################

        #MAKING BUTTONS
        font.setPixelSize(16)

        #RUN
        self.Run = QtWidgets.QPushButton(self.simulator)
        self.Run.setFont(font)
        self.Run.clicked.connect(run)
        self.Run.setGeometry(QtCore.QRect(40, 70, 80, 35))

        #STEP
        self.Step = QtWidgets.QPushButton(self.simulator)
        self.Step.setFont(font)
        self.Step.clicked.connect(step)
        self.Step.setGeometry(QtCore.QRect(160, 70, 80, 35))

        #RESET

        ###########################CC/PC/IR ~ SIMULATOR TAB############################

        #CLOCKPCIR

        #CLOCK
        self.CC = QtWidgets.QLineEdit(self.simulator)
        self.CC.setGeometry(QtCore.QRect(40, 120, 311, 31))
        self.CC.setObjectName("clockCycles")
        self.CC.setReadOnly(True)

        #PC
        self.PC = QtWidgets.QLineEdit(self.simulator)
        self.PC.setGeometry(QtCore.QRect(40, 150, 311, 31))
        self.PC.setObjectName("PC")
        self.PC.setReadOnly(True)

        #IR
        self.IR = QtWidgets.QLineEdit(self.simulator)
        self.IR.setGeometry(QtCore.QRect(40, 180, 311, 31))
        self.IR.setObjectName("IR")
        self.IR.setReadOnly(True)

        ###########################STAGE BOX ~ SIMULATOR TAB############################

        # MAKING STAGES

        # STAGEBOX
        self.stageBox = QtWidgets.QGroupBox(self.simulator)
        self.stageBox.setGeometry(QtCore.QRect(40, 240, 411, 300))
        self.stageBox.setAlignment(QtCore.Qt.AlignCenter)
        self.stageBox.setObjectName("stageBox")

        # FETCH
        self.FETCH = QtWidgets.QLabel(self.stageBox)
        self.FETCH.setGeometry(QtCore.QRect(115, 55, 71, 20))
        self.FETCH.setObjectName("FETCH")

        self.fetch = QtWidgets.QLineEdit(self.stageBox)
        self.fetch.setGeometry(QtCore.QRect(195, 51, 185, 31))
        self.fetch.setObjectName("fetch")
        self.fetch.setReadOnly(True)

        # DECODE
        self.DECODE = QtWidgets.QLabel(self.stageBox)
        self.DECODE.setGeometry(QtCore.QRect(104, 104, 81, 20))
        self.DECODE.setObjectName("DECODE")

        self.decode = QtWidgets.QLineEdit(self.stageBox)
        self.decode.setGeometry(QtCore.QRect(195, 100, 185, 31))
        self.decode.setObjectName("decode")
        self.decode.setReadOnly(True)

        # EXECUTE
        self.EXECUTE = QtWidgets.QLabel(self.stageBox)
        self.EXECUTE.setGeometry(QtCore.QRect(93, 153, 91, 20))
        self.EXECUTE.setObjectName("EXECUTE")

        self.execute = QtWidgets.QLineEdit(self.stageBox)
        self.execute.setGeometry(QtCore.QRect(195, 149, 185, 31))
        self.execute.setObjectName("execute")
        self.execute.setReadOnly(True)

        # MEMORYACCESS
        self.MEMORYACCESS = QtWidgets.QLabel(self.stageBox)
        self.MEMORYACCESS.setGeometry(QtCore.QRect(33, 202, 161, 20))
        self.MEMORYACCESS.setObjectName("MEMORYACCESS")

        self.memoryAccess = QtWidgets.QLineEdit(self.stageBox)
        self.memoryAccess.setGeometry(QtCore.QRect(195, 198, 185, 31))
        self.memoryAccess.setObjectName("memoryAccess")
        self.memoryAccess.setReadOnly(True)

        # REGISTERUPDATE
        self.REGISTERUPDATE = QtWidgets.QLabel(self.stageBox)
        self.REGISTERUPDATE.setGeometry(QtCore.QRect(14, 251, 171, 31))
        self.REGISTERUPDATE.setObjectName("REGISTERUPDATE")

        self.registerUpdate = QtWidgets.QLineEdit(self.stageBox)
        self.registerUpdate.setGeometry(QtCore.QRect(195, 247, 185, 31))
        self.registerUpdate.setObjectName("registerUpdate")
        self.registerUpdate.setReadOnly(True)

        ###########################DISPLAY BOX ~ SIMULATOR TAB############################

        #MAKING DISPLAYOX
        self.displayBox = QtWidgets.QGroupBox(self.simulator)
        self.displayBox.setGeometry(QtCore.QRect(40, 558, 411, 264))
        self.displayBox.setAlignment(QtCore.Qt.AlignCenter)
        self.displayBox.setObjectName("displayBox")

        #MAKING DISPLAY
        self.display = QtWidgets.QTextEdit(self.displayBox)
        self.display.setGeometry(QtCore.QRect(10, 30, 391, 226))
        self.display.setObjectName("display")
        self.display.setReadOnly(True)

        ###########################PIPLINE INFO TAB ~ SIMULATOR TAB############################

        font.setPointSize(9) #Decreasing Font Size

        x = 5 #Starting X of first Label
        y = 10 #Starting Y of first Label
        w = 200 #Width of Label
        h = 35 #Height of Label (and Entry)
        dely = 35 #Gap between Consecutive Labels
        lx = 210 #X Coordinate of Entry (QLineEdit)
        lw = 120 #Width of Entry (QLineEdit)


        #INSTRUCTIONEXECUTED
        self.NOTOTALINSEXEC = QtWidgets.QLabel(self.pipelineTab)
        self.NOTOTALINSEXEC.setGeometry(QtCore.QRect(x, y+0*(dely+h), w, h))
        self.NOTOTALINSEXEC.setObjectName("NOTOTALINSEXEC")
        self.NOTOTALINSEXEC.setFont(font)

        self.noTotalInsExec = QtWidgets.QLineEdit(self.pipelineTab)
        self.noTotalInsExec.setGeometry(QtCore.QRect(lx, y+0*(dely+h), lw, h))
        self.noTotalInsExec.setObjectName("noTotalInsExec")
        self.noTotalInsExec.setReadOnly(True)
        self.noTotalInsExec.setFont(font)

        #CPI
        self.NOCPI = QtWidgets.QLabel(self.pipelineTab)
        self.NOCPI.setGeometry(QtCore.QRect(x, y + 1 * (dely + h), w, h))
        self.NOCPI.setObjectName("NOCPI")
        self.NOCPI.setFont(font)

        self.noCPI = QtWidgets.QLineEdit(self.pipelineTab)
        self.noCPI.setGeometry(QtCore.QRect(lx, y + 1 * (dely + h), lw, h))
        self.noCPI.setObjectName("noCPI")
        self.noCPI.setReadOnly(True)
        self.noCPI.setFont(font)

        #NODATATRANSFER (load store instructions)
        self.NODATATRANSFER = QtWidgets.QLabel(self.pipelineTab)
        self.NODATATRANSFER.setGeometry(QtCore.QRect(x, y + 2 * (dely + h), w, h))
        self.NODATATRANSFER.setObjectName("NODATATRANSFER")
        self.NODATATRANSFER.setFont(font)

        self.noDataTransfer = QtWidgets.QLineEdit(self.pipelineTab)
        self.noDataTransfer.setGeometry(QtCore.QRect(lx, y + 2* (dely + h), lw, h))
        self.noDataTransfer.setObjectName("noDataTransfer")
        self.noDataTransfer.setReadOnly(True)
        self.noDataTransfer.setFont(font)

        #ALU INS EXEC
        self.NOALU = QtWidgets.QLabel(self.pipelineTab)
        self.NOALU.setGeometry(QtCore.QRect(x, y + 3 * (dely + h), w, h))
        self.NOALU.setObjectName("NOALU")
        self.NOALU.setFont(font)

        self.noAlu = QtWidgets.QLineEdit(self.pipelineTab)
        self.noAlu.setGeometry(QtCore.QRect(lx, y + 3 * (dely + h), lw, h))
        self.noAlu.setObjectName("noAlu")
        self.noAlu.setReadOnly(True)
        self.noAlu.setFont(font)

        #CONTROL INS EXEC
        self.NOCONTROLINS = QtWidgets.QLabel(self.pipelineTab)
        self.NOCONTROLINS.setGeometry(QtCore.QRect(x, y + 4 * (dely + h), w, h))
        self.NOCONTROLINS.setObjectName("NOCONTROLINS")
        self.NOCONTROLINS.setFont(font)

        self.noControlIns = QtWidgets.QLineEdit(self.pipelineTab)
        self.noControlIns.setGeometry(QtCore.QRect(lx, y + 4 * (dely + h), lw, h))
        self.noControlIns.setObjectName("noControlIns")
        self.noControlIns.setReadOnly(True)
        self.noControlIns.setFont(font)

        #NOSTALL
        self.NOSTALL = QtWidgets.QLabel(self.pipelineTab)
        self.NOSTALL.setGeometry(QtCore.QRect(x, y + 5 * (dely + h), w, h))
        self.NOSTALL.setObjectName("NOSTALL")
        self.NOSTALL.setFont(font)

        self.noStall = QtWidgets.QLineEdit(self.pipelineTab)
        self.noStall.setGeometry(QtCore.QRect(lx, y + 5 * (dely + h), lw, h))
        self.noStall.setObjectName("noStall")
        self.noStall.setReadOnly(True)
        self.noStall.setFont(font)

        #NODATAHAZARD
        self.NODATAHAZARD = QtWidgets.QLabel(self.pipelineTab)
        self.NODATAHAZARD.setGeometry(QtCore.QRect(x, y + 6 * (dely + h), w, h))
        self.NODATAHAZARD.setObjectName("NODATAHAZARD")
        self.NODATAHAZARD.setFont(font)

        self.noDataHazard = QtWidgets.QLineEdit(self.pipelineTab)
        self.noDataHazard.setGeometry(QtCore.QRect(lx, y + 6 * (dely + h), lw, h))
        self.noDataHazard.setObjectName("noDataHazard")
        self.noDataHazard.setReadOnly(True)
        self.noDataHazard.setFont(font)

        #NOCONTROLHAZARD
        self.NOCONTROLHAZARD = QtWidgets.QLabel(self.pipelineTab)
        self.NOCONTROLHAZARD.setGeometry(QtCore.QRect(x, y + 7 * (dely + h), w, h))
        self.NOCONTROLHAZARD.setObjectName("NOCONTROLHAZARD")
        self.NOCONTROLHAZARD.setFont(font)

        self.noControlHazard = QtWidgets.QLineEdit(self.pipelineTab)
        self.noControlHazard.setGeometry(QtCore.QRect(lx, y + 7 * (dely + h), lw, h))
        self.noControlHazard.setObjectName("noControlHazard")
        self.noControlHazard.setReadOnly(True)
        self.noControlHazard.setFont(font)

        #NOBRANCHMISS
        self.NOBRANCHMISS = QtWidgets.QLabel(self.pipelineTab)
        self.NOBRANCHMISS.setGeometry(QtCore.QRect(x, y + 8 * (dely + h), w, h))
        self.NOBRANCHMISS.setObjectName("NOBRANCHMISS")
        self.NOBRANCHMISS.setFont(font)

        self.noBranchMiss = QtWidgets.QLineEdit(self.pipelineTab)
        self.noBranchMiss.setGeometry(QtCore.QRect(lx, y + 8 * (dely + h), lw, h))
        self.noBranchMiss.setObjectName("noBranchMiss")
        self.noBranchMiss.setReadOnly(True)
        self.noBranchMiss.setFont(font)

        #NOSTALLDATA
        self.NOSTALLDATA = QtWidgets.QLabel(self.pipelineTab)
        self.NOSTALLDATA.setGeometry(QtCore.QRect(x, y + 9 * (dely + h), w, h))
        self.NOSTALLDATA.setObjectName("NOSTALLDATA")
        self.NOSTALLDATA.setFont(font)

        self.noStallData = QtWidgets.QLineEdit(self.pipelineTab)
        self.noStallData.setGeometry(QtCore.QRect(lx, y + 9 * (dely + h), lw, h))
        self.noStallData.setObjectName("noStallData")
        self.noStallData.setReadOnly(True)
        self.noStallData.setFont(font)

        #NOSTALLCONTROL
        self.NOSTALLCONTROL = QtWidgets.QLabel(self.pipelineTab)
        self.NOSTALLCONTROL.setGeometry(QtCore.QRect(x, y + 10 * (dely + h), w, h))
        self.NOSTALLCONTROL.setObjectName("NOSTALLCONTROL")
        self.NOSTALLCONTROL.setFont(font)

        self.noStallControl = QtWidgets.QLineEdit(self.pipelineTab)
        self.noStallControl.setGeometry(QtCore.QRect(lx, y + 10 * (dely + h), lw, h))
        self.noStallControl.setObjectName("noStallControl")
        self.noStallControl.setReadOnly(True)
        self.noStallControl.setFont(font)

        ###########################BUTTONS ~ PIPELINETAB############################

        # MAKING BUTTONS
        font.setPixelSize(16)

        # RUN
        self.Run2 = QtWidgets.QPushButton(self.pipelineInfo)
        self.Run2.setFont(font)
        self.Run2.clicked.connect(run)
        self.Run2.setGeometry(QtCore.QRect(40, 70, 80, 35))

        # STEP
        self.Step2 = QtWidgets.QPushButton(self.pipelineInfo)
        self.Step2.setFont(font)
        self.Step2.clicked.connect(step)
        self.Step2.setGeometry(QtCore.QRect(160, 70, 80, 35))

        # RESET

        ###########################PIPELINE TAB############################

        self.smolBoxColor = "QLabel{background : grey; color : white}"
        self.emptyColor = "QLabel{background : black; color : black};"
        self.fetchColor = "QLabel{background : orange; color : black}"
        self.decodeColor = "QLabel{background : pink; color : black}"
        self.executeColor = "QLabel{background : lightblue; color : black}"
        self.memoryColor = "QLabel{background : lightgreen; color : black}"
        self.writeColor = "QLabel{background : yellow; color : black}"
        self.dataHazardColor = "QLabel{border : 7px solid black; background : purple; color : white}"
        self.controlHazardColor = "QLabel{border : 7px solid black; background : green; color : white}"
        self.bothHazardColor = "QLabel{border : 7px solid black ;background : red; color : white}"

        x = 80
        y = 150
        wid = 130
        hei = 90

        wid2 = 100
        hei2 = 75

        dely = 30
        delx = 30

        gapy = (hei-hei2)//2
        gap2 = 50

        #Big Box (x+2*wid2+delx+gap2+0*(wid+delx), y-gapy+0*(hei2+dely), wid, hei)
        #Smol Box (x+0*(wid2+delx), y+0*(hei2+dely))

        #######SMOLBOXES######
        #FirstRowSmolBox
        self.x11 = QtWidgets.QLabel(self.pipelineInfo)
        self.x11.setGeometry(x+0*(wid2+delx), y+0*(hei2+dely), wid2, hei2)
        self.x11.setObjectName("x11")
        self.x11.setFont(font)
        self.x11.setAlignment(QtCore.Qt.AlignCenter)
        self.x11.setStyleSheet(self.smolBoxColor)

        self.x12 = QtWidgets.QLabel(self.pipelineInfo)
        self.x12.setGeometry(x + 1 * (wid2 + delx), y + 0 * (hei2 + dely), wid2, hei2)
        self.x12.setObjectName("x12")
        self.x12.setFont(font)
        self.x12.setAlignment(QtCore.Qt.AlignCenter)
        self.x12.setStyleSheet(self.smolBoxColor)

        #SecondRowSmolBox
        self.x21 = QtWidgets.QLabel(self.pipelineInfo)
        self.x21.setGeometry(x + 0 * (wid2 + delx), y + 1 * (hei2 + dely), wid2, hei2)
        self.x21.setObjectName("x21")
        self.x21.setFont(font)
        self.x21.setAlignment(QtCore.Qt.AlignCenter)
        self.x21.setStyleSheet(self.smolBoxColor)

        self.x22 = QtWidgets.QLabel(self.pipelineInfo)
        self.x22.setGeometry(x + 1 * (wid2 + delx), y + 1 * (hei2 + dely), wid2, hei2)
        self.x22.setObjectName("x22")
        self.x22.setFont(font)
        self.x22.setAlignment(QtCore.Qt.AlignCenter)
        self.x22.setStyleSheet(self.smolBoxColor)

        #ThirdRowSmolBox
        self.x31 = QtWidgets.QLabel(self.pipelineInfo)
        self.x31.setGeometry(x + 0 * (wid2 + delx), y + 2 * (hei2 + dely), wid2, hei2)
        self.x31.setObjectName("x31")
        self.x31.setFont(font)
        self.x31.setAlignment(QtCore.Qt.AlignCenter)
        self.x31.setStyleSheet(self.smolBoxColor)

        self.x32 = QtWidgets.QLabel(self.pipelineInfo)
        self.x32.setGeometry(x + 1 * (wid2 + delx), y + 2 * (hei2 + dely), wid2, hei2)
        self.x32.setObjectName("x32")
        self.x32.setFont(font)
        self.x32.setAlignment(QtCore.Qt.AlignCenter)
        self.x32.setStyleSheet(self.smolBoxColor)

        #FourthRowSmolBox
        self.x41 = QtWidgets.QLabel(self.pipelineInfo)
        self.x41.setGeometry(x + 0 * (wid2 + delx), y + 3 * (hei2 + dely), wid2, hei2)
        self.x41.setObjectName("x41")
        self.x41.setFont(font)
        self.x41.setAlignment(QtCore.Qt.AlignCenter)
        self.x41.setStyleSheet(self.smolBoxColor)

        self.x42 = QtWidgets.QLabel(self.pipelineInfo)
        self.x42.setGeometry(x + 1 * (wid2 + delx), y + 3 * (hei2 + dely), wid2, hei2)
        self.x42.setObjectName("x42")
        self.x42.setFont(font)
        self.x42.setAlignment(QtCore.Qt.AlignCenter)
        self.x42.setStyleSheet(self.smolBoxColor)

        #FifthRowSmolBox
        self.x51 = QtWidgets.QLabel(self.pipelineInfo)
        self.x51.setGeometry(x + 0 * (wid2 + delx), y + 4 * (hei2 + dely), wid2, hei2)
        self.x51.setObjectName("x51")
        self.x51.setFont(font)
        self.x51.setAlignment(QtCore.Qt.AlignCenter)
        self.x51.setStyleSheet(self.smolBoxColor)

        self.x52 = QtWidgets.QLabel(self.pipelineInfo)
        self.x52.setGeometry(x + 1 * (wid2 + delx), y + 4 * (hei2 + dely), wid2, hei2)
        self.x52.setObjectName("x52")
        self.x52.setFont(font)
        self.x52.setAlignment(QtCore.Qt.AlignCenter)
        self.x52.setStyleSheet(self.smolBoxColor)

        #VERTICAL DIVIER LINE
        self.Vline = QtWidgets.QFrame(self.pipelineInfo)
        self.Vline.setGeometry(QtCore.QRect(x+2*wid2+delx+gap2//2, y, 1, 4*(hei2+dely)+hei2))
        self.Vline.setFrameShape(QtWidgets.QFrame.VLine)
        self.Vline.setObjectName("Vline")



        #######BIGBOXES######

        #FirstRowBigBoxes
        self.f1 = QtWidgets.QLabel(self.pipelineInfo)
        self.f1.setGeometry(x+2*wid2+delx+gap2+0*(wid+delx), y-gapy+0*(hei2+dely), wid, hei)
        self.f1.setObjectName("f1")
        self.f1.setFont(font)
        self.f1.setAlignment(QtCore.Qt.AlignCenter)
        self.f1.setStyleSheet(self.emptyColor)

        self.d1 = QtWidgets.QLabel(self.pipelineInfo)
        self.d1.setGeometry(x + 2 * wid2 + delx + gap2 + 1 * (wid + delx), y - gapy + 0 * (hei2 + dely), wid, hei)
        self.d1.setObjectName("d1")
        self.d1.setFont(font)
        self.d1.setAlignment(QtCore.Qt.AlignCenter)
        self.d1.setStyleSheet(self.emptyColor)

        self.e1 = QtWidgets.QLabel(self.pipelineInfo)
        self.e1.setGeometry(x + 2 * wid2 + delx + gap2 + 2 * (wid + delx), y - gapy + 0 * (hei2 + dely), wid, hei)
        self.e1.setObjectName("e1")
        self.e1.setFont(font)
        self.e1.setAlignment(QtCore.Qt.AlignCenter)
        self.e1.setStyleSheet(self.emptyColor)

        self.m1 = QtWidgets.QLabel(self.pipelineInfo)
        self.m1.setGeometry(x + 2 * wid2 + delx + gap2 + 3 * (wid + delx), y - gapy + 0 * (hei2 + dely), wid, hei)
        self.m1.setObjectName("m1")
        self.m1.setFont(font)
        self.m1.setAlignment(QtCore.Qt.AlignCenter)
        self.m1.setStyleSheet(self.emptyColor)

        self.w1 = QtWidgets.QLabel(self.pipelineInfo)
        self.w1.setGeometry(x + 2 * wid2 + delx + gap2 + 4 * (wid + delx), y - gapy + 0 * (hei2 + dely), wid, hei)
        self.w1.setObjectName("w1")
        self.w1.setFont(font)
        self.w1.setAlignment(QtCore.Qt.AlignCenter)
        self.w1.setStyleSheet(self.emptyColor)

        #SecondRowBigBoxes
        self.f2 = QtWidgets.QLabel(self.pipelineInfo)
        self.f2.setGeometry(x + 2 * wid2 + delx + gap2 + 0 * (wid + delx), y - gapy + 1 * (hei2 + dely), wid, hei)
        self.f2.setObjectName("f2")
        self.f2.setFont(font)
        self.f2.setAlignment(QtCore.Qt.AlignCenter)
        self.f2.setStyleSheet(self.emptyColor)

        self.d2 = QtWidgets.QLabel(self.pipelineInfo)
        self.d2.setGeometry(x + 2 * wid2 + delx + gap2 + 1 * (wid + delx), y - gapy + 1 * (hei2 + dely), wid, hei)
        self.d2.setObjectName("d2")
        self.d2.setFont(font)
        self.d2.setAlignment(QtCore.Qt.AlignCenter)
        self.d2.setStyleSheet(self.emptyColor)

        self.e2 = QtWidgets.QLabel(self.pipelineInfo)
        self.e2.setGeometry(x + 2 * wid2 + delx + gap2 + 2 * (wid + delx), y - gapy + 1 * (hei2 + dely), wid, hei)
        self.e2.setObjectName("e2")
        self.e2.setFont(font)
        self.e2.setAlignment(QtCore.Qt.AlignCenter)
        self.e2.setStyleSheet(self.emptyColor)

        self.m2 = QtWidgets.QLabel(self.pipelineInfo)
        self.m2.setGeometry(x + 2 * wid2 + delx + gap2 + 3 * (wid + delx), y - gapy + 1 * (hei2 + dely), wid, hei)
        self.m2.setObjectName("m2")
        self.m2.setFont(font)
        self.m2.setAlignment(QtCore.Qt.AlignCenter)
        self.m2.setStyleSheet(self.emptyColor)

        self.w2 = QtWidgets.QLabel(self.pipelineInfo)
        self.w2.setGeometry(x + 2 * wid2 + delx + gap2 + 4 * (wid + delx), y - gapy + 1 * (hei2 + dely), wid, hei)
        self.w2.setObjectName("w2")
        self.w2.setFont(font)
        self.w2.setAlignment(QtCore.Qt.AlignCenter)
        self.w2.setStyleSheet(self.emptyColor)

        #ThirdRowBigBoxes
        self.f3 = QtWidgets.QLabel(self.pipelineInfo)
        self.f3.setGeometry(x + 2 * wid2 + delx + gap2 + 0 * (wid + delx), y - gapy + 2 * (hei2 + dely), wid, hei)
        self.f3.setObjectName("f3")
        self.f3.setFont(font)
        self.f3.setAlignment(QtCore.Qt.AlignCenter)
        self.f3.setStyleSheet(self.emptyColor)

        self.d3 = QtWidgets.QLabel(self.pipelineInfo)
        self.d3.setGeometry(x + 2 * wid2 + delx + gap2 + 1 * (wid + delx), y - gapy + 2 * (hei2 + dely), wid, hei)
        self.d3.setObjectName("d3")
        self.d3.setFont(font)
        self.d3.setAlignment(QtCore.Qt.AlignCenter)
        self.d3.setStyleSheet(self.emptyColor)

        self.e3 = QtWidgets.QLabel(self.pipelineInfo)
        self.e3.setGeometry(x + 2 * wid2 + delx + gap2 + 2 * (wid + delx), y - gapy + 2 * (hei2 + dely), wid, hei)
        self.e3.setObjectName("e3")
        self.e3.setFont(font)
        self.e3.setAlignment(QtCore.Qt.AlignCenter)
        self.e3.setStyleSheet(self.emptyColor)

        self.m3 = QtWidgets.QLabel(self.pipelineInfo)
        self.m3.setGeometry(x + 2 * wid2 + delx + gap2 + 3 * (wid + delx), y - gapy + 2 * (hei2 + dely), wid, hei)
        self.m3.setObjectName("m3")
        self.m3.setFont(font)
        self.m3.setAlignment(QtCore.Qt.AlignCenter)
        self.m3.setStyleSheet(self.emptyColor)

        self.w3 = QtWidgets.QLabel(self.pipelineInfo)
        self.w3.setGeometry(x + 2 * wid2 + delx + gap2 + 4 * (wid + delx), y - gapy + 2 * (hei2 + dely), wid, hei)
        self.w3.setObjectName("w3")
        self.w3.setFont(font)
        self.w3.setAlignment(QtCore.Qt.AlignCenter)
        self.w3.setStyleSheet(self.emptyColor)

        #FourthRowBigBoxes
        self.f4 = QtWidgets.QLabel(self.pipelineInfo)
        self.f4.setGeometry(x + 2 * wid2 + delx + gap2 + 0 * (wid + delx), y - gapy + 3 * (hei2 + dely), wid, hei)
        self.f4.setObjectName("f4")
        self.f4.setFont(font)
        self.f4.setAlignment(QtCore.Qt.AlignCenter)
        self.f4.setStyleSheet(self.emptyColor)

        self.d4 = QtWidgets.QLabel(self.pipelineInfo)
        self.d4.setGeometry(x + 2 * wid2 + delx + gap2 + 1 * (wid + delx), y - gapy + 3 * (hei2 + dely), wid, hei)
        self.d4.setObjectName("d4")
        self.d4.setFont(font)
        self.d4.setAlignment(QtCore.Qt.AlignCenter)
        self.d4.setStyleSheet(self.emptyColor)

        self.e4 = QtWidgets.QLabel(self.pipelineInfo)
        self.e4.setGeometry(x + 2 * wid2 + delx + gap2 + 2 * (wid + delx), y - gapy + 3 * (hei2 + dely), wid, hei)
        self.e4.setObjectName("e4")
        self.e4.setFont(font)
        self.e4.setAlignment(QtCore.Qt.AlignCenter)
        self.e4.setStyleSheet(self.emptyColor)

        self.m4 = QtWidgets.QLabel(self.pipelineInfo)
        self.m4.setGeometry(x + 2 * wid2 + delx + gap2 + 3 * (wid + delx), y - gapy + 3 * (hei2 + dely), wid, hei)
        self.m4.setObjectName("m4")
        self.m4.setFont(font)
        self.m4.setAlignment(QtCore.Qt.AlignCenter)
        self.m4.setStyleSheet(self.emptyColor)

        self.w4 = QtWidgets.QLabel(self.pipelineInfo)
        self.w4.setGeometry(x + 2 * wid2 + delx + gap2 + 4 * (wid + delx), y - gapy + 3 * (hei2 + dely), wid, hei)
        self.w4.setObjectName("w4")
        self.w4.setFont(font)
        self.w4.setAlignment(QtCore.Qt.AlignCenter)
        self.w4.setStyleSheet(self.emptyColor)

        #FifthRowBigBoxes
        self.f5 = QtWidgets.QLabel(self.pipelineInfo)
        self.f5.setGeometry(x + 2 * wid2 + delx + gap2 + 0 * (wid + delx), y - gapy + 4 * (hei2 + dely), wid, hei)
        self.f5.setObjectName("f5")
        self.f5.setFont(font)
        self.f5.setAlignment(QtCore.Qt.AlignCenter)
        self.f5.setStyleSheet(self.emptyColor)

        self.d5 = QtWidgets.QLabel(self.pipelineInfo)
        self.d5.setGeometry(x + 2 * wid2 + delx + gap2 + 1 * (wid + delx), y - gapy + 4 * (hei2 + dely), wid, hei)
        self.d5.setObjectName("d5")
        self.d5.setFont(font)
        self.d5.setAlignment(QtCore.Qt.AlignCenter)
        self.d5.setStyleSheet(self.emptyColor)

        self.e5 = QtWidgets.QLabel(self.pipelineInfo)
        self.e5.setGeometry(x + 2 * wid2 + delx + gap2 + 2 * (wid + delx), y - gapy + 4 * (hei2 + dely), wid, hei)
        self.e5.setObjectName("e5")
        self.e5.setFont(font)
        self.e5.setAlignment(QtCore.Qt.AlignCenter)
        self.e5.setStyleSheet(self.emptyColor)

        self.m5 = QtWidgets.QLabel(self.pipelineInfo)
        self.m5.setGeometry(x + 2 * wid2 + delx + gap2 + 3 * (wid + delx), y - gapy + 4 * (hei2 + dely), wid, hei)
        self.m5.setObjectName("m5")
        self.m5.setFont(font)
        self.m5.setAlignment(QtCore.Qt.AlignCenter)
        self.m5.setStyleSheet(self.emptyColor)

        self.w5 = QtWidgets.QLabel(self.pipelineInfo)
        self.w5.setGeometry(x + 2 * wid2 + delx + gap2 + 4 * (wid + delx), y - gapy + 4 * (hei2 + dely), wid, hei)
        self.w5.setObjectName("w5")
        self.w5.setFont(font)
        self.w5.setAlignment(QtCore.Qt.AlignCenter)
        self.w5.setStyleSheet(self.emptyColor)

        self.bigBoxes = [[self.d1, self.e1, self.m1, self.w1],
                         [self.d2, self.e2, self.m2, self.w2],
                         [self.d3, self.e3, self.m3, self.w3],
                         [self.d4, self.e4, self.m4, self.w4],
                         [self.d5, self.e5, self.m5, self.w5]]

        self.smolBoxes = [[self.x11, self.x12, self.f1],
                          [self.x21, self.x22, self.f2],
                          [self.x31, self.x32, self.f3],
                          [self.x41, self.x42, self.f4],
                          [self.x51, self.x52, self.f5]]

        font.setPointSize(9)
        x = 50
        y = 800
        gapx = 0
        dely = 50
        delx = 100
        hei = 50
        wid = 50

        self.DEMOCONTROLBOX = QtWidgets.QLabel(self.pipelineInfo)
        self.DEMOCONTROLBOX.setGeometry(x - gapx, y - dely, 150, hei)

        self.demoControlBox = QtWidgets.QLabel(self.pipelineInfo)
        self.demoControlBox.setGeometry(x, y, wid, hei)
        self.demoControlBox.setFont(font)
        self.demoControlBox.setAlignment(QtCore.Qt.AlignCenter)
        self.demoControlBox.setStyleSheet(self.controlHazardColor)

        self.DEMODATABOX = QtWidgets.QLabel(self.pipelineInfo)
        self.DEMODATABOX.setGeometry(x + (wid + delx) - gapx, y - dely, 150, hei)

        self.demoDataBox = QtWidgets.QLabel(self.pipelineInfo)
        self.demoDataBox.setGeometry(x + (wid + delx), y, wid, hei)
        self.demoDataBox.setFont(font)
        self.demoDataBox.setAlignment(QtCore.Qt.AlignCenter)
        self.demoDataBox.setStyleSheet(self.dataHazardColor)

        self.DEMOBOTHBOX = QtWidgets.QLabel(self.pipelineInfo)
        self.DEMOBOTHBOX.setGeometry(x + 2 * (wid + delx) - gapx, y - dely, 150, hei)

        self.demoBothBox = QtWidgets.QLabel(self.pipelineInfo)
        self.demoBothBox.setGeometry(x + 2 * (wid + delx), y, wid, hei)
        self.demoBothBox.setFont(font)
        self.demoBothBox.setAlignment(QtCore.Qt.AlignCenter)
        self.demoBothBox.setStyleSheet(self.bothHazardColor)

        ###########################INSTRUCTIONCACHE TAB############################


        self.retranslateUi(mainWindow)
        self.tabWindow.setCurrentIndex(0)
        self.updateRegisters()
        QtCore.QMetaObject.connectSlotsByName(mainWindow)


    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate

        #MAINWINDOW
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))

        #TABWINDOW
        self.tabWindow.setTabText(self.tabWindow.indexOf(self.simulator), _translate("mainWindow", "Simulator"))
        self.tabWindow.setTabText(self.tabWindow.indexOf(self.pipelineInfo), _translate("mainWindow", "Pipeline"))

        #REGISTERBOX
        self.regPipelineInfo.setTabText(self.regPipelineInfo.indexOf(self.regTab), _translate("mainWindow", "Registers"))
        self.regPipelineInfo.setTabText(self.regPipelineInfo.indexOf(self.pipelineTab), _translate("mainWindow", "PipelineInfo"))



        #INSTRUCTIONBOX
        self.instructionBox.setTitle(_translate("mainWindow", "InstructionSegment"))

        #DATABOX
        self.dataBox.setTitle(_translate("mainWindow", "DataSegment"))

        #BUTTONTEXT
        self.Run.setText(_translate("mainWindow", "Run"))
        self.Step.setText(_translate("mainWindow", "Step"))
        self.Run2.setText(_translate("mainWindow", "Run"))
        self.Step2.setText(_translate("mainWindow", "Step"))

        #STAGEBOX
        self.stageBox.setTitle(_translate("mainWindow", "STAGES"))

        #LABELS
        self.FETCH.setText(_translate("mainWindow", "Fetch :"))
        self.DECODE.setText(_translate("mainWindow", "Decode :"))
        self.EXECUTE.setText(_translate("mainWindow", "Execute :"))
        self.MEMORYACCESS.setText(_translate("mainWindow", "Memory Access :"))
        self.REGISTERUPDATE.setText(_translate("mainWindow", "Register Update :"))

        #DISPLAYBOX
        self.displayBox.setTitle(_translate("mainWindow", "DISPLAY"))

        #PIPELINEINFO
        self.NOTOTALINSEXEC.setText("Number of Total\nInstructions Executed :")
        self.NOCPI.setText("CPI :")
        self.NODATATRANSFER.setText("Number of Data\nTransfer Instructions :")
        self.NOALU.setText("Number of ALU\nInstructions :")
        self.NOCONTROLINS.setText("Number of Control\nInstructions Executed :")
        self.NOSTALL.setText("Number of Stalls\nin Pipeline :")
        self.NODATAHAZARD.setText("Number of Data\nHazards :")
        self.NOCONTROLHAZARD.setText("Number of Control\nHazards :")
        self.NOBRANCHMISS.setText("Number of Branch\nMispredictions :")
        self.NOSTALLDATA.setText("Number of Stalls due\nto Data Hazards :")
        self.NOSTALLCONTROL.setText("Number of Stalls due\nto Control Hazards :")


        #CLOCKPCIR
        self.CC.setText(_translate("mainWindow", "Clock Cycle :"))
        self.PC.setText(_translate("mainWindow", "PC :"))
        self.IR.setText(_translate("mainWindow", "IR :"))

        self.demoControlBox.setText(_translate("mainWindow", "A"))
        self.demoDataBox.setText(_translate("mainWindow", "A"))
        self.demoBothBox.setText(_translate("mainWindow", "A"))

        self.DEMOCONTROLBOX.setText(_translate("mainWindow", "Control\nHazard"))
        self.DEMODATABOX.setText(_translate("mainWindow", "Data\nHazard"))
        self.DEMOBOTHBOX.setText(_translate("mainWindow", "Control and Data\nHazard"))


    def updateCPI(self):
        global _translate
        self.CC.setText("Clock Cycle : " + str(main.clock) if self.resetID!=1 else "Clock Cycle :")
        self.PC.setText("PC : 0x" + str(hex(int("".join(main.PC), 2))[2:]).upper().zfill(8) if self.resetID!=1 else "PC :")
        self.IR.setText("IR : 0x" + str(hex(int("".join(main.Fetch_IR), 2))[2:]).upper().zfill(8) if self.resetID!=1 else "IR :")

    def updatePipelineInfo(self):
        self.noTotalInsExec.setText(str(main.InstructionsExecuted) if self.resetID!=1 else "")
        self.noCPI.setText((str(main.CPI) if self.resetID!=1 else "")if main.CPI!=0 else "" )
        self.noDataTransfer.setText(str(main.dataTransfer) if self.resetID!=1 else "")
        self.noAlu.setText(str(main.ALUInstructions) if self.resetID!=1 else "")
        self.noControlIns.setText(str(main.controlInstructions if self.resetID!=1 else ""))
        self.noStall.setText(str(main.numberOfStalls) if self.resetID!=1 else "")
        self.noDataHazard.setText(str(main.dataHazzards) if self.resetID!=1 else "")
        self.noControlHazard.setText(str(main.controlHazzards) if self.resetID!=1 else "")
        self.noBranchMiss.setText(str(main.branchMisprediction) if self.resetID!=1 else "")
        self.noStallData.setText(str(main.dataHazzardStalls) if self.resetID!=1 else "")
        self.noStallControl.setText(str(main.controlHazzardStalls) if self.resetID!=1 else "")

    def updateRegisters(self):
        global _translate
        for i in range(32):
            item = self.registers.item(i)
            item.setText(_translate("Simulator", "x"+str(i)+("  " if i<10 else " ")+": 0x"+str(hex(int("".join(main.registerFile[i]), 2))[2:]).upper().zfill(8)))


    def updateInstructions(self):
        global _translate
        self.instructions.clear()
        i = 0
        for key, val in main.instructionSegment.items():
            item = QtWidgets.QListWidgetItem()
            self.instructions.addItem(item)
            item.setText(_translate("Simulator", "0x"+str(hex(int(key, 2)))[2:].upper()+" "+"0x"+str(hex(int(val, 2)))[2:].upper().zfill(8)))


    def updateData(self):
        global _translate
        self.data.clear()
        for key in sorted(main.dataSegment):
            val = main.dataSegment[key]
            item = QtWidgets.QListWidgetItem()
            self.data.addItem(item)
            item.setText(_translate("Simulator", "0x"+str(hex(int(key, 2)))[2:].upper()+" "+"0x"+str(hex(int(val, 2)))[2:].upper().zfill(2)))

    def updateBoxes(self):
        # Updating Color/Text of BigBoxes
        if (self.resetID == 1):
            for i in range(5):
                for j in range(4):
                    box = self.bigBoxes[i][j]
                    box.setText("")
                    box.setStyleSheet(self.emptyColor)

            for i in range(5):
                for j in range(3):
                    box = self.smolBoxes[i][j]
                    box.setText("")
                    if (j == 2):
                        box.setStyleSheet(self.emptyColor)
                    else:
                        box.setStyleSheet(self.smolBoxColor)

        else:
            for i in range(5):
                for j in range(4):
                    box = self.bigBoxes[i][j]
                    if (main.copyOfl[i][j] == '1'):
                        box.setStyleSheet(self.fetchColor)
                        box.setText("FETCH\n")
                    elif (main.copyOfl[i][j] == '2' or main.copyOfl[i][j] == '$'):
                        box.setStyleSheet(self.decodeColor)
                        box.setText("DECODE\n")
                    elif (main.copyOfl[i][j] == '3'):
                        box.setStyleSheet(self.executeColor)
                        box.setText("EXECUTE\n")
                    elif (main.copyOfl[i][j] == '4'):
                        box.setStyleSheet(self.memoryColor)
                        box.setText("MEMORY\nACCESS")
                    elif (main.copyOfl[i][j] == '5'):
                        box.setStyleSheet(self.writeColor)
                        box.setText("WRITE\nBACK")
                    else:
                        box.setStyleSheet(self.emptyColor)
                        box.setText("")

            # Updating Text of Smol Boxes
            for i in range(5):
                for j in range(3):
                    box = self.smolBoxes[i][j]
                    if (main.copyOfDONE[i][j] == '1'):
                        box.setText("FETCH\n" + main.insFetch if j == 2 else "FETCH")
                        box.setStyleSheet(self.fetchColor if j == 2 else self.smolBoxColor)
                    elif (main.copyOfDONE[i][j] == '2' or main.copyOfDONE[i][j] == '$'):
                        box.setText("DECODE\n" + main.insDecode if j == 2 else "DECODE")
                        if (main.isControlHazard == 1 and main.isDataHazard == 1 and j == 2):
                            box.setStyleSheet(self.bothHazardColor)
                        elif (main.isControlHazard == 1 and j == 2):
                            box.setStyleSheet(self.controlHazardColor)
                        elif (main.isDataHazard == 1 and j == 2):
                            box.setStyleSheet(self.dataHazardColor)
                        else:
                            box.setStyleSheet(self.decodeColor if j == 2 else self.smolBoxColor)
                    elif (main.copyOfDONE[i][j] == '3'):
                        box.setText("EXECUTE\n" + main.insExecute if j == 2 else "EXECUTE")
                        box.setStyleSheet(self.executeColor if j == 2 else self.smolBoxColor)
                    elif (main.copyOfDONE[i][j] == '4'):
                        box.setText("MEMORY\nACCESS\n" + main.insMemory if j == 2 else "MEMORY\nACCESS")
                        box.setStyleSheet(self.memoryColor if j == 2 else self.smolBoxColor)
                    elif (main.copyOfDONE[i][j] == '5'):
                        box.setText("WRITE\nBACK\n" + main.insWriteBack if j == 2 else "WRITE\nBACK")
                        box.setStyleSheet(self.writeColor if j == 2 else self.smolBoxColor)
                    else:
                        if (j == 2):
                            box.setStyleSheet(self.emptyColor)
                        box.setText("")

    def updateInstructionColor(self):
        self.nextInstruction = main.two2dec(main.PC) // 4

        if (main.stepID == 0):
            self.instructions.item(self.instructions.count() - 1).setBackground(self.green)
        elif self.resetID == 1:
            pass
        else:
            item = self.instructions.item(self.nextInstruction)
            item.setBackground(self.green)

        if (self.currentInstruction != -1):
            item = self.instructions.item(self.currentInstruction)
            item.setBackground(self.white)

        if (self.nextInstruction != 0):
            self.currentInstruction = self.nextInstruction

    def updateStages(self):
        if(self.resetID==0):
            self.fetch.setText(main.insFetch if main.displayFetch!="" else "")
            self.decode.setText(main.insDecode if main.displayDecode!="" else "")
            self.execute.setText(main.insExecute if main.displayExecute!="" else "")
            self.memoryAccess.setText(main.insMemory if main.displayMemory!="" else "")
            self.registerUpdate.setText(main.insWriteBack if main.displayWriteBack!="" else "")
        else:
            self.fetch.setText("")
            self.decode.setText("")
            self.execute.setText("")
            self.memoryAccess.setText("")
            self.registerUpdate.setText("")

    def disableButtons(self):
        self.Run.setDisabled(True)
        self.Run2.setDisabled(True)
        self.Step.setDisabled(True)
        self.Step2.setDisabled(True)

    def updateDisplay(self):
        self.display.setText(main.display if self.resetID!=1 else "")

    def updateEverything(self):
        self.updateCPI()
        self.updatePipelineInfo()
        self.updateRegisters()
        self.updateInstructions()
        if(main.displayFetch!=""):
            self.updateInstructionColor()
        self.updateData()
        self.updateStages()
        self.updateBoxes()
        if(main.stepID == 0):
            self.disableButtons()
        self.updateDisplay()

def run():
    global ui
    main.stepID = 0
    main.terminalPhase2()
    ui.updateEverything()
    main.fileUpdate()

def reset():
    global ui
    ui.resetID = 1
    main.resetSimulator()
    ui.updateEverything()
    ui.resetID = 0

def step():
    global ui
    main.stepID = 1
    main.terminalPhase2()
    if(main.isFinalBreak==1):
        main.stepID = 0
        main.fileUpdate()
    ui.updateEverything()



def gui():
    global ui
    main.calledFromGui = 1

    app = QtWidgets.QApplication(sys.argv)
    Simulator = QtWidgets.QDialog()
    ui.setupUi(Simulator)
    Simulator.show()
    ui.updateEverything()

    sys.exit(app.exec_())

ui = Ui_mainWindow()


main.file_name = sys.argv[1]
main.loadDataSegment()
main.loadInstructionSegment()

print("Enter 1 to enable Data Forwarding")
print("Enter any other key to disable Data Forwarding")
main.flagDataForwarding = input("Enter your choice : ")

print("Enter 1 to run GUI")
print("Enter any other key to run on terminal")
main.calledFromGui = int(input("Enter your choice : "))

if(main.calledFromGui==1):
    gui()
else:
    main.calledFromGui=0
    main.terminalPhase2()
