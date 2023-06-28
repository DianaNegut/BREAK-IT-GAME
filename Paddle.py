# import pygame
# from pygame.locals import *


# Gri=(128,128,128)
# Orange=(255,69,0)
# Maro=(139,69,19)
# Alb=(255,255,255)
# Verde=(0,255,0)
# Galben=(255,255,0)
# Negru=(0,0,0)
# Albastru = (0, 0, 255)
# class paddle():
#     def __init__(self):
#         self.reset()
#         self.bigger=False
#         self.smaller=False
#     #gestionam miscarea si starea paletei in functie de tastele apasate
#     def move(self,speed_state,special_state,bullet_state):
#         self.direction=0
#         #global speed_state

#         if speed_state==1:
#             self.speed=3
#         if speed_state==2:
#             self.speed=6
        
#         global bulletX
#         #daca glontul este pregatit calculam pozitia ca mijlocului paletei pe axa x

#         if bullet_state is "ready":
#             bulletX=(self.rect.left+self.rect.right)/2

#         #daca paleta nu e extinsa deja si nu are alte stari speciale, marim latimea
#         if special_state==1 and self.bigger==False:
#             self.width=200
#             #actualizam dreptunghiul pt noua dimensiune
#             self.rect=Rect(self.x,self.y,self.width,self.height)
#             self.bigger=True
#         #daca paleta era deja marita, o micsoram
#         elif special_state==1 and self.smaller==True:
#              self.width = 200
#              self.rect = Rect(self.x, self.y, self.width, self.height)
#              self.bigger = True
#              self.smaller = False
     

#         if special_state>=2 and self.smaller==False:
#             self.width=100
#             #actualizam drreptunghiul pt noua dimensiune
#             self.rect=Rect(self.x,self.y,self.width,self.height)
#             self.smaller=True
        
        
#         key=pygame.key.get_pressed()
#         #daca apasam tasta stanga, scade viteza
#         if key[pygame.K_LEFT] and self.rect.left>0:
#             self.rect.x-=self.speed
            
#         #daca apasam tasta dreapta, creste viteza
#         if key[pygame.K_RIGHT] and self.rect.right<600:
#             self.rect.x+=self.speed
            
#         return bulletX

#     def draw(self,screen):
#         pygame.draw.rect(screen,Albastru,self.rect)   
#         pygame.draw.rect(screen,Alb,self.rect,4)
    
#     def reset(self):
#         self.height=20
#         self.width=100
#         self.bigger=False
#         self.smaller=False
#         self.x=290
#         self.y=575
#         self.speed=3
#         self.rect=Rect(self.x,self.y,self.width,self.height)
import pygame
from pygame.locals import *


Gri=(128,128,128)
Orange=(255,69,0)
Maro=(139,69,19)
Alb=(255,255,255)
Verde=(0,255,0)
Galben=(255,255,0)
Negru=(0,0,0)
Albastru = (0, 0, 255)

class paddle():
    def __init__(self):
        self.reset()
        self.bigger = False
        self.smaller = False
    
    def move(self, speed_state, special_state, bullet_state):
        self.direction = 0

        if speed_state == 1:
            self.speed = 3
        if speed_state == 2:
            self.speed = 6
        
        global bulletX

        if bullet_state == "ready":
            bulletX = (self.rect.left + self.rect.right) / 2

        if special_state == 1 and self.bigger == False:
            self.width = 200
            self.rect = Rect(self.x, self.y, self.width, self.height)
            self.bigger = True
        elif special_state == 1 and self.smaller == True:
            self.width = 200
            self.rect = Rect(self.x, self.y, self.width, self.height)
            self.bigger = True
            self.smaller = False

        if special_state >= 2 and self.smaller == False:
            self.width = 100
            self.rect = Rect(self.x, self.y, self.width, self.height)
            self.smaller = True
        
        
        key = pygame.key.get_pressed()
        
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        
        if key[pygame.K_RIGHT] and self.rect.right < 600:
            self.rect.x += self.speed
        
        return bulletX

    def draw(self, screen):
        pygame.draw.rect(screen, Negru, self.rect)   
        pygame.draw.rect(screen, Alb, self.rect, 4)
    
    def reset(self):
        self.height = 20
        self.bigger = False
        self.smaller = False

        if self.bigger:
            diff = self.width - 100
            self.x -= diff // 2

        self.width = 100
        self.x = 290
        self.y = 575
        self.speed = 3
        self.rect = Rect(self.x, self.y, self.width, self.height)
