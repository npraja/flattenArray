# This is another python module that has all the sample codes and tests/testcases to validate the flatten() function.
# 	
# This module is primarily used for performing basic unit testing on the flatten() function. 
# This module runs a set of test cases  to run the flatten() function with inputs, covering from 
# simple flat integer list to a huge nested lists with 200 level deep. 
#
# All the test cases will print the input array and the output flattened array (result array)

# To use the flatten() function in a python program, flattenArray.py module needs to be imported as shown below:
import flattenArray

#TestCase 001: Test with an empty array as input
#   Input: [] as empty array
#   Expected output: [] as empty
#
print("\nTesting with empty integer array")
a=[]
print("Input Array: ", a)
result  = flattenArray.flatten(a)     
print("Flattened Array: ", result)

#TestCase 002: Test with a flat 1-dimensional array as input.
#   Input: a flat array as input
#   Expected: Same flat array as expected as output without any change
print("\nTesting with flat 1 dimensional array")
a= [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Input Array: ", a)  
result  = flattenArray.flatten(a)      
print("Flattened Array: ", result)

#TestCase 003: Test with nested array as input (1 level deep)
#   Input: a nested array as input
#   Expected: flattened array as output without any change in order
print("\nTesting with nested 2-dimensional array")
a= [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
print("Input Array: ", a)  
result  = flattenArray.flatten(a)      
print("Flattened Array: ", result)

#TestCase 004: Test with nested array (3 dimensional)
#   Input: a nested array as input
#   Expected: flattened array as output without any change in order
print("\nTesting with nested array ( few level deep array)")
a=[1, 2, [3, [4, 5]], 6]
print("Input Array: ", a)
result=flattenArray.flatten(a)
print("Flattend Array: ", result)

a=[[[3,[5,[6]]]]]
print("\nInput Array: ", a)
result=flattenArray.flatten(a)
print("Flattend Array: ", result)

#TestCase 005: Test with nested array as input (1 level deep)
#   Input: a nested array as input
#   Expected: flattened array as output without any change in order
print("\nTesting with nested with empty list, consequtive list closures")
a=[1, 2, [3, [4, 5]], 6, '', { }, [], 7]
print("Input Array: ", a)
result=flattenArray.flatten(a)
print("Flattend Array: ", result)

a= [1, 2, [3, [4, 5]], 6]
print("\nInput Array: ", a)
result=flattenArray.flatten(a)
print("Flattend Array: ", result)

a = [[[[[1, 2]]]], 3]
print("\nInput Array: ", a)
result=flattenArray.flatten(a)
print("Flattend Array: ", result)

#TestCase 006: Testing the flatten() with higly nested lists, atlest 10 levels deep.
#
print("\nTesting with highly nested lists, atleast 10 levels deep")
#code that prepares a nested list with 10 levels deep
b = []
for i in range(10):    
  b = [b, i]

print("Input Array: ", b)
result  = flattenArray.flatten(b)       
print("Flattened Array: ", result)

#TestCase 007: Testing the flatten() with higly nested lists, atlest 50 levels deep.
#
print("\nTesting with highly nested lists, atleast 50 levels deep")
#code that prepares a nested list with 10 levels deep
b = []
for i in range(50):    
  b = [b, i, i+1]

print("Input Array: ", b)
result  = flattenArray.flatten(b)       
print("Flattened Array: ", result)

#TestCase 007: Testing the flatten() with higly nested lists, atlest 50 levels deep.
#
print("\nTesting with highly nested lists, atleast 200 levels deep")
#code that prepares a nested list with 10 levels deep
b = []
for i in range(200):    
  b = [b, i, i+1]

print("Input Array: ", b)
result  = flattenArray.flatten(b)       
print("Flattened Array: ", result)

#TestCase 008:  Test with a huge nested list with more than 20 depth level of reduntant data.
#   Input: huge nested list
#   Expected: a single flattened array without any change in the order.
#   
print("\nTesting with huge nested list with 20 levels deep with reduntant data")
#prepare input
hugelist = [1, [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
[2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1,
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]],1, 
 [2,23,[331,[3, 4,[3, [3, 4, [5, 6]],4, [5, 6]], [5, 6]],332], [3, 4, [5, 6]], 7, 8, [9, [10]]]] 

print("Input Array: ", hugelist)
result  = flattenArray.flatten(hugelist)         
print("Flattened Array: ", result)


