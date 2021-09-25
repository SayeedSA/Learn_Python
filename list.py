#list is a collection
#list duplicate value allow kore
#list ordered
#list changable
#list ke amra star button a represent korbo

list = [1,1,1,12,4.5,6,20,22,'sabbir']
print(list) #python a list a datatype a jhamela kore na
print(list.remove(list[3]))
list1 = [1,['sayeed',5,34,60],12,4.5,6,20,22,'sabbir'] #nested list
print(list1)
print(list1[1])
print(list1[1][3]) #see nested list value one by one

list = list + [1,2,3,4] #add two list
print(list)
list.extend([3,4,5,6,7,8]) #add two list using build in function
print(list)
list.remove(1)
print(list) #ai vbe remove korle 1st index just remove korbe

list.remove(list[3])
print(list)
#list.count(1) #count value
#print(print(list)