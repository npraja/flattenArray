#----------------------------------------------------------------------------------------------------------------------------------------#
#                                           Function:  flatten()                                                                         #
#----------------------------------------------------------------------------------------------------------------------------------------#
# Function Name:  flatten(nestedList)
#   Description:  
#       Takes a n-dimensional integer list and converts into a flat 1-dimensional array.  
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
#   The above code takes calls the flatten() function with an input_array as parameter and stores the flattened array into result.
#   The result list will have [1,2,3,4,5,6,7,8,9] as a flattened list.
#
#----------------------------------------------------------------------------------------------------------------------------------------#

def flatten(nestedList):
    
    # checkNode() checks if the given element is a Node or Leaf.  
    # Returns iterator for Node and None for Leaf, infinite loop.
    def checkNode(element):  
        try:
            itr = iter(element)
        except TypeError:
            itr = None
        else:
            # Check for infinite loop
            check_itr = iter(element)
            if (len(element) > 0):
                check_element = next(check_itr)
                if (check_element is element):    # cyclic reference. possible infinite loop.
                    itr = None
            else:
                # len(element)<=0 means nothing. so it is a Leaf
                itr = None

        return itr
    
    # Pointer to the nestedList is the root node.
    # Start the node check from ther root node.      
    itr = checkNode(nestedList)

    # initialize the traverse stack as empty.
    itr_stack = []

    # flattened array that will be returned as result
    flatten_array = []
   
    while (itr != None):
        try:
            #get the next element from current sequence
            element = next(itr)
        except StopIteration:
            # End of current level sequence
            # Check stack for untraversed branches
            if len(itr_stack) > 0:
                itr = itr_stack.pop()
            else:
                itr = None
        else:
            # Test element for Leaf/Node
            inner_itr = checkNode(element)
            if (inner_itr == None):
                flatten_array.append(element)  # it is a leaf element. add it to result array
            else:
                itr_stack.append(itr)   # save current context level to stack
                itr = inner_itr         # move down to next iterator sequence

    #returns the result        
    return flatten_array


