'''
Iterators can be used to a lot of iterable objects
Using iter() we create an iterator of an object
The next() when used with an iterator will return the next value
'''

example_tuple = (1,2,3)
example_string = "some words"
example_list = ["a", "b", "c", 1]

tuple_iterator = iter(example_tuple)
string_iterator = iter(example_string)
list_iterator = iter(example_list)

print(next(tuple_iterator))
print(next(string_iterator))
print(next(list_iterator))

