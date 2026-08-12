# Data ko structure way me present krne ko datastructures kehte hai.
# Data ko efficiently store krne aur access krne ke liye data structures ka use kiya jata hai.
# list,tupple,dict,set ye 4 data structures hai.
# custom data structures bhi banaye ja sakte hai. stack,queue,linked list,tree,graph ye data structures bhi hai.

## List data structure. 
# ye mutable data structure hai. ap kisi bhi value ko change kar sakte ho.
# list me duplicate values store ki ja sakti hai. same value accuring multiple times in the list.
# list me indexing hoti hai. list me heterogeneous data store kiya ja sakta hai. we can save different types of data in the same list.like int,float,string etc.
# ordered data structure hai. list me order maintain hota hai. list me values ko access karne ke liye indexing ka use kiya jata hai.

# a=[12,4,5,6,7]
# fruits=['apple','banana','mango','grapes']
# print(a[0]) ## 12
# print(fruits[1]) ## banana
# print(a[-1]) ## 7
# print(fruits[0:3]) ## ['apple', 'banana', 'mango']

a=[12,4,5,6,7,34.5]

#  #1st way to print list values using indexing
# for i in range(len(a)):
#     print(a[i])

# 2nd way to print list values using for loop
# for i in a:
#     print(i)

# print(dir(list)) ## list ke methods ko dekhne ke liye dir() ka use kiya jata hai.

# help(list) ## list ke methods ke baare me detail me janne ke liye help() ka use kiya jata hai.
l=[1,2,3,4,5]
print(l)
# l.append(6) ## append() method ka use list me new value add karne ke liye kiya jata hai.
print(l) ## [1, 2, 3, 4, 5, 6]
l.insert(2,10) ## insert() method ka use list me new value add karne ke liye kiya jata hai. ye method 2 arguments leta hai. 1st argument me index aur 2nd argument me value.
print(l) ## [1, 2, 10, 3, 4, 5, 6]


# a=12,4,5,6,6
# print(a) ## tuple data structure