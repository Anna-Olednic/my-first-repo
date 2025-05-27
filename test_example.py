# Input array
arr = [4, 4, 8, 3, 3, 3, 2, 4, 4]

# 1. Print every element of the array
print("All elements in the array:")
for element in arr:
    print(element)

# 2. Print the first 3 elements of the array
print("\nFirst 3 elements of the array:")
print(arr[:3])

# 3. Print the sum of all elements
total_sum = sum(arr)
print("\nSum of all elements:", total_sum)

# 4. Print the sum of all elements except those equal to 4
filtered_sum = sum(x for x in arr if x != 4)
print("Sum of elements excluding 4:", filtered_sum)

# myArray = [4, 4, 8, 3, 3, 3, 2, 4, 4]
# #
# # # for (i=0; i<10; i++);{
# # #     console.log(myArray[i])} JavaScript
# #
# for element in myArray:
#         print(element)
#
# for i in range(3):
#     print(myArray[i])

# import json
#
# with open('list.json', 'r') as json_file:
#     data = json.load(json_file)
#     print(data)

    # obj_variable = {
    #     "name", "id"
    # }
    # print(obj_variable)

import json

# Open and load the JSON file
with open('list.json', 'r') as json_file:
    data = json.load(json_file)

# Loop through each list item and print id and name
for item in data.get("lists", []):
    list_id = item.get("id")
    list_name = item.get("name")
    print(f"ID: {list_id}, Name: {list_name}")
