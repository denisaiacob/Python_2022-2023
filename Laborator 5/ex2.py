'''
Create a function and an anonymous function that receive a variable number of arguments.
Both will return the sum of the values of the keyword arguments.
'''


def my_function(*args, **kwargs):
    sum = 0
    for key, value in kwargs.items():
        sum = sum + value
    return sum


if __name__ == "__main__":
    print(my_function(1, 2, c=3, d=4))
    exec("def num_sum(*args,**kwargs):return sum(kwargs.values())")
    print(num_sum(1, 2, c=3, d=4))
