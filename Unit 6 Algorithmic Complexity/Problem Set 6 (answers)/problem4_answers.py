Problem 4-1: Consider the following Python procedure. Specify its order of growth.

def modten(n):
    return n%10
  
Answer: O(1)
  
  
Problem 4-2: Consider the following Python procedure. Specify its order of growth.
  
def multlist(m, n):
    '''
    m is the multiplication factor
    n is a list.
    '''
    result = []
    for i in range(len(n)):
        result.append(m*n[i])
    return result 
  
Answer: O(len(n))
  
