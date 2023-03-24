# Problem 4-1: Consider the following Python procedure. Specify its order of growth.

def modten(n):
    return n%10
  
# --> Answer: O(1)

#------------------------------------------------  
#------------------------------------------------  

# Problem 4-2: Consider the following Python procedure. Specify its order of growth.

def multlist(m, n):
    '''
    m is the multiplication factor
    n is a list.
    '''
    result = []
    for i in range(len(n)):
        result.append(m*n[i])
    return result 

# --> Answer: O(len(n))

#------------------------------------------------  
#------------------------------------------------

# Problem 4-3: Consider the following Python procedure. Specify its order of growth.

def foo(n):
    if n <= 1:
        return 1
    return foo(n/2) + 1 

# --> Answer: O(log(n))

#------------------------------------------------  
#------------------------------------------------

# Problem 4-4: Consider the following Python procedure. Specify its order of growth.

def recur(n):
    if n <= 0:
        return 1
    else:
        return n*recur(n-1)

# --> Answer: O(n)

#------------------------------------------------  
#------------------------------------------------

# Problem 4-5: Consider the following Python procedure. Specify its order of growth.

def baz(n):
    for i in range(n):
        for j in range(n):
            print( i,j )

# --> Answer: O(n^2)
  
