'''
Write a function called process that receives a variable number of keyword arguments
The function generates the first 1000 numbers of the Fibonacci sequence and then processes them in the following way:
If the function receives a parameter called filters, this will be a list of predicates (function receiving an argument
and returning True/False) and will retain from the generated numbers only those for which the predicates are True.
If the function receives a parameter called limit, it will return only that amount of numbers from the sequence.
If the function receives a parameter called offset, it will skip that number of entries from the beginning of the result list.
The function will return the processed numbers.
'''


def sum_digits(x):
    return sum(map(int, str(x)))


def process(**kwargs):
    fibonacci = [0, 1]
    offset = 0
    limit = 0
    for i in range(2, 1000):
        fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])
    for key, value in kwargs.items():
        if key == 'filters':
            for i in value:
                fibonacci = list(filter(i, fibonacci))
        if key == 'offset':
            offset = value
        if key == 'limit':
            limit = value
    for i in range(0, offset):
        fibonacci.remove(fibonacci[0])
    processedNumbers = []
    for i in range(0, limit):
        processedNumbers.append(fibonacci[i])
    return processedNumbers


if __name__ == "__main__":
    print(process(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20], limit=2,
                  offset=2))
