                                              README
                                             (PHASE-3)
                          ================================================
                          Appending a cache like memory module to Phase 2
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

=> Follow the following sequence of steps:

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

-> PC, Cycle Count, IR, values of the registers(x0-x31) are displayed on the 
terminal as well as shown on the GUI.
-> Total number of clock cycles, instructions executed, CPI value, no. of data transfer instruction executed, no. of ALU instruction executed,
no. of control instruction executed, no of stalls/bubbles in the pipeline, no of data hazards, no of control hazards, no of branch mispredictions, no of stalls
-> Additionally, in this phase Number of accesses, Number of hits, Number of misses
for instruction cache and data cache are also displayed on the terminal as well as shown on the GUI.
Also, entire contents of data cache and instruction cache are displayed on GUI.
-> Moreover, these values will also be shown if the user steps through the code 
one instruction at a time. 

=================================================================
4. How to run

-> python ProjectRunner.py <file_name>.mc (to run the program)
-> Consequently the instructions to further proceed in the program are displayed 

=================================================================
5. List of any libraries to compile and run it
(A) PyQt5 
(B) sys

=================================================================

=========================Phase 2=================================
6. Work split among the team members
Ritik 

	=> Brainstorming, Logic 

	=> Data Hazards
      		- Hazard Detection Unit for Non-Control Instructions 
      		- Hazard Detection Unit for Control Instructions

	=> Control Hazards
      		- Branch Prediction
      		- Branch Resolution

	=> Setting Knobs
      		- Data Forwarding/ No data forwarding
      		- Pipeline Registers
      		- Tracing Pipeline Registers for a particular instruction

	=> Testing 
	=> Debugging
	=> GUI integration 

Piyush

	=> Data Hazards
	      	- Hazard Detection Unit for Non-Control Instructions 
      		- Hazard Detection Unit for Control Instructions

	=> Control Hazards
      		- Branch Prediction
      		- Branch Resolution

	=> Testing 
	=> Debugging
	=> GUI integration 

Anshul
	=> GUI
	=> GUI integration
	=> Logic and Implementation for Flushing
	=> Logic and Implementation for Stalling
	=> Testing

Sakshat
	=> Contributed in Control Hazards
	=> Preparing test cases
	=> Testing
	=> Logic and Implementation for Stalling
	=> Design Document
	=> ReadMe

Kushagra
	=> Preparing test cases
	=> Testing
	=> Logic and Implementation for Flushing
	=> Logic and Implementation for Stalling
	=> Contributed in Data Hazards	
	=> Design Document
	=> ReadMe

=========================Phase 3=================================
6. Work split among the team members
Ritik 
	=> Brainstorming, Logic 
	=> Instruction Cache
	=> Data Cache 
		- Read Operation
		- Write Operation 
	=> Testing 
	=> Debugging
	=> GUI integration 

Piyush
	=> Instruction Cache
	=> Data Cache 
		- Read Operation
		- Write Operation 
	=> Testing 
	=> Debugging  
	=> GUI integration

Anshul
	=> GUI
	=> GUI integration
	=> LRU Policy Implementation
	=> Testing

Sakshat
	=> Instruction Cache 
	=> Design Document
	=> ReadMe

Kushagra
	=> LRU Policy Implementation 
	=> Design Document
	=> ReadMe

=================================================================
7. GUI-what all data is being displayed and how to interpret it

-> 2 buttons are displayed on the GUI: "RUN" and  "STEP"
-> If "RUN" is selected, the complete code is executed and PC, Clock Cycle Count, IR 
are displayed.
-> If "STEP" is selected, you can run the code one instruction at a time and PC, 
Clock Cycle Count, IR are displayed at every step.

# Instruction Segment
-> Displays all the instructions along with their addresses
# Data Segment 
-> Displays all the data along with its address
# Registers
-> Displays the values of all the 31 registers(x0-x31)
#Pipeline
-> Displays the five stage block diagram of the working of the pipeline
highlighting the data and control hazard cases.
#Pipeline Info
-> Displays all the information related to Pipeline -  Total number of clock cycles, Instructions executed, CPI value,
No. of data transfer instruction executed, No. of ALU instruction executed, No. of control instruction executed, 
No. of stalls/bubbles in the pipeline, No of data hazards, No of control hazards, No of branch mispredictions, 
No of stalls, etc.

=> Additions in Phase-3
-> The content of all the sets of both the Instruction cache and data cache
that have non-zero data are displayed on the GUI.
-> For each of Fetch, Load and Store instruction the set that is accessed is displayed by us.
-> Upon a miss, the victim block is highlighted.


------------------------------------------END------------------------------------------------------
