nums: list[int] = [1, 2,3,4, 5,6,7,8]
# even_list = []

# for num in nums:
#     if num % 2 == 0:
#         even_list.append(num)

# print(even_list)

# even_nums = [num for num in nums if num % 2 == 0]
# print(even_nums)


# odd_nums = [num for num in nums if num % 2 != 0]
# print(odd_nums)

even_list = []
odd_list = []
for num in nums:
     if num % 2 == 0:
        even_list.append(num)
        print("{0} is Even".format(num))
     else:
       odd_list.append(num)
       print("{0} is Odd".format(num))

print(even_list)
print(odd_list)