'''
 Write a function that receives a single dict parameter named mapping.
 This dictionary always contains a string key "start". Starting with the value of this key you must obtain a list of objects
 by iterating over mapping in the following way: the value of the current key is the key for the next value, until you find a loop
 (a key that was visited before). The function must return the list of objects obtained as previously described.
'''


def loop(mapping):
    objectsList = []
    key = "start"
    ok = 1
    while ok == 1:
        key = mapping.get(key)
        if objectsList.count(key) == 1 or key == "start":
            ok = 0
        else:
            objectsList.append(key)
    return objectsList


if __name__ == '__main__':
    mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
    print(loop(mapping))
