'''
Iterators can be used to a lot of iterable objects
Using iter() we create an iterator of an object
The next() when used with an iterator will return the next value
When the iterable object has reached the final position the next call of 
next() will raise a StopIteration error
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


'''
The __iter__() method works as __init__() method and we can use it to initialize
any attribute we want. In __iter__() we have to return self.
The __next__() method is used to define what will happend when someone calls next()
at an iterable attribute. In this case we add some numbers and append to string.
'''
class Car:
    def __iter__(self):
        self.model = "Toyota"
        self.total_km = 3000
        return self
    
    def __next__(self):
        x = self.total_km
        y = self.model
        self.total_km += 1
        self.model += "1"
        return x, y
    

my_car = Car()
car_iterator = iter(my_car)

print(next(car_iterator))



'''
In this case we can add a statement to check when to raise the StopIteration error
'''
class Car:
    def __iter__(self):
        self.model = "Toyota"
        self.total_km = 3000
        return self
    
    def __next__(self):
        if self.total_km > 3010:
            raise StopIteration
        else:
            x = self.total_km
            y = self.model
            self.total_km += 1
            self.model += "1"
        return x, y
    

my_car = Car()
car_iterator = iter(my_car)

print(next(car_iterator))

#######