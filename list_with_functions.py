#list 
#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert',
#'pop', 'remove', 'reverse', 'sort'
a=[1,2,3,4,3,3,3,3,3,3,5,6,71,2,3,4,5,6,7,8]
b=[1,2,3,4,3,7]
#print(type(a))
#print(dir(a))

#  Append object to the end of the list.
#a.append(90)
#print(a)

#Remove all items from list.
#a.clear()
#print(a)
#print(help(a.clear))

#b=a.copy()
#print(b)
#print(help(a.copy))

#Return number of occurrences of value

#print(a.count(3))
#print(help(a.count))

#Extend list by appending elements from the iterable.

#a.extend(b)
#print(a)
#print(help(a.extend))

#print(a.index(3))


#a.insert(2,[999,1,2,3,5,6,7,87,4])
#print(a)
#print(help(a.insert))


# Remove and return item at index (default last).
#a.pop()
#print(a.pop())
#print(help(a.pop))

#a.remove(3)
#print(a)
#print(help(a.remove))


a.sort(reverse=True)
print(a)
#print(help(a.sort))
#a.reverse()
#print(a)
#print(help(a.sort))