# Name: Gurjas Chalana
# Student Number: 101234914 


from os import error
from typing import Text
import pygame
import textwrap
from pygame import image
from pygame.locals import *

# All initlizations 
Black = (0,0,0)
Grey = (220,220,220)
White = (255,255,255)
Red = (255,0,0)
Blue = (0,0,255)
Size = (1920,1080)
y = 500
ctr = 0
y2 = 500
y3 = 100
image = 0
pygame.init()
TextList = []
Line = open('end_credits.txt','r')
Screen = pygame.display.set_mode(Size)
font = pygame.font.SysFont('Arial', 45)

# Appending all my images, into the list I created
ImageList = []
im1 = pygame.image.load('Assignment1.png').convert()
im2 = pygame.image.load('Assignment2.png').convert()
im3 = pygame.image.load('Assignment3.png').convert()
im4 = pygame.image.load('Assignment4.png').convert()
im7 = pygame.image.load('Assignment7.png').convert()
im8 = pygame.image.load('Assignment8.png').convert()
im9 = pygame.image.load('Assignment9.png').convert()
im10 = pygame.image.load('Assignment10.png').convert()
ImageList.append(im1)
ImageList.append(im2)
ImageList.append(im3)
ImageList.append(im4)
ImageList.append(im7)
ImageList.append(im8)
ImageList.append(im9)
ImageList.append(im10)

# Checks for the index value found in the .txt, converts into an int and uses it as x to resume the text from where it was left off 
try: 
    Lastline = open('LastLine.txt','r')
    Line3 = Lastline.readline()
    x = int(Line3)  
    # Checks for the index value of the image, if lastline.txt is found then uses it as the value for the index of the image to resume the slideshow from the point it was left on  
    try:
        LastImage = open('LastImage.txt','r')
        Line4 = LastImage.readline()
        image = int(Line4)
    # If the file for lastline.txt isn't found, then it doesn't try to search for the index in LastImage.txt, and Image index is = 0 
    except:
        image = 0

# If the file doesn't open, just restart the credit scene, from x = 0     
except:
    x = 0
  

# Loop to turn lines into indexes of a list
Line2 = Line.readline()
while len(Line2) > 0:
    # If length of the line is greater than 40, it will split it into 4, otherwise it will keep it as a single line and print it with other lines  
    if len(Line2) > 40:
        a = len(Line2)//4
        b = len(Line2)//2
        c = a + b
        Line2 = Line2.rstrip('\n')
        TextList.append(Line2[:a])
        TextList.append(Line2[a:b])
        TextList.append(Line2[b:c])
        TextList.append(Line2[c:])
    # If the line is too short, then it will be written along with the next 3 indexes
    else:
        Line2 = Line2.rstrip('\n')
        TextList.append(Line2)
    Line2 = Line.readline()


# While loop for the code that manipulates the screen
exit_flag = False 
while not exit_flag:

# Tries to run through indexes, to render the font, this wraps the text as best as I could.   

    try:  
        FontScreen = font.render(TextList[x] ,True,Black)
        Screen.blit(FontScreen, (850,y))

        FontScreen2 = font.render(TextList[x+1] ,True,Black)
        Screen.blit(FontScreen2, (850,y+55))
        
        FontScreen3 = font.render(TextList[x+2] ,True,Black)
        Screen.blit(FontScreen3, (850,y + 110))

        FontScreen4 = font.render(TextList[x+3] ,True,Black)
        Screen.blit(FontScreen4, (850,y+165))

    



           
# Loops indefinity, until the program is terminated. 
    except IndexError: 
        x = 0
        image = 0
    
    
# - the y value,  if the y value is less than 0 equate it to 1080 and add 4 to the x value, this is so a new line shows up with the rolling affect. 
    y -= 2
    pygame.time.delay(10)
    if y < 0: 
        y = 1080
        x += 4  
    



    # Images
    
    y2 -= 2
    try:
        Screen.blit(ImageList[image], (0, y2))
# Loops indefinity, until the program is terminated. 
    except IndexError:
        image = 0
        
# - the y value,  if the y value is less than 0 equate it to 1080 and add 4 to the x value, this is so a new line shows up with the rolling affect. 
    if y2 < 0: 
        image += 1
        y2 = 1080 
        pygame.time.delay(10)
    

    pygame.display.update()
    Screen.fill(Grey) 

    
# If they terminate the process, Get the index of the line they left on for images and text, so that it can use it for the try and except to resume the credits. 

    for e in pygame.event.get(): 
        if e.type == pygame.QUIT:           
            with open('LastLine.txt', 'w') as f:
                f.write(str(x))
            with open('Lastimage.txt', 'w') as f:
                f.write(str(image))
            exit_flag = True
            


pygame.quit()


