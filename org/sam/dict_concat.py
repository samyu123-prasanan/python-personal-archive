my_dict = {'name':'Tushara', 'age': 12, 'name':'samyuktha'}

print(my_dict)
# Output: Jack
print(my_dict['name'])

# Output: 26
#print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error
# my_dict.get('address')
# my_dict['address']

dict1 = {'address':'Tambaram', 'ph':9876543210}

print(dict1)

dict2 = {}

dict2.update(my_dict)

dict2.update(dict1)

print(dict2)