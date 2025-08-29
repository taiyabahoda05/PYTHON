# def show(n):
#     if (n == 0):
#         return
#     print(n)
#     show(n-1)

# show(5)

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return fact(n-1) * n
    
# print(fact(7))

# def sum(n):
#     if (n==0):
#         return 0
#     return sum(n-1) + n

# print(sum(5))

def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print (list[idx])
    print_list(list,idx+1)

fruits = ["mango","apple","orange","banana","strawberry"]
print_list(fruits)