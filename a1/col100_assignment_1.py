def rem():
    return 3%4
    #My entry number is 2021CS10103 so last 2-digits are 03.

def hadd(a,b):
     return ((a or b) and not (a and b), a and b)
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


def cmp(a0,a1,a2,a3, b0,b1,b2,b3):
    #last 2 digits are 03 of my entry number so remainder is 3 thus >= is our case of "True"
    #program for a3a2a1a0>=b3b2b1b0
    if (a3 is True and b3 is False):
        return True
    elif ((not a3 and not b3) or (a3 and b3)) and (a2 is True and b2 is False):
        return True
    elif ((not a3 and not b3) or (a3 and b3)) and ((not a2 and not b2) or (a2 and b2)) and (a1 is True and b1 is False):
        return True
    elif ((not a3 and not b3) or (a3 and b3)) and ((not a2 and not b2) or (a2 and b2)) and ((not a1 and not b1) or (a1 and b1)) and (a0 is True and b0 is False):
        return True
    elif ((not a3 and not b3) or (a3 and b3)) and ((not a2 and not b2) or (a2 and b2)) and ((not a1 and not b1) or (a1 and b1)) and ((not a0 and not b0) or (a0 and b0)):
        return True
    else:
        return False



def hsub(a,b):
    #defining 1-bit subtractor
    return ((a or b) and not (a and b), not a and b)
def fsub(a,b,c):
    #full subtractor using 1-bit subtractor
    (s0,s1)=hsub(a,b)
    (s2,s3)=hsub(s0,c)
    return (s2,s1 or s3)
def sub4(a0,a1,a2,a3, b0,b1,b2,b3):
    #4-bit subtractor using full subtractor
    if cmp(a0,a1,a2,a3, b0,b1,b2,b3):
        (s0,s1)=fsub(a0,b0,False)                                               #initially borrow is 0 i.e. False
        (s2,s3)=fsub(a1,b1,s1)                                                  #continuously taking borrow
        (s4,s5)=fsub(a2,b2,s3)
        (s6,s7)=fsub(a3,b3,s5)
        return (s0,s2,s4,s6,False)                                              #False represent positive sign
    else:
        (d0,d1,d2,d3,d4)=sub4(b0,b1,b2,b3, a0,a1,a2,a3)
        return (d0,d1,d2,d3,True)                                               #True represent negative sign

def add8(a, b, c):
    #8-bit adder using two 4-bit adders
    #assigning local variables
    (a0,a1,a2,a3,a4,a5,a6,a7) = a
    (b0,b1,b2,b3,b4,b5,b6,b7) = b
    (s0,s1,s2,s3,s4)=add4(a0,a1,a2,a3, b0,b1,b2,b3, c)                          # s4 is a carry bit
    (s5,s6,s7,s8,s9)=add4(a4,a5,a6,a7, b4,b5,b6,b7, s4)
    return ((s0,s1,s2,s3,s5,s6,s7,s8), s9)


def mul4(a, b):
    (a0,a1,a2,a3) = a                                                           #assigning local variables
    (b0,b1,b2,b3) = b
    #defining 4 bit multiplier
    if b == (False,False,False,False):                                          #base case
        return (False,False,False,False,False,False,False,False)
    else:
        (s0,s1,s2,s3,s4)=sub4(b0,b1,b2,b3, True,False,False,False)              #recursive case
        s = (s0,s1,s2,s3)
        (m0,m1,m2,m3,m4,m5,m6,m7)=mul4(a, s)
        x1=(m0,m1,m2,m3,m4,m5,m6,m7)
        x2=(a0,a1,a2,a3,False,False,False,False)
        ((p0,p1,p2,p3,p4,p5,p6,p7), p8)=add8(x1, x2, False)
        return (p0,p1,p2,p3,p4,p5,p6,p7)