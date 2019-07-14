
from array import *

def rotate_arr(myarray):

    lastel = myarray[-1]
    #insert last element to first position
    myarray.insert(0, lastel)

    myarray1 = myarray
    #remove last element of the new array
    myarray1.pop(len(myarray1)-1)
    myarray2=myarray1

    return myarray2

N = int(input("Input N :"))
myarray = array('i',[9,6,8,3,1])

x=1
while x < N :

    print(rotate_arr(myarray))
    x += 1

