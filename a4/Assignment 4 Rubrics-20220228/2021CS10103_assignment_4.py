#PART 1 (there are no duplicates in any input list #constrained on all)
#1
def emptyset():
    #empty set returns a []
    return []  #O(1) as its taking costant time
# print(emptyset())

#2
def isEmpty(S):
    # Input a set S of any type
    #Output if set S is empty then it will have no element means 0 length and returns True
    #       otherwise false
    if len(S) ==0:
        return True
    else:
        return False    #O(1) as its taking costant time
#print(isEmpty([0,1,1,0,1]))
#print(isEmpty([]))

#3
def member(S,e):
    #Input a set S of any type and an element e
    # Output returns boolean value true if e is in S otherwise false
    s=len(S)
    found = False
    i=0
    # INVARIANT: found == False implies forall j (0 ≤ j < i): L[j] =/= e
    # found == True implies L[i] == e
    while i < s and not found: # n-i is decreasing
        if S[i] == e:       # indexing has a time complexity O(1)
            found=True
        else:
            i +=1       #in worst case while loop executing n times
    return found #time complexity O(s), s=len(S)
#print(member([4 ,2 ,3 ,1] ,4))
#print(member(["ELL100","MTL100","COL100"],"MTL100"))
#print(member(['a','d','w','q','e','r','t','y','u','i','o','k','j','g'],'u'))

#4
def singleton(x):
    #return a singleton set with single element given x of any type
    # output [x]
    return [x]      # O(1)
#print(singleton('mtl100'))

#5
def isSubset(P,Q):
    #Input P and Q are two sets of same type represented as list
    #Output return boolean value True if P is a subset of Q
    p=len(P)
    i=0
    while i<p : #p-i is decreasing
        # return False at same time if got a particular element isn't in Q of P
        if member(Q,P[i])is False:       # member fn. has a time complexity O(len(Q))
            return False
        else:
            i +=1      #in worst case while loop executing p times
        # return True if got all element is in Q of P
    return True #time complexity O(p*q), p=len(P) and q=len(Q)
# print(isSubset (['a','d','w','q','n'] ,['a','d','w','q','e','r','t','y','u','i','o','k','j','g']))
# print(isSubset ([1 ,2,3] ,[3 ,2 ,1 ,4]))

#6
def setEqual(P,Q):
    #Input P and Q are two sets of same type represented as list
    #Output return boolean value True if P is exactly equal to Q
    if len(P)==len(Q) and isSubset(P,Q) is True: #time complexity of isSubset fn. is O(p*q), p=len(P) and q=len(Q)
        # return True if got P is subset of Q and length of list is also same
        # as there is no repeated elements in any set
        return True
    else:               # len has O(1) as time complexity
        return False    #time complexity O(p*q), p=len(P) and q=len(Q)
#print(setEqual ([1 ,2 ,3] ,[3 ,2 ,1]))
#print(setEqual ([1 ,2 ,3,4] ,[3 ,2 ,1]))
#print(setEqual(['a','d','w','q','i','o','k','j','g','e','r','t','y','u'],['a','d','w','q','e','r','t','y','u','i','o','k','j','g']))

#7
def union(P,Q):
    #Input P and Q are two sets of same type represented as list
    #Output: returns the list that represents the set PUQ( P union Q)
    p=len(P)
    i=0
    # Invariant Q = (P[0:i]UQ)
    while i<p:      #p-i is decreasing
        if member(Q,P[i]) is False:     # member fn. has a time complexity O(len(Q))
            Q.append(P[i])              # append has O(1)
        i +=1                           # loop executing p times
    return Q    #time complexity O(p*q), p=len(P) and q=len(Q)
# print(union(["MTL100","COL100"],["NLN100","MTL100"]))
# print(union([5 ,2 ,3,4] ,[3 ,2 ,5423,1]))

#8
def intersection(P,Q):
    #Input P and Q are two sets of same type represented as list
    #Output: returns the list that represents  the set P∩Q( P intersection Q)
    p=len(P)
    i=0
    # Invariant L = (P[0:i]∩Q)
    L=[]
    while i<p:      #p-i is decreasing
        if member(Q,P[i]) is True:     # member fn. has a time complexity O(len(Q))
            L.append(P[i])              # append has O(1)
        i +=1                           # loop executing p times
    return L    #time complexity O(p*q), p=len(P) and q=len(Q)
# print(intersection (["MTL100" ,"COL100"] ,["NLN100" ,"MTL100"]))
# print(intersection([5 ,2 ,3,4,45,23,76,12] ,[12,23,11,234,453 ,2 ,5423,1]))

#9
def cartesian(P,Q):
    #Input P and Q are two sets of any types represented as list
    #Output returns the list that represent the cartesian product P×Q
    p=len(P)
    q=len(Q)
    L=[]
    i=0
    #Invariant L=P[0:i]×Q
    while i<p:      #p-i is decreasing
        j=0
        while j<q:  #q-j is decreasing
            L.append((P[i],Q[j]))
            j +=1                       # loop executing q times
        i +=1                           # loop executing p times
    return L    #time complexity O(p*q), p=len(P) and q=len(Q)
#print(cartesian ([1 ,3 ,2] ,["C" ,"M"]))

#10
def power(P):
    #Input P is a set of any type
    #Output returns a List which represents the set that contain all the subsets of P as elements
    #done recursively
    if len(P)==0:           #base case
        return [[]]
    else:
        P1=P[0:-1]          #removing last element => no. of elements decreasing
        P12=power(P1)       #power set of shorten list
        #appending last element in each element of power set of List which has one less element
        [x.append(P[-1]) for x in P12]
        L=power(P1)    #defining power(P1) again as our P12 has been updated
        L.extend(P12)  #adding both list(1st power(P1) )and 2nd appended one)
        return L
#time complexity T(p) = T(p-1) + len(P12)*O(1){for append} + O(len(P12)){for extend}
#                       len(P12) = 2^(p-1) , p=len(P)
#solving recursively gives time complexity is O(2^(p)), p=len(P)

# print(power([1,2]))
# print(power([1 ,2,3,7]))
# print(power([]))

#PART 2 (there are no duplicates in any input list and all are ordered sets #constrained on all)
#1
def emptyset_2():
    #empty set returns a []
    return []  #O(1) as its taking costant time
#print(emptyset())

#2
def isEmpty_2(S):
    # Input a set S of any type
    #Output if set S is empty then it will have no element means 0 length and returns True
    #       otherwise false
    if len(S) ==0:
        return True
    else:
        return False    #O(1) as its taking costant time
#print(isEmpty([0,1,1,0,1]))
#print(isEmpty([]))

#3
def member_2(S,e):
    #Input a set S(ordered) of any type and an element e
    # Output returns boolean value true if e is in S otherwise false
    a=0
    b=len(S)-1
    found=False
    #Invariant: found = False => S[m]=/=e
    #           found = True => S[m]==e
    while a<=b and not found: #b-a is decreasing
        m=(a+b)//2            #using bisection method
        if S[m]==e:           #if mid element is e return True
            found = True
        elif S[m]<e:          #if mid element is less than e
            a=m+1             #update a(left end) to m+1
        else:                 #if mid element is greater than e
            b=m-1             #update b(right end) to m-1
    return found
#time complexity T(b-a)=T((b-a)//2) +C           #(b-a)=(len(S)), s=len(S)
#                      =T((s)//4) +2C            #I have put s not s-1 considering big O
#                      =T((s)//2^3) +3C
#                           .
#                           .
#                      =T((s)//2^n) +nC  for large n and let (s)//2^n>=1 ##for very large n T(1)=O(1)
#                T(s)=nC  ,and log(base 2, (s)/1) >= n
#               T(s) >= [log(base 2, (s))]C ==> T(s) is O(log(s))
#print(member_2([1 ,2 ,3 ,4] ,4))
#print(member_2(["COL100","ELL100","MTL100"],"MTL100"))

#4
def singleton_2(x):
    #return a singleton set with single element given x of any type
    # output [x]
    return [x]      #O(1) as its taking costant time
#print(singleton_2(567))

#5
def isSubset_2(P,Q):
    #Input P and Q are two sets of same type represented as list(and are ordered)
    #Output return boolean value True if P is a subset of Q
    p=len(P)
    i=0
    while i<p :     #p-i is decreasing
        # return False at same time if got a particular element isn't in Q of P
        if member_2(Q,P[i])is False:       # member fn. has a time complexity O(log(len(Q)))
            return False
        else:
            i +=1      #in worst case while loop executing p times
        # return True if got all element is in Q of P
    return True         #time complexity O(p*log(q)), p=len(P) and q=len(Q)
#print(isSubset_2([1 ,2 ,3,4,5] ,[1 ,2 ,3 ,4]))
#print(isSubset_2 ([1 ,2 ,9] ,[2 ,3 ,6]))

#6
def setEqual_2(P,Q):
    #Input P and Q are two sets of same type represented as list(and are ordered)
    #Output return boolean value True if P is exactly equal to Q
    if len(P)==len(Q) and isSubset_2(P,Q) is True: #time complexity of isSubset fn. is O(p*log(q)), p=len(P) and q=len(Q)
        # return True if got P is subset of Q and length of list is also same
        # as there is no repeated elements in any set
        return True
    else:               # len has O(1) as time complexity
        return False    #time complexity O(p*log(q)), p=len(P) and q=len(Q)
# print(setEqual_2 ([1 ,2 ,3] ,[1 ,2]))
# print(setEqual_2 ([1 ,2 ,3] ,[1 ,2 ,3]))

#7
def union_2(P,Q):
    #Input P and Q are two sets of same type represented as list(and are ordered)
    #Output: returns the list that represents the set PUQ( P union Q), also ordered
    p=len(P)
    q=len(Q)
    i=0
    j=0
    L=[]
    # Invariant L = (P[0:i]UQ[0:j])
    while i<p and j<q:      #p-i and q-j is decreasing
        if P[i]<Q[j]:       #if P[i]<Q[j] keep the smaller in list L
            L.append(P[i])
            i +=1           # increment in i by 1
        elif P[i]==Q[j]:    #if P[i]==Q[j] keep anyone in list L
            L.append(P[i])
            i +=1           # increment in i by 1
            j +=1           # increment in j by 1
        else:               #if P[i]<Q[j] keep the smaller in list L
            L.append(Q[j])
            j +=1           # increment in j by 1
    if i==p:                #if list P has finished put all remaining elements of Q in L
        while j<q:          #q-j is decreasing
            L.append(Q[j])
            j +=1
    else:                   #if list Q has finished put all remaining elements of P in L
        while i<p:          #p-i is decreasing
            L.append(P[i])
            i +=1
    return L        #O(p+q)
# append and indexing has time complexity as O(1)
#for time complexity 1st loop is executing p+q-k times, k is some constant
#if 1st executing p times then 2nd will execute q-k1 times otherwise p-k2 times, k1&k2 are constant
#time complexity is O(p+q), p=len(P) and q=len(Q)
#print(union_2 (["COL" ,"ELL" ,"MTL"] ,["MTL" ,"PYL"]))
#print(union_2 ([1,3,4,56,87,344],[2,4,5,6,7,78,88,678]))

#8
def intersection_2(P,Q):
    #Input P and Q are two sets of same type represented as list(and are ordered)
    #Output: returns the list that represents  the set P∩Q( P intersection Q), also ordered
    p=len(P)
    q=len(Q)
    i=0
    j=0
    L=[]
    # Invariant L = (P[0:i]∩Q[0:j])
    while i<p and j<q:      #p-i and q-j is decreasing
        if P[i]<Q[j]:       #if P[i]<Q[j] no change in list L
            i +=1           # increment in i by 1
        elif P[i]==Q[j]:    #if P[i]==Q[j] keep anyone in list L
            L.append(P[i])
            i +=1           # increment in i by 1
            j +=1           # increment in j by 1
        else:               #if P[i]<Q[j] no change in list L
            j +=1           # increment in j by 1 #as anyone list get finished no need to check further
    return L                #O(p+q), p=len(P) and q=len(Q)
# append and indexing has time complexity as O(1)
#for time complexity loop is executing p+q-k times, k is some constant
# print(intersection_2 ([1 ,2 ,3 ,4,5,6,7,8,9,788,2323,34546,56455,65656] ,[3 ,4 ,5 ,6 ,7 ,8,65656]))
# print(intersection_2 (["COL" ,"ELL" ,"MTL"] ,["MTL" ,"PYL"]))

#9
def cartesian_2(P,Q):
    #Input P and Q are two sets of any types represented as list(and are ordered)
    #Output returns the list that represent the cartesian product P×Q (in ordered pair)
    p=len(P)
    q=len(Q)
    L=[]
    i=0
    #Invariant L=P[0:i]×Q
    while i<p:      #p-i is decreasing
        j=0
        while j<q:  #q-j is decreasing
            L.append((P[i],Q[j]))
            j +=1                       # loop executing q times
        i +=1                           # loop executing p times
    return L    #time complexity O(p*q), p=len(P) and q=len(Q)
# print(cartesian_2 ([1 ,2 ,3] ,['C','M']))
# print(cartesian_2([23,34,45,56,67,98],['a','c','e','y']))
#For ordering in cartesian product we will check 1st element of bracket (a,b) if a will be less then it will be put
# first in the list, in case if it is same then we will check for 2nd element in bracket

#10
def power_3(P):
    #Input P is a set of any type which is ordered by sorting
    #Output returns a List which represents the set that contain all the subsets of P as elements in ordered manner
    #       except the element [] is at last
    # helper function for power_2
    # done recursively
    if len(P)==0:           #base case
        return [[]]
    else:
        P1=P[1:]            #removing first element from given list P
        P13=power_3(P1)     #getting power set of new list in which no. of elements is decreased by 1
        P12=P13[0:-1]       #putting last element at first
        P12.insert(0,P13[-1])   #insert has time complexity O(k), k is length of list
        [x.insert(0,P[0]) for x in P12]  #extend has O(k), k is length of list to be extended
        #inserting 1st element in each element of power set of List which has one less element
        L=power_3(P1)       #defining power_3(P1) again as our P12 has been updated
        P12.extend(L)       #adding both list(1st inserted one) and 2nd (power_3(P1)) one)
        return(P12)         #P12 is sorted except the element [] is at last
#time complexity T(p) = T(p-1) + O(len(P12)){for insert} + O(len(P12)){for extend}
#                       len(P12) = 2^(p-1) , p=len(P)
#solving recursively gives time complexity is O(2^(p)), p=len(P)
def power_2(P):
    #Input P is a set of any type which is ordered by sorting
    #Output returns a List which represents the set that contain all the subsets of P as elements in ordered manner
    Q=power_3(P)
    T=power_3(P)
    S=Q[0:-1]
    S.insert(0,T[-1])
    return S        #time complexity is O(2^(p)), p=len(P)
# print(power_2([1,2,3]))
# print(power_2([1 ]))
#For ordering in power set we will check 1st element of a subset elemnt if it will be less then we will put it
# first in the list, in case if it is same then we will check for further elements in subset element