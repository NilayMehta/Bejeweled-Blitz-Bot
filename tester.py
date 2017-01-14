import os
import time
import PIL
from PIL import ImageGrab as ig
from PIL import Image
import autopy
import win32gui
import time
import chilimangoes

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

# x21y21 color bounds
gems = [["yellow", "red", "green", "blue", "purple", "white", "orange"],
        ["y", "r", "g", "b", "p", "w", "o"]]
bounds =[[520, 306, 135, 345, 430, 665, 265],
        [565, 330, 180, 390, 500, 720, 307]]

def screenGrabTitle():
    boxTitle = (235, 302, 745, 722)
    im = ig.grab(boxTitle)
    savepath = os.getcwd() + '\\screens'
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    im.save(os.getcwd() + '\\screens\\screenshot_' + str(int(time.time())) +
        '.png', 'PNG')

def screenGrabGame():
    boxGame = (404, 354, 722, 670)
    im = ig.grab(boxGame)
    savepath = os.getcwd() + '\\screens'
    im.save(os.getcwd() + '\\screens\\screenshot_' + str(int(time.time())) +
        '.png', 'PNG')

# First Monitor Dim
X_POS_ONE = 1920
Y_POS_ONE = 1080

#Second Monitor Anchor Point
X_POS_MAIN = 404
Y_POS_MAIN = 352

X_POS = X_POS_ONE + X_POS_MAIN
Y_POS = X_POS_ONE + X_POS_MAIN

def colorGrab_Pillow():
    print 'start'
    boxGame = (X_POS, Y_POS, X_POS + 320, Y_POS + 320)
    counter = 1
    # im.grab() = chilimangoes.grab_screen()
    # im = ig.grab(boxGame)
    # im = chilimangoes.grab_screen()
    savepath = os.getcwd() + '\\screens'
    chilimangoes.grab_screen([2324, 379, 2644, 699]).save(os.getcwd() +
        '\\screens\\screen_' + str(counter) + '.jpg', 'jpeg')
    # im.save(os.getcwd() + '\\screens\\screen_' + str(counter) + '.jpg', 'jpeg')
    img = Image.open(os.getcwd() + '\\screens\\screen_' + str(counter) + '.jpg')
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

# def colorGrab_PillowGIF():
#     print 'start'
#     boxGame = (X_POS, Y_POS, X_POS + 320, Y_POS + 320)
#     counter = 1
#     im = ig.grab(boxGame)
#     savepath = os.getcwd() + '\\screens'
#     im.save(os.getcwd() + '\\screens\\screen_' + str(counter) + '.gif', 'gif')
#     img = Image.open(os.getcwd() + '\\screens\\screen_' + str(counter) + '.gif')
#     for y in range(8):
#         for x in range(8):
#             a1 = 21 + x*40
#             a2 = 21 + y*40
#             b = img.getpixel((a1, a2))
#             board[y][x] = b
#     for g in range(8):
#         print board[g]

# def colorGrab_PillowGIFDOUBLE():
#     print 'start'
#     boxGame = (404, 354, 722, 670)
#     counter = 1
#     im = ig.grab(boxGame)
#     savepath = os.getcwd() + '\\screens'
#     im.save(os.getcwd() + '\\screens\\screen_' + str(counter) + '.gif', 'gif')
#     img = Image.open(os.getcwd() + '\\screens\\screen_' + str(counter) + '.gif')
#     for y in range(8):
#         for x in range(8):
#             a1 = 20 + x*40
#             a2 = 18 + y*40
#             b1 = 20 + x*40
#             b2 = 20 + y*40
#             a = img.getpixel((a1, a2))
#             b = img.getpixel((b1, b2))
#             board[y][x] = (a + b)/2
#             print b
#     for g in range(8):
#         print board[g]

def assignColor(x, y):
    cl = board[y][x]
    if (bounds[0][0] < cl < bounds[1][0]) | (400 < cl < 428):
        board[y][x] = gems[1][0]
    elif (bounds[0][1] < cl < bounds[1][1]):
        board[y][x] = gems[1][1]
    elif (bounds[0][2] < cl < bounds[1][2]) | (110 < cl < 121):
        board[y][x] = gems[1][2]
    elif (bounds[0][3] < cl < bounds[1][3]):
        board[y][x] = gems[1][3]
    elif (bounds[0][4] < cl < bounds[1][4]) | (235 < cl < 243) | (570 < cl < 640):
        board[y][x] = gems[1][4]
    elif ((bounds[0][5] < cl < bounds[1][5]) | (499 < cl < 503) | (745 < cl < 765)):
        board[y][x] = gems[1][5]
    elif (bounds[0][6] < cl < bounds[1][6]):
        board[y][x] = gems[1][6]
    else:
        recolorY.append(y)
        recolorX.append(x)
        print cl

# def colorGrab():
#     #autopy.bitmap.capture_screen().save('1.png')
#     autopy.bitmap.capture_screen_portion(boxGame).save('1.png')
#     screen = autopy.bitmap.Bitmap.open('1.png')
#     print 'start'
#     for y in range(8):
#         for x in range(8):
#             a1 = X_POS + 20 + x*40
#             a2 = Y_POS + 20 + y*40
#             b = hex(screen.get_color(a1, a2))
#             board[y][x] = b
#             print b
#     print board

# def main():
#     # screenGrabTitle()
#     # screenGrabGame()
#     colorGrab()

# if __name__ == '__main__':
#     time.sleep(3.0)
#     starttime = time.time()
#     counter = 0
#     while (counter < 15):
#         colorGrab_Pillow()
#         counter += 1
#         time.sleep(4.0 - ((time.time() - starttime) % 4.0))

# colorGrab()
colorGrab_Pillow()
#colorGrab_PillowGIF()
#colorGrab_PillowGIFDOUBLE()

print("--- %s seconds ---" % (time.time() - start_time))