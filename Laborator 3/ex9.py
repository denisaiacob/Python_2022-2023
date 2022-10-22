'''
Write a function that receives a variable number of positional arguments and a variable number of keyword arguments
adn will return the number of positional arguments whose values can be found among keyword arguments values.
'''


def my_function(p, k):
    nr = 0
    for i in k.values():
        if p.count(i) > 0:
            nr = nr + 1
    return nr


if __name__ == '__main__':
    positionalArguments = [1, 2, 3, 4]
    keywordArguments = dict(x=1, y=2, z=3, w=5)
    print(my_function(positionalArguments, keywordArguments))
