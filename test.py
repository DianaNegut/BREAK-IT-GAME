import pygame
from pygame import mixer
from pygame.locals import *
from Wall import wall 
from Paddle import paddle
import math
pygame.init()





#red green blue format
Gri=(128,128,128)
Orange=(255,69,0)
Maro=(139,69,19)
Alb=(255,255,255)
Verde=(0,255,0)
Galben=(255,255,0)
Negru=(0,0,0)
Albastru = (0, 0, 255)


cols=8
rows=6
count=0
score=0




#le folosesc pt a determina dimensiunea paletei
bigger=False
smaller=True



#variabile 
speed_state=0
special_state=0
game_over=0
live_ball=False
ball_x=0
ball_y=0
highscore=0
speed_ok=False



#muzica
mixer.music.load("background.wav")
mixer.music.play(-1) 






#informatii gloante
bulletImg=pygame.image.load('bullet.png')
bulletX=0
bulletY=575
bulletY_change=5
bullet_state="ready"
nr_bullet=0





#definesc functia pt a trage un glont 
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    #drawing one image onto another
    screen.blit(bulletImg,(x+20,y))





#coliziune glont-caramida
def isCollision(bulletX, bulletY, wallX, wallY):
    bullet_rect = pygame.Rect(bulletX, bulletY, bulletImg.get_width(), bulletImg.get_height())
    wall_rect = pygame.Rect(wallX, wallY, wall.width, wall.height)
    #verific daca scele 2 dreptunghiuri se suprapun
    if bullet_rect.colliderect(wall_rect):
        return True
    else:
        return False
    



#citesc highscore
def load_highscore():
    global highscore
    try:
        with open ("high.txt", "r") as file:
            highscore=int(file.read())
    except FileExistsError:
        highscore=0



#modific highscore
def save_highscore():
    with open("high.txt", "w") as file:
        file.write(str(highscore))



#updatez highscore
def update_highscore(score):
    global highscore
    if (score>highscore):
        highscore=score
        save_highscore()




#afisez pe ecran highscoreul
def draw_score(screen):
    font = pygame.font.Font(None, 36)
    text = font.render("Highscore: " + str(highscore), True, Alb)
    text_rect = text.get_rect()
    text_rect.bottomright = (590, 590)  
    screen.blit(text, text_rect)

    

        

#Ball class
class ball():
    #valoarea initiala a bilei
    def __init__(self,x,y):
        self.reset(x,y)
    
    def move(self):
        #o sa o folosesc sa verific daca peretele a fost distrus complet, adica daca bila a atins partea de sus a ecranului (daca da atunci a castigat utilizatorul)
        wall_destroyed=1
        if self.rect.top<0:
            self.game_over=1

        row_count=0
        distance=10

        for row in wall.blocks:
            item_count=0

            for item in row:
                #verificam coliziunea dintre dreptunghiurile mingii si a blocului curent
                if self.rect.colliderect(item[0]):
                     collisionSound = mixer.Sound("collision.mp3")
                     collisionSound.play()
                    
                     global score,bulletY5
                    #coliziune cu partea de sus si bila se deplaseaza in jos
                     if abs(self.rect.bottom-item[0].top)<distance and self.speed_y>0:

                        self.speed_y*=-1
                        if wall.blocks[row_count][item_count][1]==1  :
                            score+=1
                            update_highscore(score)
                    #col cu partea de jos si bila merge in sus
                     if abs(self.rect.top-item[0].bottom)<distance and self.speed_y<0:
                        self.speed_y*=-1
                        if wall.blocks[row_count][item_count][1]==1  :
                            score+=1
                            update_highscore(score)
                    #col partea dreapta a bilei cu partea stanga a caramizii, bila merge spre dreapta
                     if abs(self.rect.right-item[0].left)<distance and self.speed_x>0:
                        self.speed_x*=-1
                        if wall.blocks[row_count][item_count][1]==1 :
                            score+=1
                            update_highscore(score)
                    #col partea s a bilei cu partea d a caramizii, bila merge spre s
                     if abs(self.rect.left-item[0].right)<distance and self.speed_x<0:
                        self.speed_x*=-1
                        if wall.blocks[row_count][item_count][1]==1:
                            score+=1
                            update_highscore(score)
                   
                     global special_state
 
                     if wall.blocks[row_count][item_count][1]==0.9:
                        special_state+=1
                        score+=1
                       
                        update_highscore(score)
                       
                       

                        self.ok=True
                      #  print(special_state)
                    
                     if special_state!=0 and self.ok==True:
                        #6 si 1 sunt limitele superioare ale peretelui
                        #aici fac efectul exploziv al caramizilor verzi
                        if row_count>=1:
                            if wall.blocks[row_count-1][item_count][1]<3 and wall.blocks[row_count-1][item_count][1]!=0:
                                wall.blocks[row_count-1][item_count][1]=0
                                wall.blocks[row_count-1][item_count][0]=(0,0,0,0)
                                score+=1
                                update_highscore(score)

                            if item_count<=6 and wall.blocks[row_count-1][item_count+1][1]<3 and wall.blocks[row_count-1][item_count+1][1]!=0:
                                wall.blocks[row_count-1][item_count+1][1]=0
                                wall.blocks[row_count-1][item_count+1][0]=(0,0,0,0)
                                score+=1
                                update_highscore(score)
                            
                            if item_count>=1 and wall.blocks[row_count-1][item_count-1][1]<3 and wall.blocks[row_count-1][item_count-1][1]!=0 :
                                wall.blocks[row_count-1][item_count-1][1]=0
                                wall.blocks[row_count-1][item_count-1][0]=(0,0,0,0)
                                score+=1
                                update_highscore(score)
                   
                        if item_count>=1 and wall.blocks[row_count][item_count-1][1]<3 and wall.blocks[row_count][item_count-1][1]!=0:
                            wall.blocks[row_count][item_count-1][1]!=0
                            wall.blocks[row_count][item_count-1][0]=(0,0,0,0)
                            score+=1
                            update_highscore(score)

                        if item_count<=6 and wall.blocks[row_count][item_count+1][1]<3 and wall.blocks[row_count][item_count+1][1]!=0:
                            wall.blocks[row_count][item_count+1][1]=0
                            wall.blocks[row_count][item_count+1][0]=(0,0,0,0)
                            score+=1
                            update_highscore(score)
                        
                        if row_count<=4:
                            if wall.blocks[row_count+1][item_count][1]<3 and wall.blocks[row_count+1][item_count][1]!=0:
                                wall.blocks[row_count+1][item_count][1]=0
                                wall.blocks[row_count+1][item_count][0]=(0,0,0,0)
                                score+=1
                                update_highscore(score)

                            if item_count>=1 and wall.blocks[row_count+1][item_count-1][1]<3 and wall.blocks[row_count+1][item_count-1][1]!=0:
                                wall.blocks[row_count+1][item_count-1][1]=0
                                wall.blocks[row_count+1][item_count-1][0]=(0,0,0,0)
                                score+=1
                                update_highscore(score)

                            if item_count<=6 and wall.blocks[row_count+1][item_count+1][1]<3 and wall.blocks[row_count+1][item_count+1][1]!=0:
                                wall.blocks[row_count+1][item_count+1][1]=0
                                wall.blocks[row_count+1][item_count+1][0]=(0,0,0,0)
                                score+=1
                                update_highscore(score)

                     self.ok=False
                     if special_state>3:
                        special_state=0
                     if wall.blocks[row_count][item_count][1]>1:
                        wall.blocks[row_count][item_count][1]-=1
                     else:
                        wall.blocks[row_count][item_count][0]=(0,0,0,0)
                
                if wall.blocks[row_count][item_count][1]<3:
                    #inseamna ca zidul nu a fost distrus complet
                    wall_destroyed=0
                item_count+=1

            row_count+=1
        if wall_destroyed==1:
            self.game_over=1
        #bila loveste lateralele ecranului
        if self.rect.left<0 or self.rect.right>600:
            self.speed_x*=-1
         #bila loveste partea de sus a ecranului
        if self.rect.top<0:
            self.speed_y*=-1
        #bila loveste partea de jos a ecranului
        if self.rect.bottom>600:
            self.game_over=-1
        
        global ball_x,ball_y
        ball_y=(self.rect.bottom +self.rect.top)/2
        ball_x=(self.rect.left+self.rect.right)/2

        #ricoseu paleta
        if self.rect.colliderect(paddle)==True:
            if abs(self.rect.bottom-paddle.rect.top)<distance and self.speed_y>0:
                self.speed_y*=-1
        


        #aici deplasez bila pe ecran
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y

        return self.game_over

    def draw(self):
        #desenez cercul cu conturul de 2 pixeli
        pygame.draw.circle(screen,Alb,(self.rect.x+self.ball_rad,self.rect.y+self.ball_rad),self.ball_rad)
        pygame.draw.circle(screen,Gri,(self.rect.x+self.ball_rad,self.rect.y+self.ball_rad),self.ball_rad,2)  

    def reset(self,x,y):
        self.ball_rad=10
        self.x=x-self.ball_rad
        self.y=y

        global speed_ok

        if speed_ok==False:
            self.speed_x=2
            self.speed_y=-2
        #daca viteza bilei este implicita
        if speed_state==0 and speed_ok==True:
            if self.speed_x>0:
                self.speed_x=2
            else:
                self.speed_x=-2
            if self.speed_y>0:
                self.speed_y=2
            else:
                self.speed_y=-2
            distance=20

        self.rect=Rect(self.x,self.y, self.ball_rad*2, self.ball_rad*2)
        self.game_over=0
        self.ok=False
        #daca viteza a fost crescuta
        if speed_state==1:
            if self.speed_x>0:
                self.speed_x=3
            else:
                self.speed_x=-3

            if self.speed_y>0:
                self.speed_y=3
            else:
                self.speed_y=-3
            distance=15
        elif speed_state==2:
            
            if self.speed_x>0:
                self.speed_x=4
            else:
                self.speed_x=-4

            if self.speed_y>0:
                self.speed_y=4
            else:
                self.speed_y=-4
            distance=20
        
load_highscore()
#create wall
wall=wall()
wall.create_wall()

#create paddle
paddle=paddle()




#creeaza bila si o aseaza deasupra paletei
ball=ball(paddle.x+(paddle.width//2),paddle.y-paddle.height)




#aici creez o fereastra cu dimensiunea de 600x600 de pixeli
screen=pygame.display.set_mode((600,600))



background=pygame.image.load('background.png')
#title and icon
pygame.display.set_caption("Break-it Game")
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)




running=True
#clock=how fast screen updates
clock=pygame.time.Clock()

pause_state=False

def display_text(live_ball):
    if live_ball==False:
    
        
        if game_over==1:
            update_highscore(score)
            font=pygame.font.Font(None,34)
            text=font.render("Felicitari! Ai castigat",1,Alb)
            screen.blit(text,(100,300))
            text=font.render("Apasa SPACE pentru a juca din nou!",1,Alb)
            screen.blit(text,(100,350))
            #aici fac afisarea in cazul in care pierdem
        elif game_over==-1:
            mixer.music.stop()
            gameoverSound=mixer.Sound("gameOver.mp3")
            gameoverSound.play() 
            font=pygame.font.Font(None,34)
            text=font.render("Ai pierdut...",1,Alb)
            screen.blit(text,(225,300))
            text=font.render("Apasa SPACE pentru a juca din nou!",1,Alb)
            screen.blit(text,(100,350))
            gameoverSound.stop()
    font = pygame.font.Font(None, 24)
  
show_rules = True
rules_page = pygame.Surface((600, 600))  # Creează o suprafață pentru pagina cu reguli
background2=pygame.image.load("background2.png")
font = pygame.font.Font(None, 24)
text = font.render("Regulile jocului", True, Negru)
text_rect = text.get_rect(center=(300, 300))  # Afișează textul în centrul suprafeței
rules_page.blit(text, text_rect)



        
while running:
    screen.blit(background,(0,0))
    #desenez instanta wall si paddle
    wall.draw_wall(screen)

    paddle.draw(screen)
   
    ball.draw()


    #creez chenar nr gloante ramase
    font =pygame.font.Font(None, 34)
    text=font.render("Bullets: " + str(nr_bullet)+"/5", True, Alb)
    text_rect=text.get_rect()
    text_rect.bottomright=(570, 550)
    
    screen.blit(text, text_rect) 
   

    #coada de evenimente:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            
        if event.type==pygame.KEYDOWN:
            show_rules=False
            if event.key==pygame.K_x:
                running=False
            if event.key==pygame.K_p:
                if pause_state==False:
                    pause_state=True
                else:
                    pause_state=False

            if event.key==pygame.K_UP:
                #creste viteza cu 1
                speed_state+=1
                speed_ok=True
            
                ball.reset(ball_x,ball_y)
            if event.key==pygame.K_DOWN and speed_state>=1:
                #scade viteza cu 1
                speed_state-=1
                ball.reset(ball_x,ball_y)
            
            if event.key==pygame.K_f:
                #trage un glont
                if bullet_state is "ready" and nr_bullet<5 and live_ball==True and (special_state==1 or special_state==2 or special_state==3):
                    fire_bullet(bulletX,bulletY)
                    nr_bullet+=1
   

    if show_rules:
        rules_page.blit(background2, (0,0))
        font=pygame.font.Font(None, 26)
        text=font.render("Regulile jocului:", True, Alb)
        text_rect=text.get_rect(center=(300,100))
        rules_page.blit(text, text_rect)
        text=font.render("1)Apasati orice tasta pentru a incepe jocul", True, Alb)
        text_rect=text.get_rect(center=(300,150))
        rules_page.blit(text, text_rect)
        text=font.render("2)Apasati tasta P pentru a pune pauza jocului", True, Alb)
        text_rect=text.get_rect(center=(300,200))
        rules_page.blit(text, text_rect)
        text=font.render("3)Apasati tasta F pentru a trage cu cele 5 gloante", True, Alb)
        text_rect=text.get_rect(center=(300,250))
        rules_page.blit(text, text_rect)
        text=font.render("4)Daca spargeti o caramida verde primiti bonusuri precum: ", True, Alb)
        text_rect=text.get_rect(center=(300,300))
        rules_page.blit(text, text_rect)
        text=font.render(" efect exploziv,marirea paletei, posibilitatea de a trage cu gloante", True, Alb)
        text_rect=text.get_rect(center=(300,350))
        rules_page.blit(text, text_rect)
        text=font.render("5)Apasati X pentru a inchide jocul", True, Alb)
        text_rect=text.get_rect(center=(300,400))
        rules_page.blit(text, text_rect)
        
        screen.blit(rules_page, (0, 0))




    if pause_state==True and live_ball==True:
        font=pygame.font.Font(None,34)
        text=font.render("Joc intrerupt!",1,Alb)
        screen.blit(text,(120,300))
        text=font.render("Apasa P pentru a relua jocul.",1,Alb)
        screen.blit(text,(120,350))
        text=font.render("Scorul dumneavoastra pana acum este "+ str(score),1,Alb)
        screen.blit(text,(120,250))




    
    if pause_state==False:
        if live_ball==True:
            bulletX=paddle.move(speed_state,special_state,bullet_state)
            game_over=ball.move()
            if game_over!=0:
                live_ball=False

   


    draw_score(screen)
    display_text(live_ball)


    key=pygame.key.get_pressed()
    
    #aici verific daca am apasat space si bila nu e in joc si resetez jocul 
    if key[pygame.K_SPACE]==True and live_ball==False :
        live_ball=True
        speed_state=0
        ball.reset(paddle.x+(paddle.width//2),paddle.y-paddle.height)
        paddle.reset()
        wall.create_wall()
        score=0
        update_highscore(score)
        special_state=0
        nr_bullet=0
        mixer.music.play(-1) 



    #aici afisez pe ecram scorul utilizatorului
    font=pygame.font.Font(None,34)
    text=font.render("Score: "+str(score),1,Alb)
    screen.blit(text,(20,570))

    col_count=0
    row_count=0
    for row in range(6):
     for col in range(8):
        collision = isCollision(bulletX, bulletY, wall.width * col, wall.height * row)
        if collision:
            explosionSound = mixer.Sound("laser.wav")
            explosionSound.play()
            bulletY = 575
            for i in range(row, -1, -1):
                if wall.blocks[i][col][1] != 0:  # Verifică dacă caramida nu este deja marcată ca distrusă
                    wall.blocks[i][col][0] = (0, 0, 0, 0)
                    wall.blocks[i][col][1] = 0  # Marchează caramida ca distrusă
                    bullet_state = "ready"
                    score += 1
                    break




    if bullet_state is "fire":
        #trage
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change



    if(bulletY<=0):
        bullet_state="ready"
        bulletY=575
    


    pygame.display.update()
    #200 FPS
    clock.tick(200)
pygame.quit()
