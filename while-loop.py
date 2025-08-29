# i=1
# while i<=100:
#     print(i)
#     i+=1

# i=100
# while i>=1:
#     print(i)
#     i-=1

# n = int(input("Enter a number: "))
# i=1
# while i<=10:
#     print(n,"X",i,"=",n*i)
#     i+=1

# i=1
# while i<=10:
#     print(i*i)
#     i+=1

# n = [1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx<len(n):
#     print(n[idx])
#     idx+=1

# n = (1,4,9,16,25,36,49,64,81,100)
# i=0
# x=25
# while i<len(n):
#     if(n[i] == x):
#         print("Found at index",i)
#     i+=1

# i=1
# while i<=10:
#     if(i%2 != 0):
#         i += 1
#         continue
#     print(i)
#     i +=1

n = int(input("Enter a number: "))
i = 1
sum = 0
while i<=n:
    sum += i
    i += 1
print(sum)
        