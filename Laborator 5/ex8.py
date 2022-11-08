'''
a) Write a function called print_arguments with one parameter named function. The function will return one new function
which prints the arguments and the keyword arguments received and will return the output of the function receives as a parameter.
b) Write a function called multiply_output with one parameter named function. The function will return one new function
which returns the output of the function received multiplied by 2.
c) Write a function called augment_function with two parameters named function and decorators. decorators will be a list
of functions which will have the same signature as the previous functions (print_arguments, multiply_output).
augment_function will create a new function which is augmented using all the functions in the decorators list.
'''


def multiply_by_two(x):
    return x * 2


def add_numbers(a, b):
    return a + b


def multiply_by_three(x):
    return x * 3


def add_numbers(a, b):
    return a + b


def print_arguments(function):
    def newfunction(*args, **kwargs):
        print("Arguments are:", args, kwargs)
        return function(*args, **kwargs)

    return newfunction


def multiply_output(function):
    def newfunction(*args, **kwargs):
        return 2 * function(*args, **kwargs)

    return newfunction


def augment_function(function, decorators):
    def newfunction(*args, **kwargs):
        for i in decorators:
            x = i(function)
            print(x(*args, **kwargs))

    return newfunction


if __name__ == "__main__":
    # a
    augmented_multiply_by_two = print_arguments(multiply_by_two)
    print(augmented_multiply_by_two(10))
    augmented_add_numbers = print_arguments(add_numbers)
    print(augmented_add_numbers(3, 4))
    # b
    augmented_multiply_by_three = multiply_output(multiply_by_three)
    print(augmented_multiply_by_three(10))
    # c
    decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])
    print(decorated_function(3, 4))
