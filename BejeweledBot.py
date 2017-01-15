import os
import time
from PIL import ImageGrab as ig
from PIL import Image
import autopy

start_time = time.time()

board = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]

recolorX = []
recolorY = []
MAX_MOVES = 6
moves = 0

# skipX = []
# skipY = []
skip = []

MoveY1 = []
MoveX1 = []
MoveY2 = []
MoveX2 = []

MOUSE_REST = [320, 505]

# x21y21 color bounds
gems = [["yellow", "red", "green", "blue", "purple", "white", "orange"],
        ["y", "r", "g", "b", "p", "w", "o"]]
bounds =[[520, 306, 135, 324, 430, 665, 265],
        [565, 325, 180, 390, 500, 725, 307]]

# First Monitor Dim
X_POS_ONE = 1920
Y_POS_ONE = 1080

#Second Monitor Anchor Point
X_POS = 404
Y_POS = 352

# X_POS_MAIN = 404
# Y_POS_MAIN = 352

# X_POS = X_POS_ONE + X_POS_MAIN
# Y_POS = X_POS_ONE + X_POS_MAIN

def colorGrab_Pillow():
    print 'start'
    boxGame = (X_POS, Y_POS, X_POS + 320, Y_POS + 320)
    # counter = str(int(time.time()))
    # im.grab() = chilimangoes.grab_screen()
    # im = ig.grab(boxGame)
    # im = chilimangoes.grab_screen()
    # savepath = os.getcwd() + '\\screens'
    # chilimangoes.grab_screen([2324, 379, 2644, 699]).save(os.getcwd() +
        # '\\screens\\screen_' + str(counter) + '.jpg', 'jpeg')
    # im.save(os.getcwd() + '\\screens\\screen_' + str(counter) + '.jpg', 'jpeg')
    im = ig.grab(boxGame)
    savepath = os.getcwd() + '\\screens'
    im.save(savepath + '\\screen_1' + '.jpg', 'jpeg')
    img = Image.open(savepath + '\\screen_1.jpg')
    for y in range(8):
        for x in range(8):
            a1 = 21 + x*40
            a2 = 21 + y*40
            b = img.getpixel((a1, a2))
            c = b[0] + b[1] + b[2]
            if (bounds[0][4] < c < bounds[1][4]) | (235 < c < 243):
                a2 = 17 + y*40
                b = img.getpixel((a1, a2))
                c = b[0] + b[1] + b[2]
            board[y][x] = c
    for g in range(8):
        print board[g]
        y = x = 0
    for y in range(8):
        for x in range(8):
            assignColor(x, y)
            x += 1
        y += 1
    print recolorX
    print recolorY
    recolor()
    for g in range(8):
        print board[g]
    findMovesL1()

def recolor():
    if (len(recolorY) > 0 & len(recolorY) == len(recolorX)):
        img = Image.open(os.getcwd() + '\\screens\\screen_' + str(counter) + '.jpg')
        for e in range(len(recolorY)):
            y = recolorY[e]
            x = recolorX[e]
            x = 21 + x*40
            y = 17 + y*40
            b = img.getpixel((x, y))
            c = b[0] + b[1] + b[2]
            print c
            board[y][x] = c
            assignColor(x, y)

def assignColor(x, y):
    cl = board[y][x]
    if (bounds[0][0] < cl < bounds[1][0]) | (400 < cl < 428):
        board[y][x] = gems[1][0]
    elif (bounds[0][1] < cl < bounds[1][1]):
        board[y][x] = gems[1][1]
    elif (bounds[0][2] < cl < bounds[1][2]) | (110 < cl < 121) | (194 < cl < 214):
        board[y][x] = gems[1][2]
    elif (bounds[0][3] < cl < bounds[1][3]):
        board[y][x] = gems[1][3]
    elif (bounds[0][4] < cl < bounds[1][4]) | (235 < cl < 243) | (570 < cl < 640) | (503 < cl < 516):
        board[y][x] = gems[1][4]
    elif ((bounds[0][5] < cl < bounds[1][5]) | (499 < cl < 503) | (745 < cl < 765)):
        board[y][x] = gems[1][5]
    elif (bounds[0][6] < cl < bounds[1][6]):
        board[y][x] = gems[1][6]
    else:
        recolorY.append(y)
        recolorX.append(x)
        print cl

def findMovesL1():
    global moves
    moves = y = x = 0
    # proceed = False
    # while (moves < MAX_MOVES):
    for y in range(8):
        for x in range(8):
            coord = str(y) + str (x)
            if coord in skip:
                break;
            g = board[y][x]
            if (0 < y < 7):
                up = board[y - 1][x]
                down = board[y + 1][x]
            if (0 < x < 7):
                right = board[y][x + 1]
                left = board[y][x - 1]
            if (y == 0):
                up  = None
                down = board[y + 1][x]
                # dont check up
            if (y == 7):
                down = None
                up = board[y - 1][x]
                # dont check down
            if (x == 0):
                left = None
                right = board[y][x + 1]
                # dont check left
            if (x == 7):
                right = None
                left = board[y][x - 1]
                # dont check right

            # Start making matches
            if (g == up and y > 1):
                print ("up " + str(y) + " " + str(x))
                findUpL2(y - 2, x, g)
            #send coordingate of middle gem
            if (g == down and y < 6):
                print ("down " + str(y) + " " + str(x))
                findDownL2(y + 2, x, g)
            if (g == right and x < 6):
                print ("right " + str(y) + " " + str(x))
                findRightL2(y, x + 2, g)
            if (g == left and x  > 1):
                print ("left " + str(y) + " " + str(x))
                findLeftL2(y, x - 2, g)

            # dont forget special case - up1 down1 up1

############# OUTER SQUARE #############
            #  first row middle four
            if (y == 0 and 1 < x < 6):
                farRight = board[y][x + 2]
                farLeft = board[y][x - 2]
                farDown = board[y + 2][x]
                if (g == farDown):
                    if (g == board[y + 1][x + 1]):
                        print ("Match! move " + str(y + 1) + " " + str(x) + " right FARDOWN")
                        moveRight(y + 1, x)
                        skip.extend((str(y) + str(x), str(y + 1) + str(x + 1), str(y + 1) + str(x), str(y + 2) + str(x)))
                        moves += 1
                    elif (g == board[y + 1][x - 1]):
                        print ("Match! move " + str(y + 1) + " " + str(x) + " left FARDOWN")
                        moveLeft(y + 1, x)
                        skip.extend((str(y) + str(x), str(y + 1) + str(x - 1), str(y + 1) + str(x), str(y + 2) + str(x)))
                        moves += 1
                if (g == farRight and g == board[y + 1][x + 1]):
                    print ("Match! move " + str(y) + " " + str(x + 1) + " down FARRIGHT")
                    moveDown(y, x + 1)
                    skip.extend((str(y) + str(x), str(y + 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                    moves += 1
                if (g == farLeft and g == board[y + 1][x - 1]):
                    print ("Match! move " + str(y) + " " + str(x - 1) + " down FARLEFT")
                    moveDown(y, x - 1)
                    skip.extend((str(y) + str(x), str(y + 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                    moves += 1

            #  last row middle four
            elif (y == 7 and 1 < x < 6):
                farRight = board[y][x + 2]
                farLeft = board[y][x - 2]
                farUp = board[y - 2][x]
                if (g == farUp):
                    if (g == board[y - 1][x + 1]):
                        print ("Match! move " + str(y - 1) + " " + str(x) + " right FARUP")
                        moveRight(y - 1, x)
                        skip.extend((str(y) + str(x), str(y - 1) + str(x + 1), str(y - 1) + str(x), str(y - 2) + str(x)))
                        moves += 1
                    elif (g == board[y - 1][x - 1]):
                        print ("Match! move " + str(y - 1) + " " + str(x) + " left FARUP")
                        moveLeft(y - 1, x)
                        skip.extend((str(y) + str(x), str(y - 1) + str(x - 1), str(y - 1) + str(x), str(y - 2) + str(x)))
                        moves += 1
                if (g == farRight and g == board[y - 1][x + 1]):
                    print ("Match! move " + str(y) + " " + str(x + 1) + " up FARRIGHT")
                    moveUp(y, x + 1)
                    skip.extend((str(y) + str(x), str(y - 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                    moves += 1
                if (g == farLeft and g == board[y - 1][x - 1]):
                    print ("Match! move " + str(y) + " " + str(x - 1) + " up FARLEFT")
                    moveUp(y, x - 1)
                    skip.extend((str(y) + str(x), str(y - 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                    moves += 1

            #  first col middle four
            elif (x == 0 and 1 < y < 6):
                farRight = board[y][x + 2]
                farUp = board[y - 2][x]
                farDown = board[y + 2][x]
                if (g == farUp and g == board[y - 1][x + 1]):
                    print ("Match! move " + str(y - 1) + " " + str(x) + " right FARUP")
                    moveRight(y - 1, x)
                    skip.extend((str(y) + str(x), str(y - 1) + str(x + 1), str(y - 1) + str(x), str(y - 2) + str(x)))
                    moves += 1
                if (g == farDown and g == board[y + 1][x + 1]):
                    print ("Match! move " + str(y + 1) + " " + str(x) + " right FARDOWN")
                    moveRight(y + 1, x)
                    skip.extend((str(y) + str(x), str(y + 1) + str(x + 1), str(y + 1) + str(x), str(y + 2) + str(x)))
                    moves += 1
                if (g == farRight):
                    if (g == board[y - 1][x + 1]):
                        print ("Match! move " + str(y) + " " + str(x + 1) + " up FARRIGHT")
                        moveUp(y, x + 1)
                        skip.extend((str(y) + str(x), str(y - 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                        moves += 1
                    elif (g == board[y + 1][x + 1]):
                        print ("Match! move " + str(y) + " " + str(x + 1) + " down FARRIGHT")
                        moveDown(y, x + 1)
                        skip.extend((str(y) + str(x), str(y + 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                        moves += 1

            #  last col middle four
            elif (x == 7 and 1 < y < 6):
                farLeft = board[y][x - 2]
                farUp = board[y - 2][x]
                farDown = board[y + 2][x]
                if (g == farUp and g == board[y - 1][x - 1]):
                    print ("Match! move " + str(y - 1) + " " + str(x) + " left FARUP")
                    moveLeft(y - 1, x)
                    skip.extend((str(y) + str(x), str(y - 1) + str(x - 1), str(y - 1) + str(x), str(y - 2) + str(x)))
                    moves += 1
                if (g == farDown and g == board[y + 1][x - 1]):
                    print ("Match! move " + str(y + 1) + " " + str(x) + " left FARDOWN")
                    moveLeft(y + 1, x)
                    skip.extend((str(y) + str(x), str(y + 1) + str(x - 1), str(y + 1) + str(x), str(y + 2) + str(x)))
                    moves += 1
                if (g == farLeft):
                    if (g == board[y - 1][x - 1]):
                        print ("Match! move " + str(y) + " " + str(x - 1) + " up FARLEFT")
                        moveUp(y, x - 1)
                        skip.extend((str(y) + str(x), str(y - 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                        moves += 1
                    elif (g == board[y + 1][x - 1]):
                        print ("Match! move " + str(y) + " " + str(x - 1) + " down FARLEFT")
                        moveDown(y, x - 1)
                        skip.extend((str(y) + str(x), str(y + 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                        moves += 1

############# INNER MIDDLE SQUARES #############
            #  second row middle four
            if (y == 1 and 1 < x < 6):
                farRight = board[y][x + 2]
                farLeft = board[y][x - 2]
                farDown = board[y + 2][x]
                if (g == farDown):
                    if (g == board[y + 1][x + 1]):
                        print ("Match! move " + str(y + 1) + " " + str(x) + " right FARDOWN")
                        moveRight(y + 1, x)
                        skip.extend((str(y) + str(x), str(y + 1) + str(x + 1), str(y + 1) + str(x), str(y + 2) + str(x)))
                        moves += 1
                    elif (g == board[y + 1][x - 1]):
                        print ("Match! move " + str(y + 1) + " " + str(x) + " left FARDOWN")
                        moveLeft(y + 1, x)
                        skip.extend((str(y) + str(x), str(y + 1) + str(x - 1), str(y + 1) + str(x), str(y + 2) + str(x)))
                        moves += 1
                if (g == farRight):
                    if (g == board[y - 1][x + 1]):
                        print ("Match! move " + str(y) + " " + str(x + 1) + " up FARRIGHT")
                        moveUp(y, x + 1)
                        skip.extend((str(y) + str(x), str(y - 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                        moves += 1
                    elif (g == board[y + 1][x + 1]):
                        print ("Match! move " + str(y) + " " + str(x + 1) + " down FARRIGHT")
                        moveDown(y, x + 1)
                        skip.extend((str(y) + str(x), str(y + 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                        moves += 1
                if (g == farLeft):
                    if (g == board[y - 1][x - 1]):
                        print ("Match! move " + str(y) + " " + str(x - 1) + " up FARLEFT")
                        moveUp(y, x - 1)
                        skip.extend((str(y) + str(x), str(y - 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                        moves += 1
                    elif (g == board[y + 1][x - 1]):
                        print ("Match! move " + str(y) + " " + str(x - 1) + " down FARLEFT")
                        moveDown(y, x - 1)
                        skip.extend((str(y) + str(x), str(y + 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                        moves += 1

            #  seventh row middle four
            elif (y == 6 and 1 < x < 6):
                farRight = board[y][x + 2]
                farLeft = board[y][x - 2]
                farUp = board[y - 2][x]
                if (g == farUp):
                    if (g == board[y - 1][x + 1]):
                        print ("Match! move " + str(y - 1) + " " + str(x) + " right FARUP")
                        moveRight(y - 1, x)
                        skip.extend((str(y) + str(x), str(y - 1) + str(x + 1), str(y - 1) + str(x), str(y - 2) + str(x)))
                        moves += 1
                    elif (g == board[y - 1][x - 1]):
                        print ("Match! move " + str(y - 1) + " " + str(x) + " left FARUP")
                        moveLeft(y - 1, x)
                        skip.extend((str(y) + str(x), str(y - 1) + str(x - 1), str(y - 1) + str(x), str(y - 2) + str(x)))
                        moves += 1
                if (g == farRight):
                    if (g == board[y - 1][x + 1]):
                        print ("Match! move " + str(y) + " " + str(x + 1) + " up FARRIGHT")
                        moveUp(y, x + 1)
                        skip.extend((str(y) + str(x), str(y - 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                        moves += 1
                    elif (g == board[y + 1][x + 1]):
                        print ("Match! move " + str(y) + " " + str(x + 1) + " down FARRIGHT")
                        moveDown(y, x + 1)
                        skip.extend((str(y) + str(x), str(y + 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                        moves += 1
                if (g == farLeft):
                    if (g == board[y - 1][x - 1]):
                        print ("Match! move " + str(y) + " " + str(x - 1) + " up FARLEFT")
                        moveUp(y, x - 1)
                        skip.extend((str(y) + str(x), str(y - 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                        moves += 1
                    elif (g == board[y + 1][x - 1]):
                        print ("Match! move " + str(y) + " " + str(x - 1) + " down FARLEFT")
                        moveDown(y, x - 1)
                        skip.extend((str(y) + str(x), str(y + 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                        moves += 1

            #  second col middle four
            elif (x == 1 and 1 < y < 6):
                farRight = board[y][x + 2]
                farUp = board[y - 2][x]
                farDown = board[y + 2][x]
                if (g == farUp):
                    if (g == board[y - 1][x + 1]):
                        print ("Match! move " + str(y - 1) + " " + str(x) + " right FARUP")
                        moveRight(y - 1, x)
                        skip.extend((str(y) + str(x), str(y - 1) + str(x + 1), str(y - 1) + str(x), str(y - 2) + str(x)))
                        moves += 1
                    elif (g == board[y - 1][x - 1]):
                        print ("Match! move " + str(y - 1) + " " + str(x) + " left FARUP")
                        moveLeft(y - 1, x)
                        skip.extend((str(y) + str(x), str(y - 1) + str(x - 1), str(y - 1) + str(x), str(y - 2) + str(x)))
                        moves += 1
                if (g == farDown):
                    if (g == board[y + 1][x + 1]):
                        print ("Match! move " + str(y + 1) + " " + str(x) + " right FARDOWN")
                        moveRight(y + 1, x)
                        skip.extend((str(y) + str(x), str(y + 1) + str(x + 1), str(y + 1) + str(x), str(y + 2) + str(x)))
                        moves += 1
                    elif (g == board[y + 1][x - 1]):
                        print ("Match! move " + str(y + 1) + " " + str(x) + " left FARDOWN")
                        moveLeft(y + 1, x)
                        skip.extend((str(y) + str(x), str(y + 1) + str(x - 1), str(y + 1) + str(x), str(y + 2) + str(x)))
                        moves += 1
                if (g == farRight):
                    if (g == board[y - 1][x + 1]):
                        print ("Match! move " + str(y) + " " + str(x + 1) + " up FARRIGHT")
                        moveUp(y, x + 1)
                        skip.extend((str(y) + str(x), str(y - 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                        moves += 1
                    elif (g == board[y + 1][x + 1]):
                        print ("Match! move " + str(y) + " " + str(x + 1) + " down FARRIGHT")
                        moveDown(y, x + 1)
                        skip.extend((str(y) + str(x), str(y + 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                        moves += 1

            #  seventh col middle four
            elif (x == 6 and 1 < y < 6):
                farLeft = board[y][x - 2]
                farUp = board[y - 2][x]
                farDown = board[y + 2][x]
                if (g == farUp):
                    if (g == board[y - 1][x + 1]):
                        print ("Match! move " + str(y - 1) + " " + str(x) + " right FARUP")
                        moveRight(y - 1, x)
                        skip.extend((str(y) + str(x), str(y - 1) + str(x + 1), str(y - 1) + str(x), str(y - 2) + str(x)))
                        moves += 1
                    elif (g == board[y - 1][x - 1]):
                        print ("Match! move " + str(y - 1) + " " + str(x) + " left FARUP")
                        moveLeft(y - 1, x)
                        skip.extend((str(y) + str(x), str(y - 1) + str(x - 1), str(y - 1) + str(x), str(y - 2) + str(x)))
                        moves += 1
                if (g == farDown):
                    if (g == board[y + 1][x + 1]):
                        print ("Match! move " + str(y + 1) + " " + str(x) + " right FARDOWN")
                        moveRight(y + 1, x)
                        skip.extend((str(y) + str(x), str(y + 1) + str(x + 1), str(y + 1) + str(x), str(y + 2) + str(x)))
                        moves += 1
                    elif (g == board[y + 1][x - 1]):
                        print ("Match! move " + str(y + 1) + " " + str(x) + " left FARDOWN")
                        moveLeft(y + 1, x)
                        skip.extend((str(y) + str(x), str(y + 1) + str(x - 1), str(y + 1) + str(x), str(y + 2) + str(x)))
                        moves += 1
                if (g == farLeft):
                    if (g == board[y - 1][x - 1]):
                        print ("Match! move " + str(y) + " " + str(x - 1) + " up FARLEFT")
                        moveUp(y, x - 1)
                        skip.extend((str(y) + str(x), str(y - 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                        moves += 1
                    elif (g == board[y + 1][x - 1]):
                        print ("Match! move " + str(y) + " " + str(x - 1) + " down FARLEFT")
                        moveDown(y, x - 1)
                        skip.extend((str(y) + str(x), str(y + 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                        moves += 1

############# MIDDLE SQUARE #############
            # ALL MIDDLE CASES
            if (1 < x < 6 and 1 < y < 6):
                farRight = board[y][x + 2]
                farLeft = board[y][x - 2]
                farUp = board[y - 2][x]
                farDown = board[y + 2][x]
                if (g == farUp):
                    if (g == board[y - 1][x + 1]):
                        print ("Match! move " + str(y - 1) + " " + str(x) + " right FARUP")
                        moveRight(y - 1, x)
                        skip.extend((str(y) + str(x), str(y - 1) + str(x + 1), str(y - 1) + str(x), str(y - 2) + str(x)))
                        moves += 1
                    elif (g == board[y - 1][x - 1]):
                        print ("Match! move " + str(y - 1) + " " + str(x) + " left FARUP")
                        moveLeft(y - 1, x)
                        skip.extend((str(y) + str(x), str(y - 1) + str(x - 1), str(y - 1) + str(x), str(y - 2) + str(x)))
                        moves += 1
                if (g == farDown):
                    if (g == board[y + 1][x + 1]):
                        print ("Match! move " + str(y + 1) + " " + str(x) + " right FARDOWN")
                        moveRight(y + 1, x)
                        skip.extend((str(y) + str(x), str(y + 1) + str(x + 1), str(y + 1) + str(x), str(y + 2) + str(x)))
                        moves += 1
                    elif (g == board[y + 1][x - 1]):
                        print ("Match! move " + str(y + 1) + " " + str(x) + " left FARDOWN")
                        moveLeft(y + 1, x)
                        skip.extend((str(y) + str(x), str(y + 1) + str(x - 1), str(y + 1) + str(x), str(y + 2) + str(x)))
                        moves += 1
                if (g == farRight):
                    if (g == board[y - 1][x + 1]):
                        print ("Match! move " + str(y) + " " + str(x + 1) + " up FARRIGHT")
                        moveUp(y, x + 1)
                        skip.extend((str(y) + str(x), str(y - 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                        moves += 1
                    elif (g == board[y + 1][x + 1]):
                        print ("Match! move " + str(y) + " " + str(x + 1) + " down FARRIGHT")
                        moveDown(y, x + 1)
                        skip.extend((str(y) + str(x), str(y + 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                        moves += 1
                if (g == farLeft):
                    if (g == board[y - 1][x - 1]):
                        print ("Match! move " + str(y) + " " + str(x - 1) + " up FARLEFT")
                        moveUp(y, x - 1)
                        skip.extend((str(y) + str(x), str(y - 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                        moves += 1
                    elif (g == board[y + 1][x - 1]):
                        print ("Match! move " + str(y) + " " + str(x - 1) + " down FARLEFT")
                        moveDown(y, x - 1)
                        skip.extend((str(y) + str(x), str(y + 1) + str(x + 1), str(y) + str(x + 1), str(y) + str(x + 2)))
                        moves += 1

                # only do if moves < MAX_MOVES
            x += 1
        y += 1

def findUpL2(y, x, g):
    global moves
    if (x > 0 and g == board[y][x - 1]):
        print ("Match! move " + str(y) + " " + str(x) + " left")
        moveLeft(y, x)
        # skipY.extend((y, y + 1, y + 2, y))
        # skipX.extend((x, x, x, x - 1))
        skip.extend((str(y) + str(x), str(y + 1) + str(x), str(y + 2) + str(x), str(y) + str(x - 1)))
        moves += 1
    elif (x < 7 and g == board[y][x + 1]):
        print ("Match! move " + str(y) + " " + str(x) + " right")
        moveRight(y, x)
        # skipY.extend((y, y + 1, y + 2, y))
        # skipX.extend((x, x, x, x + 1))
        skip.extend((str(y) + str(x), str(y + 1) + str(x), str(y + 2) + str(x), str(y) + str(x + 1)))
        moves += 1
    elif (y > 0 and g == board[y - 1][x]):
        print ("Match! move " + str(y) + " " + str(x) + " up")
        moveUp(y, x)
        # skipY.extend((y, y + 1, y + 2, y - 1))
        # skipX.extend((x, x, x, x))
        skip.extend((str(y) + str(x), str(y + 1) + str(x), str(y + 2) + str(x), str(y - 1) + str(x)))
        moves += 1

def findDownL2(y, x, g):
    global moves
    if (x > 0 and g == board[y][x - 1]):
        print ("Match! move " + str(y) + " " + str(x) + " left")
        moveLeft(y, x)
        # skipY.extend((y, y - 1, y - 2, y))
        # skipX.extend((x, x, x, x - 1))
        skip.extend((str(y) + str(x), str(y - 1) + str(x), str(y - 2) + str(x), str(y) + str(x - 1)))
        moves += 1
    elif (x < 7 and g == board[y][x + 1]):
        print ("Match! move " + str(y) + " " + str(x) + " right")
        moveRight(y, x)
        # skipY.extend((y, y - 1, y - 2, y))
        # skipX.extend((x, x, x, x + 1))
        skip.extend((str(y) + str(x), str(y - 1) + str(x), str(y - 2) + str(x), str(y) + str(x + 1)))
        moves += 1
    elif (y < 7 and g == board[y + 1][x]):
        print ("Match! move " + str(y) + " " + str(x) + " down")
        moveDown(y, x)
        # skipY.extend((y, y - 1, y - 2, y + 1))
        # skipX.extend((x, x, x, x))
        skip.extend((str(y) + str(x), str(y - 1) + str(x), str(y - 2) + str(x), str(y + 1) + str(x)))
        moves += 1

def findRightL2(y, x, g):
    global moves
    if (y > 0 and g == board[y - 1][x]):
        print ("Match! move " + str(y) + " " + str(x) + " up")
        moveUp(y, x)
        # skipY.extend((y, y, y, y - 1))
        # skipX.extend((x, x - 1, x - 2, x))
        skip.extend((str(y) + str(x), str(y) + str(x - 1), str(y) + str(x - 2), str(y - 1) + str(x)))
        moves += 1
    elif (y < 7 and g == board[y + 1][x]):
        print ("Match! move " + str(y) + " " + str(x) + " down")
        moveDown(y, x)
        # skipY.extend((y, y, y, y + 1))
        # skipX.extend((x, x - 1, x - 2, x))
        skip.extend((str(y) + str(x), str(y) + str(x - 1), str(y) + str(x - 2), str(y + 1) + str(x)))
        moves += 1
    elif (x < 7 and g == board[y][x + 1]):
        print ("Match! move " + str(y) + " " + str(x) + " right")
        moveRight(y, x)
        # skipY.extend((y, y, y, y))
        # skipX.extend((x, x - 1, x - 2, x + 1))
        skip.extend((str(y) + str(x), str(y) + str(x - 1), str(y) + str(x - 2), str(y) + str(x + 1)))
        moves += 1

def findLeftL2(y, x, g):
    global moves
    if (y > 0 and g == board[y - 1][x]):
        print ("Match! move " + str(y) + " " + str(x) + " up")
        moveUp(y, x)
        # skipY.extend((y, y, y, y - 1))
        # skipX.extend((x, x + 1, x + 2, x))
        skip.extend((str(y) + str(x), str(y) + str(x + 1), str(y) + str(x + 2), str(y - 1) + str(x)))
        moves += 1
    elif (y < 7 and g == board[y + 1][x]):
        print ("Match! move " + str(y) + " " + str(x) + " down")
        moveDown(y, x)
        # skipY.extend((y, y, y, y + 1))
        # skipX.extend((x, x + 1, x + 2, x))
        skip.extend((str(y) + str(x), str(y) + str(x + 1), str(y) + str(x + 2), str(y + 1) + str(x)))
        moves += 1
    elif (x > 0 and g == board[y][x - 1]):
        print ("Match! move " + str(y) + " " + str(x) + " left")
        moveLeft(y, x)
        # skipY.extend((y, y, y, y))
        # skipX.extend((x, x + 1, x + 2, x - 1))
        skip.extend((str(y) + str(x), str(y) + str(x + 1), str(y) + str(x + 2), str(y) + str(x - 1)))
        moves += 1

def introScreen():
    autopy.mouse.move(490, 575)
    autopy.mouse.click(True)
    time.sleep(0.25)
    autopy.mouse.move(440, 688)
    autopy.mouse.click(True)
    time.sleep(0.25)
    autopy.mouse.click(True)
    mouseToRest()
    time.sleep(3.5)

def playAgain():
    autopy.mouse.move(490, 770)
    autopy.mouse.click(True)
    time.sleep(0.25)
    autopy.mouse.move(440, 688)
    autopy.mouse.click(True)
    time.sleep(0.25)
    autopy.mouse.click(True)
    mouseToRest()
    time.sleep(3.5)

def mouseToRest():
    autopy.mouse.move(MOUSE_REST[0], MOUSE_REST[1])
    autopy.mouse.toggle(True)
    autopy.mouse.toggle(False)

MOUSE_POS_X = 424
MOUSE_POS_Y = 372

def moveUp(y, x):
    MoveY1.append(MOUSE_POS_Y + y*40)
    MoveX1.append(MOUSE_POS_X + x*40)
    MoveY2.append(MOUSE_POS_Y + (y - 1)*40)
    MoveX2.append(MOUSE_POS_X + x*40)

def moveDown(y, x):
    MoveY1.append(MOUSE_POS_Y + y*40)
    MoveX1.append(MOUSE_POS_X + x*40)
    MoveY2.append(MOUSE_POS_Y + (y + 1)*40)
    MoveX2.append(MOUSE_POS_X + x*40)

def moveRight(y, x):
    MoveY1.append(MOUSE_POS_Y + y*40)
    MoveX1.append(MOUSE_POS_X + x*40)
    MoveY2.append(MOUSE_POS_Y + y*40)
    MoveX2.append(MOUSE_POS_X + (x + 1)*40)

def moveLeft(y, x):
    MoveY1.append(MOUSE_POS_Y + y*40)
    MoveX1.append(MOUSE_POS_X + x*40)
    MoveY2.append(MOUSE_POS_Y + y*40)
    MoveX2.append(MOUSE_POS_X + (x - 1)*40)



# old, redundant funct #
# def findUpL2(y, x, g):
#     if (y == 0):
#         if (g == board[y][x - 1]):
#             print ("Match! move " + str(y) + " " + str(x) + " left")
#         elif (x < 7 and g == board[y][x + 1]):
#             print ("Match! move " + str(y) + " " + str(x) + " right")
#     # if (y > 1):
#     else:
#         if (g == board[y][x - 1]):
#             print ("Match! move " + str(y) + " " + str(x) + " left")
#         elif (x < 7 and g == board[y][x + 1]):
#             print ("Match! move " + str(y) + " " + str(x) + " right")
#         elif (g == board[y - 1][x]):
#             print ("Match! move " + str(y) + " " + str(x) + " up")

def purgeArrays():
    del MoveY1[:]
    del MoveX1[:]
    del MoveY2[:]
    del MoveX2[:]
    del recolorX[:]
    del recolorY[:]
    del skip[:]


def main():
    # introScreen()
    playAgain()

    global moves
    start = time.time()
    while(time.time() - start < 70):
        colorGrab_Pillow()
        for moveIndex in range(len(MoveY1)):
            autopy.mouse.move(MoveX1[moveIndex], MoveY1[moveIndex])
            autopy.mouse.toggle(True)
            autopy.mouse.smooth_move(MoveX2[moveIndex], MoveY2[moveIndex])
            autopy.mouse.toggle(False)
            # time.sleep(0.05)
            time.sleep(0.025)
        mouseToRest()
        print skip
        print MoveY1
        print MoveX1
        print MoveY2
        print MoveX2
        print ("moves: " + str(moves))
        # if (moves == 0): break
        purgeArrays()
        time.sleep(0.2)



# if __name__ == '__main__':
#     time.sleep(3.0)
#     starttime = time.time()
#     counter = 0
#     while (counter < 15):
#         colorGrab_Pillow()
#         counter += 1
#         time.sleep(4.0 - ((time.time() - starttime) % 4.0))

# colorGrab()

# mouseToRest()

#colorGrab_PillowGIF()
#colorGrab_PillowGIFDOUBLE()


# mouseToRest()
# colorGrab_Pillow()
main()
print("--- %s seconds ---" % (time.time() - start_time))