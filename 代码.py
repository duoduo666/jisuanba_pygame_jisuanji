import sys
import pygame
from pygame.locals import *

def calculater():
    def pscreen():
        screen.fill(c)
        screen.blit(one,(300,300))
        screen.blit(two,(400,300))
        screen.blit(three,(500,300))
        screen.blit(four,(300,400))
        screen.blit(five,(400,400))
        screen.blit(six,(500,400))
        screen.blit(seven,(300,500))
        screen.blit(eight,(400,500))
        screen.blit(nine,(500,500))
        screen.blit(zero,(400,600))
        #导运算符
        screen.blit(dian,(500,600))
        screen.blit(jia,(625,298))
        screen.blit(jian,(625,398))
        screen.blit(cheng,(625,498))
        screen.blit(chu,(625,598))
        screen.blit(deng,(300,600))
        screen.blit(geng2,(725,298))
        screen.blit(mi,(725,398))
        screen.blit(geng,(125,300))
        screen.blit(zkuo,(125,400))
        screen.blit(ykuo,(125,500))
        screen.blit(mi2,(125,600))
        #图标
        screen.blit(title,(100,200))
        screen.blit(sal,(350,0))
        screen.blit(ac,(350,800))
        #常数
        screen.blit(pi,(725,498))
        screen.blit(e,(725,598))
        pygame.display.update()
    pygame.init()
    screen_size = width,height = 1000, 1000
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("计算器")
    c = (255,255,255)
    p = (400,225)
    num = ""
    snum = ""
    t = pygame.font.SysFont("arial",32)
    s = pygame.font.SysFont("arial",20)
    #导入图片
    #数字
    ad = ("E://duoduo2/jisuanxia/")
    zero = pygame.image.load(ad + "py0.png")
    one = pygame.image.load(ad + "py1.png")
    two = pygame.image.load(ad + "py2.png")
    three = pygame.image.load(ad + "py3.png")
    four = pygame.image.load(ad + "py4.png")    
    five = pygame.image.load(ad + "py5.png")    
    six = pygame.image.load(ad + "py6.png")
    seven = pygame.image.load(ad + "py7.png")    
    eight = pygame.image.load(ad + "py8.png")
    nine = pygame.image.load(ad + "py9.png")
    #图标
    al = pygame.image.load(ad + "pyall.png")
    sal = pygame.image.load(ad + "smallall.png")
    ji = pygame.image.load(ad + "pyji.png")
    suan = pygame.image.load(ad + "pysuan.png")
    begin = pygame.image.load(ad + "begin.png")
    title = pygame.image.load(ad + "title.png")
    ac = pygame.image.load(ad + "ac.png")
    #运算符
    dian = pygame.image.load(ad + "pydian.png")
    jia = pygame.image.load(ad + "jia.png")
    jian = pygame.image.load(ad + "jian.png")
    cheng = pygame.image.load(ad + "cheng.png")
    chu = pygame.image.load(ad + "pychu.png")
    deng = pygame.image.load(ad + "deng.png")
    geng2 = pygame.image.load(ad + "geng2.png")
    mi = pygame.image.load(ad + "mi.png")
    geng = pygame.image.load(ad + "geng.png")
    zkuo = pygame.image.load(ad + "zkuo.png")
    ykuo = pygame.image.load(ad + "ykuo.png")
    mi2 = pygame.image.load(ad + "mi2.png")
    #常数
    pi = pygame.image.load(ad + "pi.png")
    e = pygame.image.load(ad + "e.png")
    #正文
    #开始屏
    screen.fill(c)
    screen.blit(al,(225,250))
    screen.blit(zero,(300,100))
    screen.blit(one,(100,60))
    screen.blit(two,(800,200))
    screen.blit(three,(150,800))
    screen.blit(four,(750,800))
    screen.blit(five,(500,80))
    screen.blit(six,(40,300))
    screen.blit(seven,(800,500))
    screen.blit(eight,(600,600))
    screen.blit(nine,(100,600))
    screen.blit(begin,(350,800))
    pygame.display.flip()
    
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 350 <= x <= 636 and 800 <= y<= 875:
                    pscreen()
                if 300 < x < 400 and 300 < y < 400:     #1
                    num += str(1)
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if 400 <= x <= 500 and 300 < y <400:    #2
                    num += str(2)
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if 500 <= x <= 600 and 300 < y <400:    #3
                    num += str(3)
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if 300 < x < 400 and 400 < y < 500:     #4
                    num += str(4)
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update() 
                if 400 < x < 500 and 400 < y < 500:     #5
                    num += str(5)
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if 500 < x < 600 and 400 < y < 500:     #6
                    num += str(6)
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if 300 < x < 400 and 500 < y < 600:     #7
                    num += str(7)
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if 400 < x < 500 and 500 < y < 600:     #8
                    num += str(8)
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if 500 < x < 600 and 500 < y < 600:     #9
                    num += str(9)
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if 400 < x < 500 and 600 < y < 700:     #0
                    num += str(0)
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if 500 < x < 600 and 600 < y < 700:     #.
                    num += "."
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if 625 < x < 725 and 298 < y < 398:     #加号
                    num += "+"
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if 625 < x < 725 and 398 < y < 498:     #减号
                    num += "-"
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if 625 < x < 725 and 498 < y < 598:     #乘号
                    num += "*"
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if 625 < x < 725 and 598 < y < 698:     #除号
                    num += "/"
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if 725 <x < 825 and 298 < y < 398:      #根号2
                    num += "**0.5"
                    snum += "2,"
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    sword = s.render(snum,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    screen.blit(sword,(500,200))
                    pygame.display.update()
                if 725 < x < 825 and 398 < y < 498:     #算一个属的 幂
                    num += "**"
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if 725 < x < 825 and 498 < y < 598:    #pi 圆周率 兀
                    num += str(3.14159265358)
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if 725 <x < 825 and 598 < y < 698:      #常数e 
                    num += str(2.7182818284)
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if 125 < x < 225 and 300 < y < 400:    #任意根号
                    num += "+0"
                    num = str(eval(num))
                    num += "**(1/"
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if 125 < x < 225 and 400 < y < 500:   #左括号
                    num += "("
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if 125 < x < 225 and 500 < y < 600:   #右括号
                    num += ")"
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if 125 < x < 225 and 600 < y < 700:    #2次方——mi2
                    num += "**2"
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if 300 < x < 400 and 600 < y < 700:     #等号 =
                    pscreen()
                    try:
                        num += "+0"
                        a = str(eval(num))
                        word = t.render(a,True,(0,0,0),(225,225,225))
                        screen.blit(word,p)
                        num = ""
                        snum = ""
                        pygame.display.update()
                    except BaseException:
                        pig = "Are you kidding? What did you do!"
                        pigword = t.render(pig,True,(0,0,0),(225,225,225))
                        screen.blit(pigword,p)
                        num = ""
                        snum = ""
                        pygame.display.update()
                    finally:
                        pygame.display.update()
            #键盘处理
            if event.type == KEYDOWN:
                if event.key == K_1 or event.key == K_KP1:      #1                               #数字
                    num += str(1)
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if event.key == K_2 or event.key == K_KP2:      #2
                    num += str(2)
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if event.key == K_3 or event.key == K_KP3:      #3
                    num += str(3)
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if event.key == K_4 or event.key == K_KP4:      #4
                    num += str(4)
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if event.key == K_5 or event.key == K_KP5:      #5
                    num += str(5)
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if event.key == K_6 or event.key == K_KP6:      #6
                    num += str(6)
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if event.key == K_7 or event.key == K_KP7:      #7
                    num += str(7)
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if event.key == K_8 or event.key == K_KP8:      #8
                    num += str(8)
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if event.key == K_9 or event.key == K_KP9:      #9
                    num += str(9)
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if event.key == K_0 or event.key == K_KP0:      #0
                    num += str(0)
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                
                if event.key == K_PLUS or event.key == K_KP_PLUS:            #加号          #符号
                    num += "+"
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if event.key == K_ASTERISK or event.key == K_KP_MULTIPLY:    #乘号
                    num += "*"
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if event.key == K_SLASH or event.key == K_KP_DIVIDE:         #除号
                    num += "/"
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if event.key == K_MINUS or event.key == K_KP_MINUS:           #减号
                    num += "-"
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if event.key == K_PERIOD or event.key == K_KP_PERIOD:         #.
                    num += "."
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if event.key == K_g:                                          #根号
                    num += "**0.5"
                    snum += "2,"
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    sword = s.render(snum,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    screen.blit(sword,(500,200))
                    pygame.display.update()
                if event.key == K_m:                                          #幂
                    num += "**"
                    word = t.render(num,True,(0,0,0),(225,225,225))
                    screen.blit(word,p)
                    pygame.display.update()
                if event.key == K_p:                                           #pi 
                    num += str(3.14159265358)
                    word = t.render(num,True,(0,0,0),(225,225,225))           
                    screen.blit(word,p)
                    pygame.display.update()
                    
                if event.key == K_EQUALS or event.key == K_RETURN or event.key == K_KP_ENTER:                                     #=
                    pscreen()
                    try:
                        num += "+0"
                        a = str(eval(num))
                        word = t.render(a,True,(0,0,0),(225,225,225))
                        screen.blit(word,p)
                        num = ""
                        snum = ""
                        pygame.display.update()
                    except BaseException:
                        pig = "Are you kidding? What did you do!"
                        pigword = t.render(pig,True,(0,0,0),(225,225,225))
                        screen.blit(pigword,p)
                        num = ""
                        snum = ""
                        pygame.display.update()
                    finally:
                        pygame.display.update()

calculater()
