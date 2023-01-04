#from assignment_1
def add(a,b,c):
    #full adder with help of half adder
    s1=(a or b) and not (a and b)                                               #taken hint from half adder for sum bit
    c1=(a and b)                                                                #half adder for carry bit
    c2=(s1 and c)                                                               #carry bit for s1 and c
    return ((s1 or c) and not (s1 and c), c2 or c1)
def add4(a0,a1,a2,a3, b0,b1,b2,b3, c):
    #a 4-bit adder with the help of full adder
    (x1,y1)=add(a0,b0,c)                                                        #continuously taking carry bit
    (x2,y2)=add(a1,b1,y1)
    (x3,y3)=add(a2,b2,y2)
    (x4,y4)=add(a3,b3,y3)
    return (x1,x2,x3,x4,y4)
def add8(a, b, c):
    #8-bit adder using two 4-bit adders
    #assigning local variables
    (a0,a1,a2,a3,a4,a5,a6,a7) = a
    (b0,b1,b2,b3,b4,b5,b6,b7) = b
    (s0,s1,s2,s3,s4)=add4(a0,a1,a2,a3, b0,b1,b2,b3, c)                          # s4 is a carry bit
    (s5,s6,s7,s8,s9)=add4(a4,a5,a6,a7, b4,b5,b6,b7, s4)
    #we need 8 bit return as there will be no 9th bit/carry bit in mul4, so i removed 9th bit
    return (s0,s1,s2,s3,s5,s6,s7,s8)

def mul(a,b0):
    (a0,a1,a2,a3)=a
    if b0 is False:
        return (False,False,False,False)
    else:
        return a


#Question_1

def mul4(a,b):
    (a0,a1,a2,a3)=a
    (b0,b1,b2,b3)=b
    #to make all value of 8-bit I calculated manually as we don't have function to add any sized binary
    #calculating it recursively and then adding (Ideology is same as in algorithm)
    (x0,x1,x2,x3)=mul(a,b0)
    m1=(x0,x1,x2,x3,False,False,False,False)
    (y0,y1,y2,y3)=mul(a,b1)
    m2=(False,y0,y1,y2,y3,False,False,False)
    (z0,z1,z2,z3)=mul(a,b2)
    m3=(False,False,z0,z1,z2,z3,False,False)
    (w0,w1,w2,w3)=mul(a,b3)
    m4=(False,False,False,w0,w1,w2,w3,False)
    #adding them using 8-bit adder from assignment_1
    p1=add8(m4, m3, False)
    p2=add8(p1, m2, False)
    p3=add8(p2, m1, False)
    return p3

#Question_2

def mul4i(a,b):
    (a0,a1,a2,a3)=a
    (b0,b1,b2,b3)=b
    #doing iteratively, adding just after calculating(using same idea as in algorithm)
    #then adding using previously defined add8 function
    m1=(False,False,False,False,False,False,False,False)
    (w0,w1,w2,w3)=mul(a,b3)
    m2=(False,False,False,w0,w1,w2,w3,False)
    p1=add8(m1, m2, False)
    (z0,z1,z2,z3)=mul(a,b2)
    m3=(False,False,z0,z1,z2,z3,False,False)
    p2=add8(p1, m3, False)
    (y0,y1,y2,y3)=mul(a,b1)
    m4=(False,y0,y1,y2,y3,False,False,False)
    p3=add8(p2, m4, False)
    (x0,x1,x2,x3)=mul(a,b0)
    m5=(x0,x1,x2,x3,False,False,False,False)
    p4=add8(p3, m5, False)
    return p4