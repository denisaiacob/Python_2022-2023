'''
Write a function that receives as a parameters a list of musical notes (strings),
a list of moves (integers) and a start position (integer). The function will return the song composed by
going though the musical notes beginning with the start position and following the moves given as parameter.
'''


def song(notes, moves, position):
    songComposed = [notes[position]]
    for i in moves:
        position = (position + i) % len(notes)
        songComposed.append(notes[position])
    return songComposed


if __name__ == '__main__':
    notes = ["do", "re", "mi", "fa", "sol"]
    moves = [1, -3, 4, 2]
    startPosition = 2
    print(song(notes, moves, startPosition))
