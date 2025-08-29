# with open("practice.txt","r") as f:
#     data=f.read()

# new_data = data.replace("Java","Python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)

# def check_for_word():
#     word = "learning"
#     with open("practice.txt","r") as f:
#         data=f.read()
#         if (word in data):
#             print("Found")
#         else:
#             print("Not found")
# check_for_word()
    
# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no+=1
#     return -1
# print(check_for_line())

count = 0
with open("practice.txt","r") as f:
    data=f.read()

nums = data.split(",")
for i in nums:
    if(int(i)%2 == 0 ):
        count +=1
print(count)   