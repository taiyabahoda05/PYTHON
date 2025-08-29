# num = [ 1,2,3,4,5]
# for val in num:
#     print(val)

# n = [1,4,9,16,25,36,49,64,81,100]
# for val in n:
#     print(val)

# n = (1,4,9,16,25,36,49,64,81,100)
# x=16
# for val in n:
#    if(val == x):
#     print("X found",val)

# for i in range(10):   #range(stop)
#     print(i)

# for i in range(3,10):   #range(start,stop)
#     print(i)

# for i in range(2,10,2):   #range(start,stop,step)
#     print(i)

# for i in range(1,101):   
#     print(i)

# for i in range(100,0,-1):   
#     print(i)

# n = int(input("Number: "))
# for i in range(1,11):
#     print(n,"X",i,"=",n*i)

n = int(input("Number: "))
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)