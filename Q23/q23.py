<<<<<<< HEAD
import random
=======
from itertools import permutations
import time
>>>>>>> 8964bf9965c45f4420326b380a0cd68528c4969b

word = ["D", "O", "D", "E", "C", "A", "H", "E", "D", "R", "O", "N"]

<<<<<<< HEAD
for i in range(100):
    randwordorder = random.shuffle(word)
    if randwordorder[0] == "D" and (randwordorder[0] == randwordorder[2] or randwordorder[0] == randwordorder[3] or randwordorder[0] == randwordorder[4] or randwordorder[0] == randwordorder[5] or randwordorder[0] == randwordorder[6] or randwordorder[0] == randwordorder[7]):
        
=======
possible_states = permutations(word)


def normalise_connections() -> list[list[int]]:
    connections = [
        # 1
        [2, 3, 10, 9, 12],
        [1, 12, 5, 4, 3],
        [1, 2, 4, 11, 10],
        [2, 3, 11, 6, 5],
        [2, 4, 6, 7, 12],
        [5, 7, 8, 11, 4],
        [5, 6, 8, 9, 12],
        [11, 10, 6, 9, 7],
        [1, 10, 8, 7, 12],
        [1, 3, 8, 9, 11],
        [3, 4, 6, 8, 10],
        [1, 2, 5, 9, 7],
    ]

    # Convert face numbers to face indexes
    connections_indexes = []
    for i in range(len(connections)):
        face_connections = []
        for j in range(len(connections[i])):
            face_num = connections[i][j]

            face_connections.append(face_num - 1)

        connections_indexes.append(face_connections)

    print(connections_indexes)

    return connections_indexes


connections = normalise_connections()


def d_not_connected(state: list[str], d_index: int) -> bool:
    face_connections = connections[d_index]

    for connection in face_connections:
        if connection >= len(state):
            print(d_index, state, connection)

        letter = state[connection]

        if letter == "D":
            return False

    return True


def o_connected(state: list[str], d_index: int) -> bool:
    face_connections = connections[d_index]

    for connection in face_connections:
        letter = state[connection]

        if letter == "O":
            return True

    return False


total = 0
for _ in possible_states:
    total += 1

possible_states = permutations(word)


current = 0
valid = 0

start = time.time()
last_print = time.time()
last_percent = 0
print("Evalulating states")
for state in possible_states:
    current += 1

    if time.time() > last_print + 1:
        percent = (current * 100) / total
        delta_percent = percent - last_percent
        left = 100 - percent

        sec_left = left / delta_percent
        min_left = sec_left / 60

        print(f"Completed: {percent:.2f}%, ETA: {sec_left:.2f}s or {min_left:.2f}")
        last_percent = percent

        last_print = time.time()

    d_indexes = []
    o_indexes = []

    valid_d = True
    valid_o = True

    for index, letter in enumerate(state):
        if letter == "D":
            d_indexes.append(index)
        elif letter == "O":
            o_indexes.append(index)

    for d_index in d_indexes:
        if not d_not_connected(state, d_index):
            valid_d = False
            break

    if not valid_d:
        continue

    for o_index in o_indexes:
        if not o_connected(state, o_index):
            valid_o = False
            break

    if not valid_o:
        continue

    valid += 1

end = time.time()

print(f"Time taken: {end - start:.2f}")
print(
    f"Evaluated: {total} and found {valid} valid. Therefore, probability: {valid / total:.2f}"
)

# print(valid, total, valid / total)
>>>>>>> 8964bf9965c45f4420326b380a0cd68528c4969b
