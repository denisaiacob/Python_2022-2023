'''
Write a function that will order a list of string tuples based on the 3rd
character of the 2nd element in the tuple
'''

def group_by_tuple(tupleList):
    tupleList.sort(key=lambda i: i[1][-1])
    return tupleList

if __name__ == '__main__':
    tupleList=[('abc', 'bcd'), ('abc', 'zza'),('aba', 'bcc')]
    print(group_by_tuple(tupleList))