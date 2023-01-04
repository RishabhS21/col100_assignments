import math
#Question 1
#1a
#taylor series expansion of function 'e^x' upto 'n' terms
def expn(x,n):
    #INPUT Specifications: n > 0
    #OUTPUT Specifications: e^x = 1+x+x^2/2!+x^3/3!+.......
    # initialisation
    i_term=1    # first term is 1 and i_term is containing general ith term
    sum=i_term  # represents sum of i terms
    i=1         # initialising with i=1
    # INVARIANT1 i_term = x^(i-1)/(i-1)!
    # INVARIANT2 sum = sum of first i terms
    while i<=(n-1):     # TERMINATION n-i decreases to 0
        i_term= i_term*(x/i)        #next term is (x/i) times the previous one, time complexity O(1)
        sum += i_term                                                           #time complexity O(1)
        i += 1                      #increment by 1, time complexity #O(1)
    return sum  #time complexity O(n) as while loop is executing n times with constant no. of calculations

#1b
#taylor series expansion of 'cos(x)' upto 'n' terms
def cosine(x,n):
    #INPUT Specifications: n > 0
    #OUTPUT Specifications: cos(x)==1-x^2/2!+x^4/4! +...
    # initialisation
    i_term=1    # first term is 1 and i_term is containing general ith term
    sum=i_term  # represents sum of i terms
    i=1         # initialising with i=1
    # INVARIANT1 i_term = (-1)^(i-1)(x^2*(i-1)/2*(i-1)!)
    # INVARIANT2 sum = sum of first i terms
    while i<=(n-1):     # TERMINATION n-i decreases to 0
        i_term *= -x*x/((2*i-1)*(2*i))      #next term is -(x^2/((2*i-1)*(2*i))) times the previous one, time complexity #O(1)
        sum += i_term                                                           #time complexity #O(1)
        i += 1                              #increment by 1, time complexity #O(1)
    return sum  #time complexity O(n) as while loop is executing n times with constant no. of calculations

#1c
#taylor series expansion of '1/(1-x)' upto 'n' terms
def inverse(x,n):
    #INPUT Specifications: n > 0 and |x|<1
    #OUTPUT Specifications: 1/(1-x)= 1+x+x^2+x^3......
    # initialisation
    i_term=1    # first term is 1 and i_term is containing general ith term
    sum=i_term  # represents sum of i terms
    i=1         # initialising with i=1
    # INVARIANT1 i_term = x^(i-1)
    # INVARIANT2 sum = sum of first i terms
    while i<=(n-1):     # TERMINATION n-i decreases to 0
        i_term= i_term*(x)          #next term is (x) times the previous one, time complexity #O(1)
        sum += i_term                                                           #time complexity #O(1)
        i += 1                      #increment by 1, time complexity #O(1)
    return sum  #time complexity O(n) as while loop is executing n times with constant no. of calculations

#1d
#taylor series expansion of 'natural log' upto 'n' terms
def natural_log(x,n):
    #INPUT Specifications: n > 0
    #OUTPUT Specifications: ln(1+x)= x-x^2/2+x^3/3......
    # initialisation
    i_term=x    # first term is x and i_term is containing general ith term
    sum=i_term  # represents sum of i-1 terms
    i=2         # initialising with i=2
    # INVARIANT1 i_term = (-1)^(i-1)*x^i/(i)!
    # INVARIANT2 sum = sum of first i-1 terms
    while i<=(n):       # TERMINATION n-i+1 decreases to 0
        i_term= -i_term*(x*(i-1)/i)         #next term is (x*(i-1)/i) times the previous one, time complexity #O(1)
        sum += i_term                                                           #time complexity #O(1)
        i += 1                      #increment by 1, time complexity #O(1)
        #end when i = n+1, INVARIANT2 sum = sum of n terms
    return sum  #time complexity O(n) as while loop is executing n times with constant no. of calculations

#1e
#taylor series expansion of 'tan inverse' upto 'n' terms
def tan_inv(x,n):
    #INPUT Specifications: n > 0
    #OUTPUT Specifications: tan^(-1)(x)= x-x^3/3+x^5/5....
    # initialisation
    i_term=x    # first term is x and i_term is containing general ith term
    sum=i_term  # represents sum of i terms
    i=1         # initialising with i=1
    # INVARIANT1 i_term = (-1)^(i-1)*x^(2i-1)/(2i-1)!
    # INVARIANT2 sum = sum of first i terms
    while i<=(n-1):     # TERMINATION n-i decreases to 0
        i_term= -i_term*(x*x*(2*i-1)/(2*i+1))       #next term is (x*x*(2*i-1)/(2*i+1)) times the previous one, time complexity #O(1)
        sum += i_term                                                           #time complexity #O(1)
        i += 1                      #increment by 1, time complexity #O(1)
    return sum  #time complexity O(n) as while loop is executing n times with constant no. of calculations


#Question 2
#to find the root of assigned function via iterative bisection
#f(x)= (1/(1-x))- cos(x)
#given:
#f(a).f(b)<0
#OUTPUT
#Found == True implies |f (Value)| ≤ eps
#IterList:denotes the series of approximate results as
#the iteration converges towards the root (or when the loop is exited).
def bisect(a,b,eps):
    f1=(1/(1-a))- math.cos(a)
    f2=(1/(1-b))- math.cos(b)
    #initialisation
    Found=False
    m = a
    IterList = [ ]      #intitially list contain no value
    #INVARIANT 1: f(a).f(b)<0 ==> f has root in interval[a,b] and Found =True ==>|f(m)| i.e. |out|<=eps
    #INVARIANT 2: IterList=the series of approximate results
    while (a<b) and (not Found): #TERMINATION: b-a decreases
        m=(a+b)/2                #bisecting the interval, m>=tol
        out = (1/(1-m))- math.cos(m) #out=f(m)
        IterList.append(m)          #sticking m at the end of series,  time complexity=time to append(constant time)
        if abs(out)<= eps:          #found root
            Found=True
        elif out*f2<0:
            a=m                     #updating left boundary if f(m).f(b)<0
        else:
            b=m                     #updating right boundary if f(m).f(b)>0
    value=m
    return (Found, value, IterList)
    #time complexity T(b-a)=T((b-a)/2) +C
    #                      =T((b-a)/4) +2C
    #                      =T((b-a)/2^3) +3C
    #                           .
    #                           .
    #                      =T((b-a)/2^n) +nC and width (b-a)/2^n>=tol ##for very large n T(tol)-->0
    #                T(b-a)=nC  ,and log(base 2, (b-a)/tol) >= n
    #               T(b-a) >= [log(base 2, (b-a)/tol)]C ==> T(b-a) is O(log(b-a))


#Question 3
#functions that return coefficient of x^n in their taylor expansion iteratively

#3a
def expn_coeff(n):
    #coeff have no value when n<0
    if n<0:
        return 0
    else:
        #initialisation
        i_term=1
        i=1
        #INVARIANT i_term= 1/i!
        while i<=(n): # TERMINATION  n-i+1 decreases to 0
            i_term= (i_term/i)
            i += 1              #increment by 1 in i
        return i_term  #time complexity O(n) as while loop is executing n times with constant no. of calculations

#3b
def cosine_coeff(n):
    #coeff have no value when n<0 and when n is odd
    if n<0:
        return 0
    elif n%2!=0:
        return 0
    else:       #n is even
        #initialisation
        i_term=1
        i=1
        #INVARIANT i_term= 1/(i-1)! ,final value will be returned when i=n+1
        while i<=(n): # TERMINATION  n-i+1 decreases to 0
            i_term= (i_term/i)
            i += 1
        if (n/2)%2!=0:   #negative value when n/2 is odd
            return -i_term
        else:
            return i_term  #time complexity O(n) as while loop is executing n times with constant no. of calculations

#3c
def inverse_coeff(n):
    #coeff have no value when n<0
    if n<0:
        return 0
    else:
        #initialisation
        i_term=1
        i=1
        #INVARIANT i_term= 1
        while i<=(n): # TERMINATION  n-i+1 decreases to 0
            i_term *= 1
            i += 1
        return i_term  #time complexity O(n) as while loop is executing n times with constant no. of calculations

#3d
def natural_log_coeff(n):
    #coeff have no value when n<0
    if n<=0:
        return 0
    else:
        #initialisation
        i_term=1
        i=1
        #INVARIANT i_term= (-1)^i*(1/i)
        while i<=(n-1): # TERMINATION  n-i decreases to 0
            i_term= -(i_term*i/(i+1))
            i += 1
        return i_term  #time complexity O(n) as while loop is executing n times with constant no. of calculations

#3e
def tan_inv_coeff(n):
    #coeff have no value when n<0 and when n is even
    if n<0:
        return 0
    elif n%2==0:
        return 0
    else:
        #initialisation
        i_term=1
        i=1
        #INVARIANT i_term= 1/i
        while i<=(n-1): # TERMINATION  n-i decreases to 0
            i_term= (i_term*(i)/(i+1))
            i += 1
        if ((n-1)/2)%2 !=0:  # negative of i_term is returned when (n-1)/2 is odd
            return -i_term
        else:
            return i_term
        return i_term  #time complexity O(n) as while loop is executing n times with constant no. of calculations


#Question 4
#return the sum of series upto a specific power n, iteratively
###comments for all part of Question 4
#initialisation i=1
#INVARIANT: sum = sum of taylor series upto power i-1
#TERMINATION n-i+1 decreases to 0
#all coefficient calculating function has time complexity as O(n) for calculating coefficient of x^n
#O(i)+4 is executed n times
# T(n)= 4n+ {O(1)+O(2)+O(3)+....+O(n)} = O(n^2)
#time complexity is O(n^2)

#4a
def expn_t(x,n):
    sum =expn_coeff(0)
    i=1
    while i<=n:
        sum += expn_coeff(i)*(x**i)
        i += 1
    return sum  #time complexity is O(n^2)

#4b
def cosine_t(x,n):
    sum =cosine_coeff(0)
    i=1
    while i<=n:
        sum += cosine_coeff(i)*(x**i)
        i += 1
    return sum  #time complexity is O(n^2)

#4c
def inverse_t(x,n):
    sum =inverse_coeff(0)
    i=1
    while i<=n:
        sum += inverse_coeff(i)*(x**i)
        i += 1
    return sum  #time complexity is O(n^2)

#4d
def natural_log_t(x,n):
    sum =natural_log_coeff(0)
    i=1
    while i<=n:
        sum += natural_log_coeff(i)*(x**i)
        i += 1
    return sum  #time complexity is O(n^2)

#4e
def tan_inv_t(x,n):
    sum =tan_inv_coeff(0)
    i=1
    while i<=n:
        sum += tan_inv_coeff(i)*(x**i)
        i += 1
    return sum  #time complexity is O(n^2)


#Question 5
#f(x)=ln(1+x) and g(x)=cos(x)

#5a
#returns coefficient of x^n in f(x)+g(x)
def add_coeff(n):
    return natural_log_coeff(n) + cosine_coeff(n) #time complexity O(n)+O(n)=O(n)

#5b
#returns the coefficient of x^n in the Taylor series of f(x).g(x)
def mul_coeff(n):
    #initialisation
    i=0
    sum=0
    #INVARIANT : sum = coefficient of x^(i-1) in the Taylor series of f(x).g(x)
    while i<=n:         #TERMINATION: n-i+1 decreases to 0
        p=natural_log_coeff(i)      # O(i)
        j=n-i                       # O(1)
        q=cosine_coeff(j)           # O(n-i) as j=n-i
        sum = sum + p*q             # O(1)
        i=i+1                       # O(1)
    return sum                      # T(n)=n*{O(i)+O(1)+O(n-i)+O(1)+O(1)}= O(n^2)

#5c
#returns the coefficient of x^n in the Taylor series of (d.f(x)/dx)
def diff_coeff(n):
    return (n+1)*natural_log_coeff(n+1) # time complexity T(n)= 2+O(n+1) = O(n)


#Question 6
def limit_diff(x,eps):
    a=cosine(x,20)          # O(20)=O(1)
    h=eps                   # O(1)
    b=natural_log(x,20)     # O(20)=O(1)
    c1= b*a                 # O(1)
    x=x+h                   # O(1)
    a=cosine(x,20)          # O(20)=O(1)
    h=eps                   # O(1)
    b=natural_log(x,20)     # O(20)=O(1)
    c2= b*a                 # O(1)
    return (c2-c1)/h        #time complexity is O(1) as the program is running in constant time