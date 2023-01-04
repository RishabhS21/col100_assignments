import sys  # imported sys to use sys.exit
# this function check whether there is a tuple with 1st argument x in the list L or not
def istuple(L,x):
    n=len(L)
    find=False
    i=0
    while i<n and not find:
        if type(L[i]) is tuple: # if element at i index is tuple 
            (a,b)=L[i]
            if a == x:          # if 1st element of tuple is x
                find=True
                return find,i   # return True and index of tuple
        i+=1
    return False                # otherwise return false, O(n)

# this function check whether there is an element k in the list L or not
def found(L,k):
    n=len(L)
    find=False
    i=0
    while i<n and not find:
        if L[i]==k:
            find=True
            return find,i       # return True and index of element
        else:
            i=i+1
    return False                # otherwise return false, O(n)

# this function check for tuples in the list which are of (variable, index) and return the corresponding value of variables which are located at index 
# also this fuction returns a list which is basically an unused list
def varTup(L):
    n=len(L)
    i=0
    G=L.copy()                  # G is a fresh shallow copy of L, O(n)
    while i<n:
        if type(L[i]) is tuple: # if element at i index is tuple 
            (a,b)=L[i]
            print(a+' = '+L[b]) # print variable and its corresponding value
            # to remove the tuple and found value at index position from the list
            if not found(G,(a,b)) and not found(G,L[b]):        #O(2n) in worst case
                G=G
            elif not found(G,(a,b)):
                G.remove(L[b])
            elif not found(G,L[b]):
                G.remove((a,b))
            else:
                G.remove((L[b])) 
                G.remove((a,b))  
        i+=1
    m=len(G)
    F=[]
    for i in range(m):          #O(m)
        F.append(eval(G[i]))    # to convert all string elements in G to integer       
    return (F)# returns garbage list, O(2n^2)=O(n^2)

print()
lines = [] # initalise to empty list
with open("/Users/rishabhkumar/Downloads/input_file.txt") as f:
    lines = f.readlines() # read all lines into a list of strings
    n=len(lines)
L=[]   # initialising list L
for i in range(n):
    List=lines[i].split() # split lines along space
    if len(List)==3 :     # line is VARIABLE = TERM
        if List[2].isdigit() or List[2] == 'True':  # if TERM is a number or True(not a variable)
            if not found(L,List[2]):                # if TERM is not in L
                L.append(List[2])                   # append TERM to L
                L.append((List[0],len(L)-1))        # append (VARIABLE,index) to L
            else:
                find,index=found(L,List[2])
                L.append((List[0],index))           # if TERM is already in L, append (VARIABLE,index) to L                
        elif List[2] ==  'False' :                  # if TERM is False           
            if not found(L,List[2]):                # if TERM is not in L
                L.append(List[2])                   # append TERM to L
                L.append((List[0],len(L)-1))        # append (VARIABLE,index) to L
            else:
                find,index=found(L,List[2])
                L.append((List[0],index))           # if TERM is already in L, append (VARIABLE,index) to L                
        elif List[2].isalpha():                     # if TERM is a variable
            if not istuple(L,List[2]):              # if that variable is not in list that means that variable is undefined
                print('error :',List[2],'is not defined') # print error message and exit
                sys.exit(0)
            else:
                find,index=istuple(L,List[2])       # if that variable is in list, find its index
                (a,b)=L[index]
                L.append((List[0],b))               # append (VARIABLE,index) to L
    elif len(List)==4:    # line is VARIABLE = UNARY OPERATOR TERM
        if List[3].isdigit()  or List[3]=='True':   # if term is true or a number 
            if not found(L,List[3]):                # if term is not in list, append it
                L.append(List[3])
                v=str(eval(List[2]+' '+List[3]))    # evaluating the RHS
                if not found(L,v):
                    L.append(v)                     # if not in list append the value 'v' with its index
                    L.append((List[0],len(L)-1))
                else:
                    find,index=found(L,v)           # if v is in list append only tuple with index
                    L.append((List[0],index))  
            else:                                   # if term is in list then dont append it
                v=str(eval(List[2]+' '+List[3]))    # evaluating the RHS
                if not found(L,v):
                    L.append(v)                     # if not in list append the value 'v' with its index
                    L.append((List[0],len(L)-1))
                else:
                    find,index=found(L,v)           # if v is in list append only tuple with index
                    L.append((List[0],index))  
                                                    
        elif List[3]=='False':                      # similarly if term is false
            if not found(L,List[3]):
                L.append(List[3])
                v=str(eval(List[2]+' '+List[3]))    # evaluating the RHS
                if not found(L,v):
                    L.append(v)                     # if not in list append with its index
                    L.append((List[0],len(L)-1))
                else:
                    find,index=found(L,v)
                    L.append((List[0],index))  
            else:
                v=str(eval(List[2]+' '+List[3]))
                if not found(L,v):
                    L.append(v)
                    L.append((List[0],len(L)-1))
                else:
                    find,index=found(L,v)
                    L.append((List[0],index))  
            
        elif List[3].isalpha():                     # if term is a varible
                if not istuple(L,List[3]):          # if variable is not defined then print error and exit
                    print('error:'+List[3] +'is not defined')
                    sys.exit()
                else:
                    find,index=istuple(L,List[3])   # if variable is defined and value is at b index
                    (a,b)=L[index]
                    if L[b].isdigit() or L[b]=='True': # if value at b index is true or digit
                        v=str(eval(List[2]+' '+L[b]))  # evalute RHS
                        if not found(L,v):
                            L.append(v)                # if v is not in list append the value v with its index tuple
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)       # if v is in list append with its index tuple
                            L.append((List[0],index))
                    elif List[b]=='False':              # similarly if term value is false
                        v=str(eval(List[2]+' '+L[b]))
                        if not found(L,v):
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index))   
    elif len(List)==5:    # line is VARIABLE = TERM BINARY OPERATOR TERM
        if List[3]=='/':                           # if binary operator is '/' then update it to '//', as we are supposed to return integer value only
            List[3]='//'
        
        # N=lines[i].split('=',1)
        if (List[2].isdigit() or List[2]=='True'): # if first term is true or digit      
            if not found(L,List[2]):               
                L.append(List[2])
                if (List[4].isdigit() or List[4]=='True' ): # if second term is true or digit
                    v=str(eval(List[2]+' '+List[3]+' '+List[4])) # evaluate RHS
                    if not found(L,List[4]):                    # if second term is not in list append it
                        L.append(List[4])
                        if not found(L,v):                      # if RHS is not in list append it and also its index tuple
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:                                   # if RHS is in list append only its index tuple
                            find,index=found(L,v)
                            L.append((List[0],index))
                    else:                                       # if second term is in listdon't append it
                        if not found(L,v):                      # if RHS is not in list append it and also its index tuple
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:                                   # if RHS is in list append only its index tuple
                            find,index=found(L,v)
                            L.append((List[0],index))
                elif List[4]=='False':                          #similarly if second term is false
                    v=str(eval(List[2]+' '+List[3]+' '+List[4]))
                    if not found(L,List[4]):
                        L.append(List[4])
                        if not found(L,v):
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index))
                    else:
                        if not found(L,v):
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index))
                elif List[4].isalpha():                         # if second term is a variable
                    if not istuple(L,List[4]):                  # if variable is not defined then print error and exit
                        print('error :',List[4],'is not defined')
                        sys.exit()
                    else:                                       # if variable is defined and value is at b index
                        find,index=istuple(L,List[4])           
                        (a,b)=L[index]
                        v=str(eval(List[2]+' '+List[3]+' '+L[b])) # evaluate RHS after putting value of second term at b index
                        if not found(L,v):                      # if RHS is not in list append it and also its index tuple
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:                                   # if RHS is in list append only its index tuple
                            find,index=found(L,v)
                            L.append((List[0],index)) 
                        
            else:                                               # if first term is False and is already in list don't append it and further same as above
                if (List[4].isdigit() or List[4]=='True' ):     # if second term is true or digit....
                    v=str(eval(List[2]+' '+List[3]+' '+List[4]))
                    if not found(L,List[4]):                    
                        L.append(List[4])
                        if not found(L,v):
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index))
                    else:
                        if not found(L,v):
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index))
                elif List[4]=='False':                          # if second term is false......
                    v=str(eval(List[2]+' '+List[3]+' '+List[4]))
                    if not found(L,List[4]):
                        L.append(List[4])
                        if not found(L,v):
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index))
                    else:
                        if not found(L,v):
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index))
                elif List[4].isalpha():                         # if second term is a variable..........
                    if not istuple(L,List[4]):
                        print('error :',List[4],'is not defined')
                        sys.exit()
                    else:
                        find,index=istuple(L,List[4])
                        (a,b)=L[index]
                        v=str(eval(List[2]+' '+List[3]+' '+L[b]))
                        if not found(L,v):
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index))
                        
        elif List[2]=='False':                              # if first term is false.....
            if not found(L,List[2]):                        # if first term is not in list append it and follow as above
                L.append(List[2])
                if (List[4].isdigit() or List[4]=='True' ):
                    v=str(eval(List[2]+' '+List[3]+' '+List[4]))
                    if not found(L,List[4]):
                        L.append(List[4])
                        if not found(L,v):
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index))
                    else:
                        if not found(L,v):
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index))
                elif List[4]=='False':
                    v=str(eval(List[2]+' '+List[3]+' '+List[4]))
                    if not found(L,List[4]):
                        L.append(List[4])
                        if not found(L,v):
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index))
                    else: 
                        if not found(L,v):
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index))
                elif List[4].isalpha():
                    if not istuple(L,List[4]):
                        print('error :',List[4],'is not defined')
                        sys.exit()
                    else:
                        find,index=istuple(L,List[4])
                        (a,b)=L[index]
                        v=str(eval(List[2]+' '+List[3]+' '+L[b]))
                        if not found(L,v):
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index))
                          
            else:                                           # if first term is in list don't append it and follow as above.....
                if (List[4].isdigit() or List[4]=='True' ):
                    v=str(eval(List[2]+' '+List[3]+' '+List[4]))
                    if not found(L,List[4]):
                        L.append(List[4])
                        if not found(L,v):
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index))
                    else:
                        if not found(L,v):
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index))
                elif List[4]=='False':
                    v=str(eval(List[2]+' '+List[3]+' '+List[4]))
                    if not found(L,List[4]):
                        L.append(List[4])
                        if not found(L,v):
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index))
                    else:
                        if not found(L,v):
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index))
                elif List[4].isalpha():
                    if not istuple(L,List[4]):
                        print('error :',List[4],'is not defined')
                        sys.exit()
                    else:
                        find,index=istuple(L,List[4])
                        (a,b)=L[index]
                        v=str(eval(List[2]+' '+List[3]+' '+L[b]))
                        if not found(L,v):
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index))
        elif List[2].isalpha():                                 # if first term is a variable
            if not istuple(L,List[2]):                          # if this variable is not defined then print error and exit
                print('error :',List[2],'is not defined')
                sys.exit()
            else:                                               # if the first term variable is defined and at index b1
                find,index=istuple(L,List[2])
                (a1,b1)=L[index]
                if (List[4].isdigit() or List[4]=='True' ):     # if second term is a number or true
                    v=str(eval(L[b1]+' '+List[3]+' '+List[4]))  # evaluate the expression
                    if not found(L,List[4]):                    # if the second term is not in the list then append it
                        L.append(List[4])
                        if not found(L,v):                      #  append it to list if it is not already there
                            L.append(v)
                            L.append((List[0],len(L)-1))        # append the expression and its index to list
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index))           # if value is already there then append only tuple with index
                    else:                                       # if the second term is in the list don't append it and follow as above.....
                        if not found(L,v):
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index))
                elif List[4]=='False':                          # if second term is false proceed similarly...
                    v=str(eval(L[b1]+' '+List[3]+' '+List[4]))
                    if not found(L,List[4]):
                        L.append(List[4])
                        if not found(L,v):
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index))
                    else:
                        if not found(L,v):
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index))
                elif List[4].isalpha():                         # if second term is a variable, further same as above....
                    if not istuple(L,List[4]):
                        print('error :',List[4],'is not defined')
                        sys.exit()
                    else:
                        find,index=istuple(L,List[4])
                        (a,b)=L[index]
                        v=str(eval(L[b1]+' '+List[3]+' '+L[b]))
                        if not found(L,v):
                            L.append(v)
                            L.append((List[0],len(L)-1))
                        else:
                            find,index=found(L,v)
                            L.append((List[0],index)) 

    else:                 # if line is not of size 3, 4 or 5
        print('invalid input length in line',i+1 )#,' ,upto',i,'line output is below') 
        sys.exit()        # exit the program
    # now to check whether last element( which is variable of ongoing line) of list is already in list or not
    T=L.copy()            # copying the list to T
    (a,b)=T[-1]
    T.remove((a,b))       # removing the last element of T
    if not istuple(T,a):  # if the variable is not in list
        T.append((a,b))
        L=T               # then append the variable to list
    else:                 # if the variable is in list
        find,index=istuple(T,a)
        T[index]=(a,b)#len(T)-1) # then replace the variable with its index
        L=T             # then update the list by name L    
# print(L)                  
# print(len(L))
print(varTup(L))        # print output that contains value of every variable and the garbage list
 