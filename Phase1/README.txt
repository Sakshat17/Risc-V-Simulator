================================================
Functional Simulator for RISCV Processor
================================================
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
-> python GUI.py <input_file_name>.mc (to run the program)
-> Consequently the instructions to further proceed in the program are displayed
-> Two options is given- either to run on the GUI or run on the terminal
-> Enter-"1" to run the GUI or "any other key" to run on the terminal
-> Then two options is provided to proceed:
(A) Enter-"1" to run the code one step at a time   
(B) Run the entire code at once by entering "any other key"
-> If "1" was entered(i.e. step by step execution), press "r" to further run one more step 
or any other key to run the entire code from there.

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
-> PC, Cycle Count, IR, values of the registers(x0-x31) are displayed on the 
terminal as well as shown on the GUI.
-> Additionally, these values will also be shown if the user steps through the code 
one instruction at a time. 

=================================================================
4. How to run

-> python GUI.py <input_file_name>.mc (to run the program)
-> Consequently the instructions to further proceed in the program are displayed 

=================================================================
5. List of any libraries to compile and run it
(A) PyQt5 
(B) sys

=================================================================
6. Work split among the team members
The complete project was made using Replit which is a real time editor that allows multiple users
to work together at the same time like google docs.
All of us worked together in each of the components while being on a meet. No explicit division of work
was made.  

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
