import pygame, sys
from pygame.locals import *
from math import sqrt
windowSurface = pygame.display.set_mode((480, 320))
pygame.display.set_caption('输入端')
GRAY = (197, 197, 197)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
DARK_GRAY = (87, 84, 79)
WHITE = (255, 255, 255)
RED = (255,0,0)
pygame.init()
menu_font = pygame.font.Font("font/STFANGSO.ttf", 17)
menu_text = menu_font.render("输入端", True, BLACK)
clear_text = menu_font.render("清除", True, WHITE)
save_text = menu_font.render("写完", True, WHITE)
logo_text = menu_font.render("o(=•ェ•=)m", True, BLACK)

draw = False
brush_size = 2
brush_color = GREEN

menu_rect = pygame.Rect(0, 0, 100, 320)
screen_rect = pygame.Rect(100, 0, 380, 320)
clear_rect = pygame.Rect(5, 290, 60, 25)
save_rect = pygame.Rect(5, 260, 60, 25)
save_flag = False
file_number = 1

lst=[]
Lst=[]
ch='1'#input()
lbp=[]
breakPoint=True
while True:
    #Pygame 事件
    ex=False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            ex=True
            break
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                ex=True
                break
        if event.type == MOUSEBUTTONDOWN:
            draw = True
        if event.type == MOUSEBUTTONUP:
            draw = False
    if ex : break
    #Draw
    mouse_pos = pygame.mouse.get_pos()
    if draw == True and mouse_pos[0] > 100:
        if not(lst) or mouse_pos!=lst[-1]:
            lst.append(mouse_pos)
            if breakPoint:lbp.append(len(lst))
            #pygame.draw.circle(windowSurface, brush_color, mouse_pos, brush_size)
            if not(breakPoint):pygame.draw.line(windowSurface, brush_color, lst[-2], lst[-1])
            save_flag = False
    #Clear
    if draw == True:
        if clear_rect.collidepoint(mouse_pos):
            lst=[]
            pygame.draw.rect(windowSurface, BLACK, screen_rect)
    
    pygame.draw.rect(windowSurface, GRAY, menu_rect)
    windowSurface.blit(menu_text, (10, 20))
    
    pygame.draw.line(windowSurface, BLACK, (0, 100), (100, 100))
    pygame.draw.line(windowSurface, BLACK, (0, 105), (100, 105))
    
    pygame.draw.rect(windowSurface, DARK_GRAY, clear_rect)
    windowSurface.blit(clear_text, (10, 290))


    pygame.draw.rect(windowSurface, DARK_GRAY, save_rect)
    windowSurface.blit(save_text, (10, 262))
    windowSurface.blit(logo_text, (10, 60))
    
    if draw == True and save_flag == False:
        if save_rect.collidepoint(mouse_pos) and lst:
            #print(lst)
            print("File has been saved :P")
            save_surface = pygame.Surface((380, 320))
            save_surface.blit(windowSurface, (0, 0), (100, 0, 380, 320))
            pygame.draw.rect(windowSurface, BLACK, screen_rect)
            
            ll=[lst[0]]
            i=1
            while i<len(lst):
                if i+1 not in lbp:
                    dist=round(sqrt((lst[i][0]-lst[i-1][0])**2+(lst[i][1]-lst[i-1][1])**2))
                    tr=[[lst[i-1][0]+(lst[i][0]-lst[i-1][0])/dist*j,lst[i-1][1]+(lst[i][1]-lst[i-1][1])/dist*j] for j in range(dist)]
                    ll.extend(tr)
                    ll.append(lst[i])
                i+=1
            #print(ll)
            #for i in ll:
            #    pygame.draw.circle(windowSurface, brush_color, (i[0],i[1]), brush_size)
            llt=list(zip(*ll))
            #找重心
            cx,cy=sum(llt[0])/len(llt[0]),sum(llt[1])/len(llt[0])
            #pygame.draw.circle(windowSurface, RED, (round(cx),round(cy)), brush_size)#打印重心
            llt=[[llt[0][i]-cx for i in range(len(llt[0]))],[llt[1][i]-cy for i in range(len(llt[0]))]]
            #print(llt)
            maxLine=max(llt[0])
            minLine=min(llt[0])
            maxCol=max(llt[1])
            minCol=min(llt[1])
            ll=[[round(llt[0][i]/(maxLine-minLine)*300),round(llt[1][i]/(maxCol-minCol)*300)] for i in range(len(llt[0]))]
            #print(ll)
            #for i in ll:
            #    pygame.draw.circle(windowSurface, brush_color, (i[0]+290,i[1]+160), brush_size)
            #pygame.draw.circle(windowSurface, RED, (290,160), brush_size)
            Lst.append(ll)
            lst=[]
    pygame.display.update()
    breakPoint=not draw
f=open(ch+'.sav','w')
f.write(str(len(Lst)))
f.write("\n")
for i in range(len(Lst)):
    f.write(str(len(Lst[i])))
    f.write("\n")
    for j in range(len(Lst[i])):
        for k in range(len(Lst[i][j])):
            f.write(str(Lst[i][j][k]))
            f.write("\n")
print("finished")
f.close()
