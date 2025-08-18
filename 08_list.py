# List in Python : List are container to store a set of values of any data type

# LIST METHODS

L1=[25,1,5,8,96,45,75]

L1.sort()       # Sorted the list
print(L1)

L1.reverse()    # Reverse the list
print(L1)    

L1.append(154)   # Add the element at the end of the list
print(L1)

L1.insert(3,6)   # This will add 6 at 3 index
print(L1)      

L1.pop(2)        # Will delete element at index 2 and return its value
print(L1)       

L1.remove(154)    # Will remove 154 from the list
print(L1)        

L1[0]=2           # Replace the value at index 0
print(L1)

L2=[54,75,85,2,65,8,63]
L3=L1+L2            # Add two List
print(L3)

L4=L1*3
print(L4)          # Repeating the list


