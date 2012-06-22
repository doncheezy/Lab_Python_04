
list1 = ['bananas','strawberries','apples','bread']
print "groceries = ",list1

list1.append('champagne')
print "latest update of groceries =",list1

del list1[3]
print "removing bread the list will be =",list1

list1.sort()
print "after sorting =",list1



print "The data structure I will use be a dictionary."

dict1 = {"apple":"7.3 ","bananas":"price - 5.5","bread":"1.0","carrots":"1.0","champagne":"20.90","strawberries":"32.6"}
print 'apples price', dict1["apple"]
print dict1.items()

dict1['strawberries']=63.43
print'new price of strawberries',dict1['strawberries']

dict1['chicken']=6.5
print'latest price of chicken',dict1['chicken']







