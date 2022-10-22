'''
The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules for a dictionary that has strings as keys and values)
and a dictionary. A rule is defined as follows: (key, "prefix", "middle", "suffix").
A value is considered valid if it starts with "prefix", "middle" is inside the value (not at the beginning or end) and ends with "suffix".
The function will return True if the given dictionary matches all the rules, False otherwise.
'''


def validate_dict(rules, d):
    for i in d:
        ok = 0
        for j in rules:
            if j[0] == i:
                ok = 1
                if j[3] != "" and d.get(i).endswith(j[3]) == False:
                    return False
                if j[1] != "" and d.get(i).startswith(j[1]) == False:
                    return False
                if j[2] != "":
                    if d.get(i).find(j[2]) == -1 or d.get(i).startswith(j[2]) or d.get(i).endswith(j[2]):
                        return False
        if ok == 0:
            return False
    return True


if __name__ == '__main__':
    rules = {("key1", "", "inside", ""), ("key2", "", "middle", "winter")}
    # d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
    d = {"key1": "come inside, it's too cold out", "key2": "middle winter"}
    print(validate_dict(rules, d))
