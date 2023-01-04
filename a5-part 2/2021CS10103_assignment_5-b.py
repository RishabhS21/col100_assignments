import sys

def ismember(x,l): # for element
    if x in l:
        return(True)
    else:
        return(False)
#timecomplexity is O(n) n is len(l)
#it will tell whether an element is in list or not 
def ismember2(x,l): #for tuple
    i=0
    while i<len(l):
        if ismember(x,l[i])==True:
            return(True)
        else:
            i+=1
    return False
#time complexity is O(n) where n is len(l)

# using it as helper fn it will give us the index of value of variable if present in list.            
def actualindex(z,l): #for tuple
    for x in l:
        if (ismember(z,x)==True):
            (a,b)=x
            return(b)
#time complexity is O(n) where n is len(l)

        
#it will give us the index of element we are trying to find in list.
def index(x,l):  # for element
    for i in range(0,len(l)):
        if ismember(x,l[i])==True:
            return(i)
#time complexity is O(n) where n is len(l)      



def joinList(lst): # to join all elements of a list which are of string type
    s=''
    for i in range(len(lst)):
        if i==0:
            s+=lst[i]
        else:
            s+=' '+lst[i]
    return s
# print(joinList(['a','b','c']))
lines = [] # initalise to empty list
with open('/Users/rishabhkumar/Downloads/Assignment 5 - part 2-20220306/input_file.txt') as f:
    lines = f.readlines() # read all lines into a list of strings
print (lines)

# collecting all the statements as instruction in list by changing if while
instruction_list=[]
for statement in lines: # each statement is on a separate line
    token_list=statement.split()
    if token_list[0]!='while':
        instruction_list.append( joinList(token_list))
    elif token_list[0]=='while':
        if token_list[2]=='<':
            instruction_list.append("BLE"+','+token_list[3][:-1]+','+token_list[1])
        elif token_list[2]=='>':
            instruction_list.append("BLE"+','+token_list[1]+','+token_list[3][:-1])
        elif token_list[2]=='<=':
            instruction_list.append("BLT"+','+token_list[3][:-1]+','+token_list[1])
        elif token_list[2]=='>=':
            instruction_list.append("BLT"+','+token_list[1]+','+token_list[3][:-1])
        elif token_list[2]=='==':
            instruction_list.append("BE "+','+token_list[1]+','+token_list[3][:-1])
        elif token_list[2]=='!=':
            instruction_list.append("BNE"+','+token_list[1]+','+token_list[3][:-1])
        else:
            print ("Syntax Error!!")  # invalid input

            sys.exit()  
# print(instruction_list) 

# making a list tab_count which has no. of tabs in corresponding statement line
lines = [] # initalise to empty list
with open('/Users/rishabhkumar/Downloads/Assignment 5 - part 2-20220306/input_file.txt') as f:
    lines = f.readlines() # read all lines into a list of strings
# print (lines)
tab_count=[]
for statement in lines: # each statement is on a separate line
    tabs = 0
    while statement[tabs] == '\t':
        tabs += 1
    tab_count.append(tabs)
print(tab_count)   


# make tuple of tab indices if it increase on going ahead
def same_tab_ahead(tab_list):
    change=[]
    for i in range(len(tab_list)):
        if tab_list[i]>tab_list[i-1]:
            for j in range(i+1,len(tab_list)):
                if tab_list[j]==tab_list[i-1]:
                    change.append((i-1,j))   # i-1 is the element index after which it get changed
                    break 
    return change
print(same_tab_ahead([0, 0, 0, 1, 0,1,0]))

# make tuple of tab indices if it decreases w.r.t. before element
def same_tab_before(tab_list):
    decrease=[]
    for i in range(len(tab_list)):
        if tab_list[i]<tab_list[i-1]:
            j=i-1
            while j>=0:
                if tab_list[j]==tab_list[i]:
                    decrease.append((i,j))   # i is the element value decreased after
                    break
                j-=1
            
    
    return decrease
# print(same_tab_before([0, 0, 0, 1, 0,1,0]))
# putting branch elements
k=0
for i in range(len(same_tab_before(tab_count))):
    (a,b)=same_tab_before(tab_count)[i]
    instruction_list.insert(a+k ,'branch '+str(b)) # as after putting branch we need to increase the index by 1 of further branch elements
    k+=1
# print(instruction_list)

# putting index values for while statements
# as we have to put index values for while statements so we need to take care of further added branh element so p is introduced
for i in range(len(same_tab_ahead(tab_count))):
    (a,b)=same_tab_ahead(tab_count)[i]
    p=0
    for j in range(0,len(instruction_list)):
        if instruction_list[j][0:4]=='bran':
            p+=1
        elif j==b+p:
            break
            
    # print(p)        
    instruction_list[a]=instruction_list[a]+','+str(b+p)
    
print('instruction list :' , instruction_list) # here we have the final list of instructions

# incomplete code, it is upto giving instructions list only and also with defining class
# incomplete code, it is upto giving instructions list only and also with defining class
# incomplete code, it is upto giving instructions list only and also with defining class
    
    
# l=[]
# for statement in instruction_list:
#     token_list=statement.split()
#     if statement[0:3]=='BLE':
#         for i in range():
#             jhg=0
#         if statement[4].isnumeric() and ismember(statement[4],l):
#             l.append(statement[4])
#         if statement[6].isnumeric() and ismember(statement[6],l):
#             l.append(statement[6])

# some test cases
# 1st input:            # 
# x = x + 1
# while x < 1:
# 	x = x + 1
# 	x = x + 1
# 	while y < 1:
# 		y = y + 1
# 		z = z + 1
# 		while z > 1:
# 			k = k + 1
# 	while a < 2:
# 		a = 2
# 		while l < 1:
# 			a = a + 1
# 			x = x + 1
# a = a + 1    
# output instruction list : ['x = x + 1', 'BLE,1,x,16', 'x = x + 1', 'x = x + 1', 'BLE,1,y,10', 'y = y + 1', 'z = z + 1',
# 'BLE,z,1,11', 'k = k + 1', 'branch 4', 'BLE,2,a', 'a = 2', 'BLE,1,l', 'a = a + 1', 'x = x + 1', 'branch 1', 'a = a + 1']      

# 2nd input
# i = 0
# while i < 3:
#     j = 1
#     while j < 2:
#         x = i + j
#         j = j + 1
#     i = i + 1   
# y = 0
# output instruction list : ['i = 0', 'BLE,3,i,9', 'j = 1', 'BLE,2,j,7', 'x = i + j', 'j = j + 1', 'branch 3', 'i = i + 1', 'branch 1', 'y = 0']
