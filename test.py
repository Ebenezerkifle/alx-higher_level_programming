def my_function(counter=10):
    return counter + 1

print(my_function())
a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4], 'friends': [ { 'id': 82, 'name': "Bob" }, { 'id': 83, 'name': "Amy" } ] }
b=a.get('friends')[-1]["name"]
print (b)