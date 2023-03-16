import readchar
import random
import os
# VARIABLES
position = [4, 2]
map_width = 20
map_height = 15
map_objects = []
eaten_objects = 1
tail_length = 0
tail = []
points = 0
randPosition = []
for a in range(1):
    randomx = random.randint(0, 19)
    randomy = random.randint(0, 14)
    randPosition.append((randomx, randomy))
    while randPosition in position or randPosition in tail:
        randomx = random.randint(0, 19)
        randomy = random.randint(0, 14)
    map_objects.append((randomx, randomy))
    randPosition.clear()
while True:
    # DIBUJAR EL MAPA
    if position in tail:
        print("HAS PERDIDO")
        break
    if len(map_objects) == 0:
        print("HAS GANADO")
        break
    print("-" * 3 * (map_width + 1))
    for coordinate_y in range(map_height):
        print("|", end="")
        for coordinate_x in range(map_width):
            char_to_draw = " "
            object_in_cell = None
            for map_object in map_objects:
                if map_object[0] == coordinate_x and map_object[1] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object
            for tail_piece in tail:
                if tail_piece[0] == coordinate_x and tail_piece[1] == coordinate_y:
                    char_to_draw = "@"
            if position[0] == coordinate_x and position[1] == coordinate_y:
                char_to_draw = "@"
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1
                    points += 1
                    for a in range(1):
                        randomx = random.randint(0, 19)
                        randomy = random.randint(0, 14)
                        randPosition.append((randomx, randomy))
                        while randPosition in position or randPosition in tail:
                            randomx = random.randint(0, 19)
                            randomy = random.randint(0, 14)
                        map_objects.append((randomx, randomy))
                        randPosition.clear()
            print(" {} ".format(char_to_draw), end="")
        print("|")
    print("-" * 3 * (map_width + 1))
    print("PUNTOS: {}".format(points))
    # DIRECCION
    #direction = input("(WASD)")
    direction = readchar.readchar()
    if direction == "w":
        tail.insert(0, position.copy())
        tail = tail[:tail_length]
        if position[1] < 1:
            print("HAS PERDIDO")
            break
        else:
            position[1] -= 1

    elif direction == "s":
        tail.insert(0, position.copy())
        tail = tail[:tail_length]
        if position[1] > 13:
            print("HAS PERDIDO")
            break
        else:
            position[1] += 1

    elif direction == "a":
        tail.insert(0, position.copy())
        tail = tail[:tail_length]
        if position[0] < 1:
            print("HAS PERDIDO")
            break
        else:
            position[0] -= 1

    elif direction == "d":
        tail.insert(0, position.copy())
        tail = tail[:tail_length]
        if position[0] > 18:
            print("HAS PERDIDO")
            break
        else:
            position[0] += 1

    elif direction == "b":
        break
    os.system("cls")