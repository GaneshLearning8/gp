# # Operators

# #arithmetic operators: addition(+), subtract(-), multiply(*), division(/), floor division(//)
# x = 2+1
# print(x+1)
# print(x-1)
# print(x*1)
# print(x/1)
# print(x//1)


# #assignment operators: =, +=, -=, *=, /=
# # result = 5
# # # result = result + 1
# # result += 1
# # print(result)

# result = 5
# result += 1
# print(result)

# result = 5
# result = result + 1
# result -= 1
# print(result)

# result = 5
# result *= 2
# print(result)

# result = 5
# result /= 2
# print(result)

# result = 5
# result //= 2
# print(result)

#comparision operators: ==, <=, >=, <, >
   
result:int = 5
if result == 2:
    print("False")
else:
    print(result)
# print(result)

result:int= 5
if result <= 2:
    print("False")
else:
    print(result)

result:int= 5
if result >= 2:
    print("true")

   
result:int = 5
if result > 2:
    print("true")


result:int= 5
if result < 2:
    print("False")
else:
    print(result)

# #membership operator: in, not in

# x = "My Office Time Is 11:00 AM In The Morning"
# result= x
# print('11AM'in result)
# print('11AM'in x)
# print('11:00 AM'in result)
# print('11:00 AM'in x)

print('11:00 AM'not in result)
print('11:00 AM'not in x)
print('11AM'not in result)
print('11AM'not in x)

# #idenity operator: is, is not

# x = "My Office Time Is 11:00 AM In The Morning"
# result= x

# print(id(x), id(result))

# print(id(x) is id(result))
# print(id(x) is not id(result))
