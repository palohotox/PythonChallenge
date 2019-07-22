
from functools import reduce

#using reduce methode from functols
product = reduce((lambda x, y: x / y), [2, 2, 2, 2])
print(product)


lambda x, y: x / y



"""
#Multiply all elements in the list
def multpList(list1) :
    sumList=1
    for a in list1:
        sumList *= a
    return sumList

list1 =[3,3,3]


print (multpList(list1))
#sum(list1) # sum all the elements in the list



#print(sum(list1))



#sum all elements in the list
str1 = [1,2,3,4,4.4,"e","r","g","r"]
strl2 = [i for i in str1 if isinstance(i,int)]
print(sum(strl2))
"""
