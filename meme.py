
import pygame, sys,os,time
import sqlite3
baglanti = sqlite3.connect('database.db')
baglanti.row_factory = sqlite3.Row
veritabani_sec = baglanti.cursor()
oku = veritabani_sec.execute('Select sec,minu,hour,day,month,year,tl,ml,loc,gmt from numbers')
for verileri_cek in oku.fetchall():
    sec =  int(verileri_cek['sec'])
    minu =int(verileri_cek['minu'])
    hour = int(verileri_cek['hour'])
    day =  int(verileri_cek['day'])
    month = int(verileri_cek['month'])
    year = int(verileri_cek['year'])
    tl = int(verileri_cek['tl'])
    ml = int(verileri_cek['ml'])
    loc = str(verileri_cek['loc'])
    gmt = str
    (verileri_cek['gmt'])
baglanti.commit()
baglanti.close()
pygame.init()





############
display_width = 1500
display_height = 1100
############
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
##########
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('KAKA')
clock = pygame.time.Clock()
##########
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
######
def message_display6(text):
    largeText = pygame.font.Font('freesansbold.ttf',300)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((1200),(300))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
######
def message_display5(text):
    largeText = pygame.font.Font('freesansbold.ttf',300)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((300),(300))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
######
def message_display4(text):
    largeText = pygame.font.Font('freesansbold.ttf',250)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((750),(600))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
########
def message_display3(text):
    largeText = pygame.font.Font('freesansbold.ttf',70)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((1100),(50))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    


######
def message_display2(text):
    largeText = pygame.font.Font('freesansbold.ttf',120)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((750),(900))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    

########
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',200)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((750),(300))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)
    game_loop()
########

##########
def crash():
    global sec
    global minu
    global hour
    global day
    global month
    global year
    global tl
    global ml
    global loc
    global gmt
    global fuckyourself
    if sec <60:
        sec=sec+1
    if sec == 60:
        sec=1
        minu = minu+1
    if ml == 1 and minu ==30 :
        ml =2
        minu = 0
    if ml ==2 and minu == 30:
        hour = hour +1
        ml = 1
        minu = 0
 
    if 12 == hour and tl ==1:
        hour = 1
        tl = 2
    if 12 == hour and tl ==2:
        tl =1
        hour = 1
        day = day +1
    if month == 1 and day == 32:
        day = 1
        month = month + 1
    if month == 3 and day == 32:
        day = 1
        month = month + 1
    if month == 5 and day == 32:
        day = 1
        month = month + 1
    if month == 7 and day == 32:
        day = 1
        month = month + 1
    if month == 8 and day == 32:
        day = 1
        month = month + 1
    if month == 10 and day == 32:
        day = 1
        month = month + 1
    if month == 12 and day == 32:
        day = 1
        month = month + 1
    if month == 4 and day ==31:
        day = 1
        month = month + 1
    if month == 6 and day ==31:
        day = 1
        month = month + 1
    if month == 9 and day ==31:
        day = 1
        month = month + 1
    if month == 11 and day ==31:
        day = 1
        month = month + 1
    if month == 13:
        month = 1
        year = year + 1
    fuckyourself = year%4   
    if fuckyourself == 0:
        if month == 2 and day == 30:
            day = 1
            month = month + 1
    else:
        if month == 2  and  day ==29:
            day = 1
            month = month + 1
    
    global result
    global globul
    global result2
    global globul2
    global result3
    global globul3
    global result4
    global globul4
    global result5
    global globul5
    global result6
    global globul6
    
    result =(str(hour)+(":")+str(minu))
    result2= (str(month)+("/")+str(day)+("/")+str(year))
    result3= (("location")+("=")+str(loc)+("  gmt =")+str(gmt))
    result4= ("(")+str(sec)+(")")
    result5= str(tl)+("|")
    result6= str("|")+str(ml)

    globul = str(result)
    globul2= str(result2)
    globul3= str(result3)
    globul4=str (result4)
    globul5 =str (result5)
    globul6=str(result6)


    message_display6(globul6)
    message_display5(globul5)
    message_display4(globul4)
    message_display3(globul3)
    message_display2(globul2)
    message_display(globul)

    
##########
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    gameExit = False
########
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        crash()
        pygame.display.update()
        clock.tick(60)
########        
game_loop()
pygame.quit()
