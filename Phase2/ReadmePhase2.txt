==================================================
Functional Simulator for RISCV Processor (Phase-2)
==================================================
TEAM MEMBERS:
1) Anshul Verma - 2019CSB1075
2) Kushagra Aggarwal - 2019CSB1097
3) Piyush Presannan - 2019CSB1106
4) Ritik Garg - 2019CSB1112
5) Sakshat Chahal - 2019CSB1116

README

Table of contents
1. Instructions to the user on how to use it
2. Input format with details
3. Output format with details
4. How to run
5. List of any libraries to compile and run it.
6. Work split among the team members 
7. GUI-what all data is being displayed and how to interpret it.

=================================================================
1. Instructions to the user on how to use it

=> Follow the following sequence of steps:

-> If you want to run pipeline execution run main function Phase2 folder and for non-pipelined execution run main function of Phase1 folder
-> Enter '1' for data forwarding else press any other key for prohibiting data forwarding
-> For step by step execution enter '1' and to run the complete code at once enter any other key. 
-> Enter '1' to print the value of register file at the end of each cycle. 
-> Enter '1' if you want to print the value in pipeline registers 
-> Enter '1' to print the value of pipeline registers at the end of each cycle, and any other key for printing the registers for a specific instruction 
-> If specific instruction is selected for printing registers, enter the PC of the instruction for which you want to print the pipeline register.

=================================================================
2. Input format with details
-> All the instructions in the .mc file which is to be run should be 
in the little endian notation.
-> The instruction segment must always end with the instruction 0x00000000
-> It is assumed that the instructions in the input file are in accordance with the pdf file circulated
for the phase-1 part of the project.
=================================================================
3. Output format with details
-> All the elements are updated in the data segment would be added in the .mc
file given in the input
-> Total number of clock cycles, instructions executed, CPI value, no. of data transfer instruction executed, no. of ALU instruction executed,
no. of control instruction executed, no of stalls/bubbles in the pipeline, no of data hazards, no of control hazards, no of branch mispredictions, no of stalls
due to data hazads, no of stalls due to control hazards, values of all the registers

=================================================================
4. How to run

-> python main.py <file_name>.mc (to run the program)
-> Consequently the instructions to further proceed in the program are displayed 

=================================================================
5. List of any libraries to compile and run it
(A) PyQt5 
(B) sys

=================================================================
6. Work split among the team members
=> Brainstorming Logic - Ritik 
=>Data hazards - Ritik, Piyush, Kushagra
=>Control hazards - Ritik, Piyush, Anshul
=> Decode Branch Resolution - Ritik, Piyush, Sakshat
=> Testing - Sakshat, Kushagra, Ritik, Piyush, Anshul
=> Debugging - Ritik, Piyush
=> Design Doc - Sakshat, Kushagra
=> GUI - Anshul

 

=================================================================
7. GUI-what all data is being displayed and how to interpret it

-> 3 buttons are displayed on the GUI: "RUN", "STEP" and "RESET"
-> If "RUN" is selected, the complete code is executed and PC, Clock Cycle Count, IR 
are displayed.
-> If "STEP" is selected, you can run the code one instruction at a time and PC, 
Clock Cycle Count, IR are displayed at every step.
-> If "RESET" is selected, every data displayed is reset to its initial value as in the beginning
of the code.
# Instruction Segment
-> Displays all the instructions along with their addresses
# Data Segment 
-> Displays all the data along with its address
# Registers
-> Displays the values of all the 31 registers(x0-x31)


------------------------------------------END------------------------------------------------------
