import importlib, sys, traceback, re
from token import ISEOF
from glob import glob
fileNameRegex = re.compile('[0-9]{4}[a-zA-Z]{2}[0-9]{5}_assignment_4\.py')

emptyset_w = 1
isEmpty_w = 2
member_w = 10
singleton_w = 2 
isSubset_w = 15 
setEqual_w = 15
union_w = 15
intersection_w = 15
cartesian_w = 15
power_w = 20

emptyset_2_w = 1
isEmpty_2_w = 2
member_2_w = 15
singleton_2_w = 2 
isSubset_2_w = 15 
setEqual_2_w = 15
union_2_w = 15
intersection_2_w = 15
cartesian_2_w = 15
power_2_w = 20


files = glob("*_assignment_4.py")

if len(files)==0:
    print('Enter the file in correct format. Expected = <entryNumber>_assignment_4.py')
    sys.exit(1)

file = files[0]
print(file)

if(len(sys.argv) > 1):
    file = sys.argv[1]

m = fileNameRegex.match(file)

if m == None:
    print(f'Enter the file in correct format. Found = {file}. Expected<entryNumber>_assignment_4.py')
    sys.exit(1)

print("Found file: ",file)
file = file[:-3]


col100_module = importlib.import_module(file)
import math

# Test cases ---- [Input, Expected Output, User Output] 

def check_set(s,l):
    b = []
    for i in l:
        if i in b:
            return False
        b.append(i)
    return (set(b) == s)

def check_set_power(l1,l2):
    b = []
    for i in l1:
        b.append(set(i))
    for i in l2:
        found = False
        for j in range(0,len(b)):
            if(check_set(b[j],i)):
                found = True
                del b[j]
                break
        if not found:
            return False
    return (len(b) == 0)

def helper(fn):
    s = '-' * 30
    print (f'\n{s} Testing for {fn} {s}')

def test_emptyset():
    helper("emptyset")
    
    s = 0
    try:
        with time_limit(1):
            user_output = col100_module.emptyset()
            if(user_output == []):
                s = s + 1    
            print(f'Function: emptyset, Verdict: {len(user_output) == 0}')
    except Exception as e:
        print(traceback.format_exc())
    return s

def test_isEmpty():
    helper("isEmpty")
    s = 0
    xl = [[], [1,2,4]]
    expected_output = [True, False]
    #user_output = [col100_module.isEmpty(x) for x in xl]
    for i in range(0,len(xl)):
        try:
            with time_limit(1):
                user_output = col100_module.isEmpty(xl[i])
                if(expected_output[i] == user_output):
                    s = s + 1
                print(f'Function: isEmpty, Input: {xl[i]}\nExpected Output: {expected_output[i]} User Output: {user_output}, Verdict: {expected_output[i] == user_output}')
        except Exception as e:
            print(traceback.format_exc())
    return s/len(xl)
        
def test_member():
    helper("member")
    s = 0
    x1l = [[],[1,2,3],[1,2,3],["col","mtl"],["Alan turing","Tim Berners-Lee"],[(4,"mtl"),(4,"col"),(2,"cmp")],[(4,"mtl"),(4,"col"),(2,"cmp")]]
    x2l = [2,2,4,"COL","Alan turing",(100000,"col"),(4,"col")]
    expected_output = [False, True, False, False, True, False, True]
    #user_output = [col100_module.member(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        try:
            with time_limit(1):
                user_output = col100_module.member(x1l[i],x2l[i])
                if(expected_output[i] == user_output):
                    s = s + 1
                print(f'Function: member, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output}, Verdict: {expected_output[i] == user_output}')
        except Exception as e:
            print(traceback.format_exc())
    return s/len(x1l)

def test_singleton():
    helper("singleton")
    s = 0
    xl = [0.0,23,'a',"Alan Turing",(2,"cmp")]
    expected_output = [[0.0],[23],['a'],["Alan Turing"],[(2,"cmp")]]
    #user_output = [col100_module.singleton(x) for x in xl]
    for i in range(0,len(xl)):
        try:
            with time_limit(1):
                user_output = col100_module.singleton(xl[i])
                if(expected_output[i] == user_output):
                    s = s + 1
                print(f'Function: singleton, Input: {xl[i]}\nExpected Output: {expected_output[i]} User Output: {user_output}, Verdict: {expected_output[i] == user_output}')
        except Exception as e:
            print(traceback.format_exc())
    return s/len(xl)
        
def test_isSubset():
    helper("isSubset")
    s = 0
    x2l = [["Yudhishthir", "Bhim", "Arjun", "Nakul", "Sahadev"],["Yudhishthir", "Bhim", "Arjun", "Nakul", "Sahadev"],
    [1,2,3,5,8], [(0,"Aryabhatta "), (1729,"Ramanujan")],[(0,"Aryabhatta "), (1729,"Ramanujan")]]
    x1l = [["Arjun","Karn"],[],[2],[(66,"Belphegor")],[(0,"Aryabhatta ")]]
    expected_output = [False, True, True, False, True]
    #user_output = [col100_module.isSubset(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        try:
            with time_limit(1):
                user_output = col100_module.isSubset(x1l[i],x2l[i])
                if(expected_output[i] == user_output):
                    s = s + 1
                print(f'Function: isSubset, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output}, Verdict: {expected_output[i] == user_output}')
        except Exception as e:
            print(traceback.format_exc())
    return s/len(x1l)

def test_setEqual():
    helper("setEqual")
    s = 0
    x1l = [["virat","dhoni","sachin","rohit"], [1.0,-1.0],[]]
    x2l = [["sachin","dhoni","virat","rohit"],[-1.0,1.0],["its empty"]]
    expected_output = [True, True, False]
    #user_output = [col100_module.setEqual(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        try:
            with time_limit(1):
                user_output = col100_module.setEqual(x1l[i],x2l[i])
                if(expected_output[i] == user_output):
                    s = s + 1
                print(f'Function: setEqual, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output}, Verdict: {expected_output[i] == user_output}')
        except Exception as e:
            print(traceback.format_exc())
    return s/len(x1l)

def test_union():
    helper("union")
    s = 0
    x1l = [["virat","sachin"], [1.0,-1.0,2.0,3.0],[]]
    x2l = [["dhoni","bumrah"],[-1.0,1.0],["its empty"]]
    expected_output = [["virat","dhoni","sachin","bumrah"], [1.0,-1.0,2.0,3.0], ["its empty"]]
    #user_output = [col100_module.union(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        try:
            with time_limit(1):
                user_output = col100_module.union(x1l[i],x2l[i])
                result = check_set(set(expected_output[i]),user_output)
                if(result):
                    s = s + 1
                print(f'Function: union, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output}, Verdict: {result}')
        except Exception as e:
            print(traceback.format_exc())
    return s/len(x1l)

def test_intersection():
    helper("intersection")
    s = 0
    x1l = [["delhi","mumbai","banglore"], [1.0,-1.0,2.0,3.0],[]]
    x2l = [["delhi","kolkata"],[-1.0,1.0],["its empty"]]
    expected_output = [["delhi"], [1.0,-1.0], []]
    #user_output = [col100_module.intersection(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        try:
            with time_limit(1):
                user_output = col100_module.intersection(x1l[i],x2l[i])
                result = check_set(set(expected_output[i]),user_output)
                if(result):
                    s = s + 1
                print(f'Function: intersection, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output}, Verdict: {result}')
        except Exception as e:
            print(traceback.format_exc())
    return s/len(x1l)
def test_cartesian():
    helper("cartesian")
    s = 0
    x1l = [[1,2,3], [2,1],[]]
    x2l = [[1],["a","b"],["its empty"]]
    expected_output = [[(1,1),(2,1),(3,1)], [(2,"a"),(1,"a"),(1,"b"),(2,"b")], []]
    #user_output = [col100_module.cartesian(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        try:
            with time_limit(1):
                user_output = col100_module.cartesian(x1l[i],x2l[i])
                result = check_set(set(expected_output[i]),user_output)
                if(result):
                    s = s + 1
                print(f'Function: cartesian, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output}, Verdict: {result}')
        except Exception as e:
            print(traceback.format_exc())
    return s/len(x1l)

def test_power():
    helper("power")
    s = 0
    x1l = [[1,2,3], [1,2],[],["C","D"], [('C',1),('C',2)],[1,2,3,8], [1.0,2.0,3.0,4.0,5.0]]
    expected_output = [[[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]],[[],[1],[1,2],[2]],[[]],[[],['C'],['C','D'],['D']],[[], [('C', 1)], [('C', 1), ('C', 2)], [('C', 2)]],[[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 8], [1, 2, 8], [1, 3], [1, 3, 8], [1, 8], [2], [2, 3], [2, 3, 8], [2, 8], [3], [3, 8], [8]],[[], [1.0], [1.0, 2.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0, 4.0], [1.0, 2.0, 3.0, 4.0, 5.0], [1.0, 2.0, 3.0, 5.0], [1.0, 2.0, 4.0], [1.0, 2.0, 4.0, 5.0], [1.0, 2.0, 5.0], [1.0, 3.0], [1.0, 3.0, 4.0], [1.0, 3.0, 4.0, 5.0], [1.0, 3.0, 5.0], [1.0, 4.0], [1.0, 4.0, 5.0], [1.0, 5.0], [2.0], [2.0, 3.0], [2.0, 3.0, 4.0], [2.0, 3.0, 4.0, 5.0], [2.0, 3.0, 5.0], [2.0, 4.0], [2.0, 4.0, 5.0], [2.0, 5.0], [3.0], [3.0, 4.0], [3.0, 4.0, 5.0], [3.0, 5.0], [4.0], [4.0, 5.0], [5.0]]]
    #user_output = [col100_module.power(x1l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        try:
            with time_limit(1):
                user_output = col100_module.power(x1l[i])
                result = check_set_power(expected_output[i],user_output)
                if(result):
                    s = s + 1
                print(f'Function: power, Input: {x1l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output}, Verdict: {result}')
        except Exception as e:
            print(traceback.format_exc())
    return s/len(x1l)

def test_emptyset_2():
    helper("emptyset_2")
    s = 0
    #user_output = col100_module.emptyset_2()
    try:
        with time_limit(1):
            user_output = col100_module.emptyset_2()
            if(user_output == []):
                s = s + 1    
            print(f'Function: emptyset_2, Verdict: {len(user_output) == 0}')
    except Exception as e:
        print(traceback.format_exc())
    return s

def test_isEmpty_2():
    helper("isEmpty_2")
    s = 0
    xl = [[], [1,2,4], ["A","B"],['a','c']]
    expected_output = [True, False, False, False]
    #user_output = [col100_module.isEmpty_2(x) for x in xl]
    for i in range(0,len(xl)):
        try:
            with time_limit(1):
                user_output = col100_module.isEmpty_2(xl[i])
                if(expected_output[i] == user_output):
                    s = s + 1
                print(f'Function: isEmpty_2, Input: {xl[i]}\nExpected Output: {expected_output[i]} User Output: {user_output}, Verdict: {expected_output[i] == user_output}')
        except Exception as e:
            print(traceback.format_exc())
    return s/len(xl)

def test_member_2():
    helper("member_2")
    s = 0
    x1l = [[],[1,2,3],[1,2,3],["col","mtl"],["Alan turing","Tim Berners-Lee"],[(2,"cmp"),(4,"col"),(4,"mtl")],[(2,"cmp"),(4,"col"),(4,"mtl")]]
    x2l = [2,2,4,"COL","Alan turing",(100000,"col"),(4,"col")]
    expected_output = [False, True, False, False, True, False, True]
    #user_output = [col100_module.member_2(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        try:
            with time_limit(1):
                user_output = col100_module.member_2(x1l[i],x2l[i])
                if(expected_output[i] == user_output):
                    s = s + 1
                print(f'Function: member_2, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output}, Verdict: {expected_output[i] == user_output}')
        except Exception as e:
            print(traceback.format_exc())
    return s/len(x1l)

def test_singleton_2():
    helper("singleton_2")
    s = 0
    xl = [0.0,23,'a',"Alan Turing",(2,"cmp")]
    expected_output = [[0.0],[23],['a'],["Alan Turing"],[(2,"cmp")]]
    #user_output = [col100_module.singleton_2(x) for x in xl]
    for i in range(0,len(xl)):
        try:
            with time_limit(1):
                user_output = col100_module.singleton_2(xl[i])
                if(expected_output[i] == user_output):
                    s = s + 1
                print(f'Function: singleton_2, Input: {xl[i]}\nExpected Output: {expected_output[i]} User Output: {user_output}, Verdict: {expected_output[i] == user_output}')
        except Exception as e:
            print(traceback.format_exc())
    return s/len(xl)
def test_isSubset_2():
    helper("isSubset_2")
    s = 0
    x2l = [["Arjun","Bhim" ,"Nakul","Sahadev","Yudhishthir"],["Arjun","Bhim" ,"Nakul","Sahadev","Yudhishthir"],
    [1,2,3,5,8], [(0,"Aryabhatta "), (1729,"Ramanujan")],[(0,"Aryabhatta "), (1729,"Ramanujan")]]
    x1l = [["Arjun","Karn"],[],[2],[(66,"Belphegor")],[(0,"Aryabhatta "),(1729,"Ramanujan")]]
    expected_output = [False, True, True, False, True]
    user_output = [col100_module.isSubset_2(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        try:
            with time_limit(1):
                user_output = col100_module.isSubset_2(x1l[i],x2l[i])
                if(expected_output[i] == user_output):
                    s = s + 1
                print(f'Function: isSubset_2, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output}, Verdict: {expected_output[i] == user_output}')
        except Exception as e:
            print(traceback.format_exc())
    return s/len(x1l)

def test_setEqual_2():
    helper("setEqual_2")
    s = 0
    x1l = [["dhoni","rohit","sachin","virat"], [-1.0,1.0],[]]
    x2l = [["dhoni","rohit","sachin"],[-1.0,1.0],["its empty"]]
    expected_output = [False, True, False]
    #user_output = [col100_module.setEqual_2(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        try:
            with time_limit(1):
                user_output = col100_module.setEqual_2(x1l[i],x2l[i])
                if(expected_output[i] == user_output):
                    s = s + 1
                print(f'Function: setEqual_2, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output}, Verdict: {expected_output[i] == user_output}')
        except Exception as e:
            print(traceback.format_exc())
    return s/len(x1l)

def test_union_2():
    helper("union_2")
    s  =0
    x1l = [["sachin","virat"], [-1.0,1.0,2.0,3.0],[]]
    x2l = [["bumrah","dhoni"],[-1.0,1.0],["its empty"]]
    expected_output = [["bumrah","dhoni","sachin","virat"], [-1.0,1.0,2.0,3.0], ["its empty"]]
    #user_output = [col100_module.union_2(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        try:
            with time_limit(1):
                user_output = col100_module.union_2(x1l[i],x2l[i])
                if(expected_output[i] == user_output):
                    s = s + 1
                print(f'Function: union_2, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output}, Verdict: {expected_output[i] == user_output}')
        except Exception as e:
            print(traceback.format_exc())
    return s/len(x1l)
def test_intersection_2():
    helper("intersection_2")
    s = 0
    x1l = [["banglore","delhi","mumbai"], [-1.0,1.0,2.0,3.0],[]]
    x2l = [["delhi","kolkata"],[-1.0,1.0],["its empty"]]
    expected_output = [["delhi"], [-1.0,1.0], []]
    #user_output = [col100_module.intersection_2(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        try:
            with time_limit(1):
                user_output = col100_module.intersection_2(x1l[i],x2l[i])
                if(expected_output[i] == user_output):
                    s = s + 1
                print(f'Function: intersection_2, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output}, Verdict: {expected_output[i] == user_output}')
        except Exception as e:
            print(traceback.format_exc())
    return s/len(x1l)

def test_cartesian_2():
    helper("cartesian_2")
    s = 0
    x1l = [[1,2,3], [1,2],[]]
    x2l = [[1],["a","b"],["its empty"]]
    expected_output = [[(1,1),(2,1),(3,1)], [(1,"a"),(1,"b"),(2,"a"),(2,"b")], []]
    #user_output = [col100_module.cartesian_2(x1l[i],x2l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        try:
            with time_limit(1):
                user_output = col100_module.cartesian_2(x1l[i],x2l[i])
                if(expected_output[i] == user_output):
                    s = s + 1
                print(f'Function: cartesian_2, Input: {x1l[i],x2l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output}, Verdict: {expected_output[i] == user_output}')
        except Exception as e:
            print(traceback.format_exc())
    return s/len(x1l)

def test_power_2():
    s = 0
    helper("power_2")
    x1l = [[1,2,3], [1,2],[],["C","D"], [('C',1),('C',2)],[1,2,3,8], [1.0,2.0,3.0,4.0,5.0]]
    expected_output = [[[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]],[[],[1],[1,2],[2]],[[]],[[],['C'],['C','D'],['D']],[[], [('C', 1)], [('C', 1), ('C', 2)], [('C', 2)]],[[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 8], [1, 2, 8], [1, 3], [1, 3, 8], [1, 8], [2], [2, 3], [2, 3, 8], [2, 8], [3], [3, 8], [8]],[[], [1.0], [1.0, 2.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0, 4.0], [1.0, 2.0, 3.0, 4.0, 5.0], [1.0, 2.0, 3.0, 5.0], [1.0, 2.0, 4.0], [1.0, 2.0, 4.0, 5.0], [1.0, 2.0, 5.0], [1.0, 3.0], [1.0, 3.0, 4.0], [1.0, 3.0, 4.0, 5.0], [1.0, 3.0, 5.0], [1.0, 4.0], [1.0, 4.0, 5.0], [1.0, 5.0], [2.0], [2.0, 3.0], [2.0, 3.0, 4.0], [2.0, 3.0, 4.0, 5.0], [2.0, 3.0, 5.0], [2.0, 4.0], [2.0, 4.0, 5.0], [2.0, 5.0], [3.0], [3.0, 4.0], [3.0, 4.0, 5.0], [3.0, 5.0], [4.0], [4.0, 5.0], [5.0]]]
    #user_output = [col100_module.power_2(x1l[i]) for i in range(0,len(x1l))]
    for i in range(0,len(x1l)):
        try:
            with time_limit(1):
                user_output = col100_module.power_2(x1l[i])
                if(expected_output[i] == user_output):
                    s = s + 1
                print(f'Function: power_2, Input: {x1l[i]}\nExpected Output: {expected_output[i]} User Output: {user_output}, Verdict: {expected_output[i] == user_output}')
        except Exception as e:
            print(traceback.format_exc())
    return s/len(x1l)
##############################################################################################################################################################
#DO NOT TOUCH ANY CODE LINE ABOVE THIS


import signal
from contextlib import contextmanager

class TimeoutException(Exception): pass

@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)

emptyset_s = 0
isEmpty_s = 0
member_s = 0
singleton_s = 0 
isSubset_s = 0 
setEqual_s = 0
union_s = 0
intersection_s = 0
cartesian_s = 0
power_s = 0

emptyset_2_s = 0
isEmpty_2_s = 0
member_2_s = 0
singleton_2_s = 0 
isSubset_2_s = 0 
setEqual_2_s = 0
union_2_s = 0
intersection_2_s = 0
cartesian_2_s = 0
power_2_s = 0
fs = 0
helper("Part 1")

try:
    emptyset_s= emptyset_w*test_emptyset() 
    print("\nEmpty Set Score: ",0.6*emptyset_s)	
except Exception as e:
    print(traceback.format_exc())    

try:
    isEmpty_s = isEmpty_w*test_isEmpty()
    print("\nIsEmpty Score: ",0.6*isEmpty_s)	
except Exception as e:
    print(traceback.format_exc())  

try:
    member_s = member_w*test_member()
    print("\nTest Member Score: ",0.6*member_s)
except Exception as e:
    print(traceback.format_exc())  

try:
    singleton_s = singleton_w*test_singleton()
    print("\nTest Singleton Score: ",0.6*singleton_s)
except Exception as e:
    print(traceback.format_exc())

try:
    isSubset_s = isSubset_w*test_isSubset()
    print("\nTest Is_Subset Score: ",0.6*isSubset_s)
except Exception as e:
    print(traceback.format_exc())

try:
    setEqual_s = setEqual_w*test_setEqual()
    print("\nTest set Equal Score: ",0.6*setEqual_s)
except Exception as e:
    print(traceback.format_exc())

try:
    union_s = union_w*test_union()
    print("\nTest Union Score: ",0.6*union_s)
except Exception as e:
    print(traceback.format_exc())

try:
    intersection_s = intersection_w*test_intersection()
    print("\nTest Union Score: ",0.6*intersection_s)
except Exception as e:
    print(traceback.format_exc())

try:
    cartesian_s=cartesian_w*test_cartesian()
    print("\nTest Cartesian Score: ",0.6*cartesian_s)
except Exception as e:
    print(traceback.format_exc())

try:
    power_s=power_w*test_power()
    print("\nTest Power Score: ",0.6*power_s)
except Exception as e:
    print(traceback.format_exc())

helper("Part 2") 

try:
    emptyset_2_s= emptyset_2_w*test_emptyset_2()   
    print("\nTest Empty Set2 Score: ",0.6*emptyset_2_s)
except Exception as e:
    print(traceback.format_exc())    

try:
    isEmpty_2_s = isEmpty_2_w*test_isEmpty_2()
    print("\nTest Is Empty2 Score: ",0.6*isEmpty_2_s)
except Exception as e:
    print(traceback.format_exc())

try:
    member_2_s= member_2_w*test_member_2()
    print("\nTest Member2 Score: ",0.6*member_2_s)
except Exception as e:
    print(traceback.format_exc())  

try:
    singleton_2_s=singleton_2_w*test_singleton_2()
    print("\nTest Singleton2 Score: ",0.6*singleton_2_s)

except Exception as e:
    print(traceback.format_exc())

try:
    isSubset_2_s=isSubset_2_w*test_isSubset_2()
    print("\nTest Is subset2 Score: ",0.6*isSubset_2_s)
except Exception as e:
    print(traceback.format_exc())

try:
    setEqual_2_s=setEqual_2_w*test_setEqual_2()
    print("\nTest Set Equal2 Score: ",0.6*setEqual_2_s)
except Exception as e:
    print(traceback.format_exc())


try:
    union_2_s=union_2_w*test_union_2()
    print("\nTest Union2 Score: ",0.6*union_2_s)
except Exception as e:
    print(traceback.format_exc())

try:
    intersection_2_s=intersection_2_w*test_intersection_2()
    print("\nTest Intersection_2 Score: ",0.6*intersection_2_s)
except Exception as e:
    print(traceback.format_exc())

try:
    cartesian_2_s=cartesian_2_w*test_cartesian_2()
    print("\nTest Cartesian2 Score: ",0.6*cartesian_2_s)
except Exception as e:
    print(traceback.format_exc())

try:
    power_2_s=power_2_w*test_power_2()
    print("\nTest Power2 Score: ",0.6*power_2_s)
except Exception as e:
    print(traceback.format_exc())

part1_fs=0
part2_fs=0

part1_score_list=[emptyset_s, isEmpty_s,member_s,singleton_s,isSubset_s,setEqual_s,union_s,intersection_s,cartesian_s,power_s]

part2_score_list=[emptyset_2_s,isEmpty_2_s,member_2_s,singleton_2_s,isSubset_2_s,setEqual_2_s,union_2_s,intersection_2_s,cartesian_2_s,power_2_s]

for score in part1_score_list:
    part1_fs=part1_fs+score

for score in part2_score_list:
    part2_fs=part2_fs+score

fs=part1_fs+part2_fs


print("\n\nPart1 SCORE = "+str(part1_fs*0.6)+ "/66.0\n")
print("\n\nPart2 SCORE = "+str(part2_fs*0.6)+ "/69.0\n")
print("\n\nFINAL SCORE = "+str(fs*0.6)+ "/135.0\n")