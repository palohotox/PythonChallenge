
from array import *

myarrA = array('i',[1,2,3,5,1,2,3,3,5,4,4,8])

#myarrA.count will give the number of occurence of each element in the array


for i in myarrA:
    #print(myarrA.count(i))

    if myarrA.count(i) < 2:
        print(i)