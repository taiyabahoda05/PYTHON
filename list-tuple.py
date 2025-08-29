# list =[5,10,2,8,22]  #Lists are mutable

# list.append(3)  #[5,10,2,8,22,3]
# list.sort()     #[2, 3, 5, 8, 10, 22]
# list.sort(reverse=True)  #[22, 10, 8, 5, 3, 2]
# list.reverse()  #[2, 3, 5, 8, 10, 22]

# print(list)

# tup = (5,8,5,63)  #Tuples are immutable just like strings
# print(tup)
# print(type(tup))
# print(tup.index(5))
# print(tup.count(5))

# m1 = input("Enter 1st movie: ")     #question 1
# m2 = input("Enter 2nd movie: ")
# m3 = input("Enter 3rd movie: ")

# list = [m1,m2,m3]
# print(list)

# tup = ('c','d','a','a','b','b','a')   #question 2
# print(tup.count('a')) 

list = ['c','d','a','a','b','b','a']   #question 3
list.sort()
print(list)