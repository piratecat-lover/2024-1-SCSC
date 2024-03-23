import os
import pygame
from pygame.locals import *

# parameter
# name: string 이름 can be null
# background : string 배경화면 이미지 이름
# object : string 오브젝트 이미지 이름 can be null
# script : string 대사
#
# return void
def render_talk(name, background, object, script):
    Image(background, (0, 0), (1600, 900)).draw()
    Image(object, (1200, 200), (400, 400)).draw()
    
    Rectangle("#FFFFFF", (0, 500), (500, 100)).draw()
    Text(name, (0, 500), color = "#0000FF", font = "malgungothic", fontSize = 50).draw()
    
    Rectangle("#FF00FF", (0, 600), (1600, 400)).draw()
    Text(script, (0, 600), color = "#0000FF", font = "malgungothic", fontSize = 50).draw()
    
    
    
    pygame.display.flip()

# parameter
# name: string 이름 can be null
# background : string 배경화면 이미지 이름
# object : string 오브젝트 이미지 이름 can be null
# script : string 대사
# select : array of string 선택지들
#
# return 0~3 int 선택지 번호
def render_select(name, background, object, script, select):

    
    Image(background, (0, 0), (1600, 900)).draw()
    Image(object, (1200, 200), (400, 400)).draw()

    Rectangle("#FFFFFF", (0, 300), (500, 100)).draw()
    Text(name, (0, 300), color = "#000000", font = "malgungothic", fontSize = 50).draw()
                
    Rectangle("#FFFF00", (0, 400), (1200, 200)).draw()
    Text(script, (0, 400), color = "#000000", font = "malgungothic", fontSize = 50).draw()

    buttons = [
        Button(select[0], "#00FFFF", (0, 600), (1600, 75), 0, font = "malgungothic", fontSize = 50, textColor = "#FFFFFF", textPos = (0, 0)),
        Button(select[1], "#00FF00", (0, 675), (1600, 75), 1, font = "malgungothic", fontSize = 50, textColor = "#FFFFFF", textPos = (0, 0)),
        Button(select[2], "#FF00FF", (0, 750), (1600, 75), 2, font = "malgungothic", fontSize = 50, textColor = "#FFFFFF", textPos = (0, 0)),
        Button(select[3], "#FF0000", (0, 825), (1600, 75), 3, font = "malgungothic", fontSize = 50, textColor = "#FFFFFF", textPos = (0, 0))]



    for button in buttons:
        button.draw()

    pygame.display.flip()

    inputManager = InputManager(buttons)
    while True:
        inputManager.update()
        res = inputManager.getButton()
        if res != []:
            print(res[-1])
            break    
        

# parameter
# background : string 배경화면 이미지 이름
# script : string 대사
#
# return void
def render_ending(background, script, score):
    Image(background, (0, 0), (1600, 900)).draw()

    Rectangle("#FFFF00", (400, 300), (800, 200)).draw()
    Text(script, (400, 300), color = "#000000", font = "malgungothic", fontSize = 50).draw()

    Rectangle("#00FFFF", (400, 500), (800, 200)).draw()
    Text('Score: ' + str(score), (400, 500), color = "#000000", font = "malgungothic", fontSize = 50).draw()

    pygame.display.flip()
    
    pass

# parameter
# background : string 배경화면 이미지 이름
# is_there_save : bool 세이브 파일 존재 여부 (continue 등)
#
# return
# 0 : new game
# 1 : contiunue
# 2: load_game < - 나중에
# 3 : exit
# 4 : 왼쪽으로 이동
# 5 : 오른쪽으로 이동
def render_title(background, is_there_save):
    Image(background, (0, 0), (1600, 900)).draw()

    if not is_there_save:
        buttons = [
            Button('LEFT', "#00FFFF00", (0, 0), (200, 900), 4, font = "malgungothic", fontSize = 50, textColor = "#FFFFFF", textPos = (0, 0)),
            Button('RIGHT', "#00FF00FF", (1400, 0), (200, 900), 5, font = "malgungothic", fontSize = 50, textColor = "#FFFFFF", textPos = (0, 0)),
            Button('new game', "#FF00FF", (500, 500), (600, 100), 0, font = "malgungothic", fontSize = 50, textColor = "#FFFFFF", textPos = (0, 0)),
            Button('exit', "#FF0000", (500, 650), (600, 100), 3, font = "malgungothic", fontSize = 50, textColor = "#FFFFFF", textPos = (0, 0))]
    else:
        buttons = [
            Button('LEFT', "#00FFFF00", (0, 0), (200, 900), 4, font = "malgungothic", fontSize = 50, textColor = "#FFFFFF", textPos = (0, 0)),
            Button('RIGHT', "#00FF00FF", (1400, 0), (200, 900), 5, font = "malgungothic", fontSize = 50, textColor = "#FFFFFF", textPos = (0, 0)),
            Button('continue', "#FF00FF", (500, 500), (600, 75), 1, font = "malgungothic", fontSize = 50, textColor = "#FFFFFF", textPos = (0, 0)),
            Button('new game', "#FF00FF", (500, 600), (600, 75), 0, font = "malgungothic", fontSize = 50, textColor = "#FFFFFF", textPos = (0, 0)),
            Button('load game', "#FF0000", (500, 700), (600, 75), 2, font = "malgungothic", fontSize = 50, textColor = "#FFFFFF", textPos = (0, 0)),
            Button('exit', "#FF0000", (500, 800), (600, 75), 3, font = "malgungothic", fontSize = 50, textColor = "#FFFFFF", textPos = (0, 0))]

    for button in buttons:
        button.draw()

    pygame.display.flip()
    
    inputManager = InputManager(buttons)
    while True:
        inputManager.update()
        res = inputManager.getButton()
        if res != []:
            print(res[-1])
            break    
    

# parameter
# background : string 배경화면 이미지 이름
#
# return
# username:string(이름 검증 완료)
def render_name(background):
    Image(background, (0, 0), (1600, 900)).draw()

    buttons = [
        Button('Your name', "#FF00FF", (500, 500), (600, 100), 0, font = "malgungothic", fontSize = 50, textColor = "#FFFFFF", textPos = (0, 0))]

    for button in buttons:
        button.draw()

    pygame.display.flip()

    inputManager = InputManager(buttons)
    while True:
        inputManager.update()
        res = inputManager.getButton()
        if res != []:
            print(res[-1])
            break  
    
    pass



'''
----------------------------------------------------------------------------------
'''

def colorCode2Tuple(colorCode):
    if type(colorCode) != str:
        return (0, 0, 0)
    if colorCode[0] == '#':
        dec = int(colorCode[1:], 16)
        if len(colorCode) == 7:
            return pygame.Color(dec // 65536, (dec % 65536) // 256, dec % 256)
        elif len(colorCode) == 9:
            return pygame.Color(dec // 16777216,(dec % 16777216) // 65536, (dec % 65536) // 256, dec % 256)
    else:
        return (0, 0, 0)

class Text:
    def __init__(self, content, pos, font = "malgungothic", fontSize = 50, color = "#FFFFFF", lineSpacing = 120):
        tempContent = ['']
        for char in content:
            if char != '\n':
                tempContent[-1] += char
            else:
                tempContent += ['']
        self.content = tempContent
        self.pos = pos
        self.color = color
        self.font = font
        self.fontSize = fontSize
        self.lineSpacing = lineSpacing
    def draw(self):
        for i in range(len(self.content)):
            TextData = pygame.font.SysFont(self.font, self.fontSize).render(self.content[i], True, colorCode2Tuple(self.color))
            TextRect = TextData.get_rect();
            TextRect.topleft = (self.pos[0], self.pos[1] + i * int(self.fontSize * self.lineSpacing / 100))
            screen.blit(TextData, TextRect)

class Image:
    def __init__(self, path, pos, size):
        if path[0] != '#':
            self.content = pygame.transform.scale(pygame.image.load(path), size)
        else:
            self.content = path
        self.size = size
        self.pos = pos
    def draw(self):
        if type(self.content) != str:
            screen.blit(self.content, self.pos)
        else:
            pygame.draw.rect(screen, colorCode2Tuple(self.content), (self.pos[0], self.pos[1], self.size[0], self.size[1]))
            
class Rectangle:
    def __init__(self, color, pos, size, width = 0):
        self.color = color
        self.pos = pos
        self.size = size
        self.width = width
    def draw(self):
        pygame.draw.rect(screen, colorCode2Tuple(self.color), (self.pos[0], self.pos[1], self.size[0], self.size[1]), self.width)
        
class Button:
    def __init__(self, text, image, pos, size, key, font = "malgungothic", fontSize = 50, textColor = "#FFFFFF", textPos = (0, 0)):
        self.text = Text(text, (pos[0] + textPos[0], pos[1] + textPos[1]), font, fontSize, textColor)
        self.image = Image(image, pos, size)
        self.pos = pos
        self.size = size
        self.key = key
    def draw(self):
        self.image.draw()
        self.text.draw()

class InputManager:
    def __init__(self, inputs):
        self.inputs = inputs
        self.buttonQ = []
        self.keyQ = []
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i in self.inputs:
                    if type(i) == Button:
                        if pygame.Rect(i.pos[0], i.pos[1], i.size[0], i.size[1]).collidepoint(event.pos):
                            self.buttonQ += [i.key]
                        
    def getButton(self):
        temp = self.buttonQ[:]
        self.buttonQ = []
        return temp

    def getKey(self):
        temp = self.keyQ[:]
        self.keyQ = []
        return temp
        
    
        


pygame.init()
screen = pygame.display.set_mode((1600, 900), DOUBLEBUF)
pygame.display.set_caption('Hello World!')

os.chdir('C:\\Users\sungj\\Desktop\\sandbox')
#render_talk('Name', 'bubble_bobble_starting.png', 'bubble_bobble_player.png', 'Script: 첫째줄\n둘째줄\n셋째줄')
#render_select('Name', 'bubble_bobble_starting.png', 'bubble_bobble_player.png', 'Script: 첫째줄\n둘째줄\n셋째줄', ['ABC', 'DEF', 'GHI', 'JKL'])
#render_ending('bubble_bobble_starting.png', 'Script: 첫째줄\n둘째줄\n셋째줄', 100)
#render_title('bubble_bobble_starting.png', True)
render_name('bubble_bobble_starting.png')
