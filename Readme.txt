							Documentation for flatten() function
							====================================
This program implements a flatten() function which takes a N-dimensional nested integer list as input and 
flattens them into a single array list. 



There are 2 files in the folder.
	flattenArray.py  
	test_flatten.py

1. flattenArray.py module:
==========================
	This is the actual python module that has the implementation for flatten() function.
	The flatten() function is entirely implemented in Python without using any built-in commands or functions.
	
	To use the flatten() function in your python program, you need to first import the module as shown below:
			  import flattenArray
	
	Then, you can use the flatten() function by using the flattenArray object as shown below:
			 flattenArray.flatten(list)
		where list indicates the nested integer list as input parameter.
	
	Please refer section.3 for more info about flatten() function.

  
2. test_flatten.py module:
==========================
	This is another python module that has all the sample codes and tests/testcases to 
	validate the flatten() function.
	
	
	This module is primarily used for performing basic unit testing on the flatten() function. 
	This module runs a set of test cases  to run the flatten() function with inputs, covering from 
	simple flat integer list to a huge nested lists with 200 level deep. 
	
	All the test cases will print the input array and the output flattened array (result array)




3. Function Info
#----------------------------------------------------------------------------------------------------#
#                                   Function:  flatten()                                             #
#----------------------------------------------------------------------------------------------------#
# Function Name:  flatten(nestedList)
#   Description:  
#       Takes a n-dimensional  integer list and converts into a flat 1-dimensional array.  
#   Input:     
#       nestedList : a nested list of integer.
#   Returns:
#       result:   A flattened single-dimensional array(list)
#    
# Example:  
#
#       input_array=[[1,2,3, [4,5], 6, [7,8], 9]]
#       result = flatten(input_array)
#
#   The above code takes calls the flatten() function with an input_array as parameter 
#    and stores the flattened array into result.
#   The result list will have [1,2,3,4,5,6,7,8,9] as a flattened list.
#
#----------------------------------------------------------------------------------------------------#

4. Current Implementation:
==========================
    The flatten() implementation takes a N dimensional  integer list(array) as input and process as follows:
	
	For the given N-dimensional array, each element can fall into 2 categories:
		1. either it is an integer, in that case, it is considered as leaf
		2. or a list, in that case it is considered as Node.
	
	The program then flattens the nested list array by traversing through tree deep and collect all the leafes.
	Uses python iterators to save the iterator context into stack as it traverses.
	
	At the end, it will have a flattened array and returns it to the caller.
	
4. Further improvements:
==----==================

A) Improvements over implementation:
	This function has been tested with many different nested lists including a nested list of 300 levels deep. 
	his program worked just fine. 

	•	We can parametrize the level of depth to flatten and control it inside the function, in case of running into 
		any issue with a very deep, highly shallow nested list as input.
	•	As of now, the function will not skip empty any nested [],{} lists. 
		We can modify the flatten() function to skip the empty list if required.
	
	
B) Automation script for comparing results:
	Instead of manually checking the resulted output against expected output for every test case, we can create 
	an automation script that takes the redirected output from the test_flatten.py program and does the compares 
	the output and consolidates the result.

5. Sample Test code
===================

TestCase 002: Sample code to run the flatten() function with flat single dimensional integer list.

	#TestCase 002: Test with a flat 1-dimensional array as input.
	#   Input: a flat array as input
	#   Expected: Same flat array as expected as output without any change
	import flattenArray 
	print("\nTesting with flat 1 dimensional  array")
	a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	print("Input Array: ", a)  
	print("Flattened Array: ", flattenArray.flatten(a))
	

TestCase 006: Testing the flatten() with highly nested lists, at lest 10 levels deep.

	print("\nTesting with highly nested lists, at least 10 levels deep")
	b = []
	for i in range(10):    
	  b = [b, i]
	print("Input Array: ", b)    
	print("Flattened Array: ", flattenArray.flatten(b))
	
Look at the test_flatten.py module for more test cases.


	
	