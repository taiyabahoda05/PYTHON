# dict = {                       #Dictionary is mutable
#     "name" : "taiyaba",
#     "course": "BCA",
#     "year": "second"
# }
# print(dict)

# student = {
#     "name": "aayat",
#     "subjects": {
#         "maths" : 75,
#         "english" : 80,
#         "hindi" : 85
#     }
# }

# print(student)

# set = {55,38,63,45}     #The elements of set are immutable but set is mutable and it cannot store duplicate values
# print(set)

# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.union(set2))    #{1,2,3,4}
# print(set1.intersection(set2))  #{2,3}

# set = {"python","java","c","java","python","javascript","c++","c"}
# print(len(set))

a = int(input("Enter marks of maths: "))     
b = int(input("Enter marks of english: "))
c = int(input("Enter marks of science: "))
dict = {}
dict.update({"Maths": a})
dict.update({"English": b})
dict.update({"Science": c})

print(dict)
