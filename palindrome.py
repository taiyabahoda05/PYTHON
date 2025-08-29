m1 = input("Enter 1st no.: ")
m2 = input("Enter 2nd no.: ")
m3 = input("Enter 3rd no.: ")
list1 = [ m1,m2,m3]
list2 = list1.copy()
list2.reverse()

if(list2 == list1):
    print("PALINDROME")
else:
    print("NOT A PALINDROME")