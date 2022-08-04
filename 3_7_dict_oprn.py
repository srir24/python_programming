dict1={'Name':'Sri','Surname':'Kanth','Department':'Bio-Tech','Sem':3}
dict2={'Section':'K','Year':1}
dict3={'Sem':3,'Year':2}
print("The elements in dictionary 1 are: ",dict1)
print("The elements in dictionary 2 are: ",dict2)
print("The elements in dictionary 3 are: ",dict3)
c=len(dict1)
print("The length of dictionary 1 is : ",c)
d={**dict1,**dict2}
print("The concatenation of two dictionaries is: ",d)
dict1['College']='CBIT'
dict1['Class no']=203
print("The new elements of dictionary 1 are: ",dict1)
dict1.pop('Class no')
print("The elements in dictionary 1 after deleting particular element are: ",dict1)
dict1.update([dict3])
