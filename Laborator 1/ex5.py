if __name__ == "__main__":
    matrix = [['f', 'i', 'r', 's'],
              ['n', '_', 'l', 't'],
              ['o', 'b', 'a', '_'],
              ['h', 't', 'y', 'p']]

    n = 4
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1
    string = ''
    while 1:
        if left > right:
            break
        for i in range(left, right + 1):
            string = string + matrix[top][i]
        top = top + 1
        if top > bottom:
            break
        for i in range(top, bottom + 1):
            string = string + matrix[i][right]
        right = right - 1
        if left > right:
            break
        for i in range(right, left - 1, -1):
            string = string + matrix[bottom][i]
        bottom = bottom - 1
        if top > bottom:
            break
        for i in range(bottom, top - 1, -1):
            string = string + matrix[i][left]
        left = left + 1

    print(string)
