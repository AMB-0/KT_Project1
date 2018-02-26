=========================================================================================

					ASSIGNMENT 1 : Knowledge Technologies 		S02/2017

=========================================================================================

StudentName: Andres Medina
StudentID: 	 828936

Program tested in python 2.7.13

-----------------------------------------------------------------------------------------
I. USAGE
-----------------------------------------------------------------------------------------
- To run the program, just use the command:

	python assignment1_medina.py


- The program will then ask for an input parameter regarding the type of execution that
wants to be performed. In this case, "1" stands for baseline test and "0" for the hybrid solution.

E.g. 
	Baseline test? (1: YES ; 0: NO): 



- If the baseline test wants to be executed, then a second parameter is required. In this second parameter
"1" means Global Edit Distance and "0" means Soundex.

E.g. 
	Baseline method? (1: Edit distance ; 0: Soundex): 1  


-----------------------------------------------------------------------------------------
II. OUTPUT
-----------------------------------------------------------------------------------------  

- The program prints the following output:
  
================================================================================================

        Total Words:

                IV: 6251                        OOV: 2178                       NO: 717

================================================================================================

   I.Edit Distance Baseline Test - Toogles Configuration
-------------------------------------------

        -Twitter Abreviation:                                   OFF
        -Soundex Improvement:                                   OFF
        -Most Likely Dictionary:                                OFF

================================================================================================

   II.Evaluation Metrics
----------------------------

        1.Accuracy:                                             70.15 % (5913/8429)
        2.Precision:                                            3.91 % (5913/151233)
        3.Recall:                                               72.8 % (6136/8429)
        4.Execution Time:                                       2403.97 seconds

================================================================================================

Note:  Inside the code it is possible to adjust some toggles for activating different functionalities of the program:
	
	1. Twitter abbreviation: Includes a previous step that uses a dictionary for translating slang words
	This toggle is off when baseline is choosen.
	
	2. Soundex Improvement: If activated, the hybrid solution includes the soundex filter after the levenshtein distance one.
	This toggle is off when baseline is choosen.
	
	3. Most Likely Dictionary: Includes a last step where a dictionary with the most likely words for english is used in order
	to narrow the final hybrid solution subset to a unique candidate for matching.
