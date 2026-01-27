def xturn(a):
    xbox = int(input("Enter the box you will put X in: ")) - 1
    a[xbox] = "X"
    print("+---+---+---+")
    print("| " + boxes[0] + " | " + boxes[1] + " | " + boxes[2] + " |")
    print("+---+---+---+")
    print("| " + boxes[3] + " | " + boxes[4] + " | " + boxes[5] + " |")
    print("+---+---+---+")
    print("| " + boxes[6] + " | " + boxes[7] + " | " + boxes[8] + " |")
    print("+---+---+---+\n")

def oturn(b):
    obox = int(input("Enter the box you will put O in: ")) - 1
    b[obox] = "O"
    print("+---+---+---+")
    print("| " + boxes[0] + " | " + boxes[1] + " | " + boxes[2] + " |")
    print("+---+---+---+")
    print("| " + boxes[3] + " | " + boxes[4] + " | " + boxes[5] + " |")
    print("+---+---+---+")
    print("| " + boxes[6] + " | " + boxes[7] + " | " + boxes[8] + " |")
    print("+---+---+---+\n")

def point(c):
    if c[0] == c[1] == c[2] == "X":
        return 1
    elif c[3] == c[4] == c[5] == "X":
        return 1
    elif c[6] == c[7] == c[8] == "X":
        return 1
    elif c[0] == c[3] == c[6] == "X":
        return 1
    elif c[1] == c[4] == c[7] == "X":
        return 1
    elif c[2] == c[5] == c[8] == "X":
        return 1
    elif c[0] == c[4] == c[8] == "X":
        return 1
    elif c[2] == c[4] == c[6] == "X":
        return 1
    elif c[0] == c[1] == c[2] == "O":
        return 2
    elif c[3] == c[4] == c[5] == "O":
        return 2
    elif c[6] == c[7] == c[8] == "O":
        return 2
    elif c[0] == c[3] == c[6] == "O":
        return 2
    elif c[1] == c[4] == c[7] == "O":
        return 2
    elif c[2] == c[5] == c[8] == "O":
        return 2
    elif c[0] == c[4] == c[8] == "O":
        return 2
    elif c[2] == c[4] == c[6] == "O":
        return 2
    else:
        return 0

print("-------------------------------------")
print("Welcome to my Tic Tac Toe Game!\n")

print("+---+---+---+")
print("| 1 | 2 | 3 |")
print("+---+---+---+")
print("| 4 | 5 | 6 |")
print("+---+---+---+")
print("| 7 | 8 | 9 |")
print("+---+---+---+")
print("This is what the bored currently looks like!\n")
print("It's X's Turn")

boxes = [" ", " ", " ", " ", " ", " ", " ", " ", " ",]
winner = 0
counter = 0
while winner == 0:
    xturn(boxes)
    winner = point(boxes)
    counter += 1
    if counter == 9:
        break

    oturn(boxes)
    winner = point(boxes)
    counter += 1
    if counter == 9:
        break

if winner == 1:
    print("Congrats, X Wins!")
elif winner == 2:
    print("Congrats, O Wins!")
elif counter == 9:
    print("No One Won Thet Round! Try Again?")