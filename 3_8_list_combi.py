list1=["Name","Rollno"]
list2=['Srikanth',12345]
print("List 1 elements are: ",list1)
print("List 2 elements are: ",list2)
dict={}
for key in list1:
    for value in list2:
        dict[key]=value
        list2.remove(value)
        break
print("Dictionary from two lists is :",dict)
