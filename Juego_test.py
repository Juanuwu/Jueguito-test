import pygame
import os
import time
import random

pygame.init()

#configuracion de la ventana

win = pygame.display.set_mode((700,500))
pygame.display.set_caption("uwu")
clock = pygame.time.Clock()
dirname = os.path.dirname(__file__)

#imagenes cargadas pero bien

walkRight =[pygame.image.load(os.path.join(dirname, 'Game/R1.png')), pygame.image.load(os.path.join(dirname, 'Game/R2.png')), pygame.image.load(os.path.join(dirname, 'Game/R3.png')),pygame.image.load(os.path.join(dirname, 'Game/R4.png')),pygame.image.load(os.path.join(dirname, 'Game/R5.png')),pygame.image.load(os.path.join(dirname, 'Game/R6.png')),pygame.image.load(os.path.join(dirname, 'Game/R7.png')),pygame.image.load(os.path.join(dirname, 'Game/R8.png')),pygame.image.load(os.path.join(dirname, 'Game/R9.png'))]
walkLeft = [pygame.image.load(os.path.join(dirname, 'Game/L1.png')), pygame.image.load(os.path.join(dirname, 'Game/L2.png')), pygame.image.load(os.path.join(dirname, 'Game/L3.png')),pygame.image.load(os.path.join(dirname, 'Game/L4.png')),pygame.image.load(os.path.join(dirname, 'Game/L5.png')),pygame.image.load(os.path.join(dirname, 'Game/L6.png')),pygame.image.load(os.path.join(dirname, 'Game/L7.png')),pygame.image.load(os.path.join(dirname, 'Game/L8.png')),pygame.image.load(os.path.join(dirname, 'Game/L9.png'))]
char = pygame.image.load(os.path.join(dirname, 'Game/standing.png'))
bg = pygame.image.load(os.path.join(dirname, 'Game/coso.jpg'))
#enemieWalkRight =[pygame.image.load(os.path.join(dirname, 'Game/R1E.png')), pygame.image.load(os.path.join(dirname, 'Game/R2E.png')), pygame.image.load(os.path.join(dirname, 'Game/R3E.png')),pygame.image.load(os.path.join(dirname, 'Game/R4E.png')),pygame.image.load(os.path.join(dirname, 'Game/R5E.png')),pygame.image.load(os.path.join(dirname, 'Game/R6E.png')),pygame.image.load(os.path.join(dirname, 'Game/R7E.png')),pygame.image.load(os.path.join(dirname, 'Game/R8E.png')),pygame.image.load(os.path.join(dirname, 'Game/R9E.png'))]
elefanteRight = [pygame.image.load(os.path.join(dirname, 'Game/L1E.png')), pygame.image.load(os.path.join(dirname, 'Game/L2E.png')), pygame.image.load(os.path.join(dirname, 'Game/L3E.png')),pygame.image.load(os.path.join(dirname, 'Game/L4E.png')),pygame.image.load(os.path.join(dirname, 'Game/L5E.png')),pygame.image.load(os.path.join(dirname, 'Game/L6E.png')),pygame.image.load(os.path.join(dirname, 'Game/L7E.png')),pygame.image.load(os.path.join(dirname, 'Game/L8E.png')),pygame.image.load(os.path.join(dirname, 'Game/L9E.png'))]
enemieWalkLeft = [pygame.image.load(os.path.join(dirname, 'Game/F1.png')), pygame.image.load(os.path.join(dirname, 'Game/F2.png')), pygame.image.load(os.path.join(dirname, 'Game/F3.png')),pygame.image.load(os.path.join(dirname, 'Game/F4.png')),pygame.image.load(os.path.join(dirname, 'Game/F5.png')),pygame.image.load(os.path.join(dirname, 'Game/F6.png')),pygame.image.load(os.path.join(dirname, 'Game/F7.png')),pygame.image.load(os.path.join(dirname, 'Game/F8.png')),pygame.image.load(os.path.join(dirname, 'Game/F9.png'))]
elefanteLeft = 0

class platform1():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x + 20, self.y, self.height,self.width)
        self.end = self.height -20

    def draw(self,win):
        pygame.draw.rect(win,(255,0,0),self.rect)


class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 8
        self.standing = True
        self.hitbox = (self.x , self.y, 28,60)
        self.rect = pygame.draw.rect(win,(255,0,0),self.hitbox,2)
        self.inGround = True
        self.vida = 25
        self.contador = 0
        self.final = pygame.Rect(200,200,64,64)
       
    def die(self):
        self.contador = 0
        del enemigos[:]
        self.x = 200
        self.y = 410
    


    def draw(self, uwu):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x,self.y))
            else:
                    win.blit(walkLeft[0], (self.x,self.y))
        self.hitbox = (self.x + 11, self.y, 28,60)
        pygame.draw.rect(win,(255,0,0),self.hitbox,2)


class enemi(object):
    def __init__(self,x,y,width,height):
        self.vida = 10
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.walkCount = 0
        self.vel = random.randint(1, 3)

        self.hitbox = (self.x + 16, self.y+2, 28,60)
        self.direccion = 2
        self.rect = pygame.draw.rect(win,(0,0,0),self.hitbox,2)


    def hit(self):
        print("hit")
        self.vida -= 2
        if self.vida <= 0:
            enemigos.remove(enemy)


    



    def draw(self,win):
            self.move(self.vel)
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
            if self.direccion == 1:
                win.blit(elefanteRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.direccion == -1:
                win.blit(enemieWalkLeft[self.walkCount // 3],(self.x, self.y))
                self.walkCount += 1
            elif self.direccion == 0:
                print("uwu")

            self.hitbox = (self.x + 16, self.y+2, 28,60)
            pygame.draw.rect(win,(255,0,0),self.hitbox,2)
    
    #funcion que hace que los enemigos te sigan, si tiene comentarios en ingles es probablemente porque me lo robe de por ahi
    def move(self, speed): # chase movement
        # Movement along x direction


        if self.direccion != 0:
            if self.x > man.x:
                    self.x -= speed
                    self.direccion = 1
            elif self.x < man.x:
                    self.x += speed
                    self.direccion = -1
        self.rect = pygame.Rect(self.x, self.y, self.height,self.width)


class enemigoPlat(enemi):
    def __init__(self,x,y,width,height):
        enemi.__init__(self,x,y,width,height)
        super(enemi,self).__init__()
        self.pathStart = platform.x
        self.pathEnd = platform.x +platform.end
        self.flag = 0
        self.y = platform.y -60
        
        
    def move(self, speed):
        if self.x <= self.pathEnd and self.flag ==  0:
            self.x += speed
            self.direccion = -1
        
        if self.x >= self.pathEnd:
            self.flag = 1
        
        if self.flag == 1:
            self.x -= speed
            self.direccion = 1
            if self.x <self.pathStart:
                self. flag = 0
        self.rect = pygame.Rect(self.x, self.y, self.height,self.width)

#lo que dice el puto nombre fabian no te puedo explicar todo la puta madre estamos grandes ya pibe

class proyectil():
    def __init__(self,x,y,radio,color, facing):
        self.x = int(x)
        self.y = int(y)
        self.radio = radio
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
        
        


    def draw(self,uwu):

            pygame.draw.circle(uwu, self.color, (self.x,self.y),self.radio)





def gravedad():

        man.y += 22


def gravedadTest():
    if  man.y < 410 and flag != 1 and man.isJump == False:
        gravedad()
    if man.y >410:
        man.y = 410
    if  man.y == 410:
        man.inGround = True

#funcion en la que se ponen todas las cosas que se quieren mostrar en la pantalla asi no es todo un quilombo
def redrawGameWindow():
    win.blit(bg, (0,0))
    if(man.vida >= 0):
        man.draw(win)
    elif keys[pygame.K_SPACE]:
        man.vida = 25
        man.die()

    for bullet in bullets:
        bullet.draw(win)
    for enemy in enemigos:
        enemy.draw(win)
    for platform in platforms:
        platform.draw(win)
    pygame.draw.rect(win,(255,0,0),(0,0,man.vida*10,20,),0)
    pygame.display.update()



#aca estan los dos enemigos porque hay dos enemigos, BASTANTE SIMPLE
man = player(200, 410, 64,64)
flag = 0
run = True
shootLoop = 0
bullets = []
enemigos = []
platforms = []
nivel = 1

def levelCheck(dato):
    nivel = dato
    man.x = 200
    man.y = 410
    del enemigos[:]
    del platforms[:]
    man.contador = 0

    if(nivel == 1):
        
        enemigos.append(enemi(100,410,64,64))
        enemigos.append(enemi(80,410,64,64))
        
        platforms.append(platform1(300,400,30,200))
        platforms.append(platform1(550,300,30,200))
        platforms.append(platform1(200,200,30,200))
        platforms.append(platform1(500,200,30,64))

        
    
    elif(nivel == 2):
        
        
        
        a=platform1(100,350,30,200)
        b=platform1(300,200,30,200)
        c=platform1(550,200,30,200)
        platforms.append(a)
        platforms.append(b)
        platforms.append(c)
        man.final = pygame.Rect(550,200,64,64)
        man.contador = 0

    elif(nivel == 3):
        platforms.append(platform1(100,375,30,200))
        platforms.append(platform1(300,250,30,64))
        platforms.append(platform1(400,240,30,200))
        platforms.append(platform1(450,400,30,200))
        platforms.append(platform1(600,325,30,64))
        platforms.append(platform1(520,150,30,200))
        man.final = pygame.Rect(560,100,64,64)

        

    
levelCheck(nivel)

#empieza el loop principial, python no tiene main asi que usamos un while uwu
while run:

    clock.tick(27)
    #todo este choclo hasta la parte donde pone keys son las colisiones de las balas, despues hay que hacer que de menos asco y sacarlo de aca
    #if len(enemigos) <= 0:
        #enemigos.append(enemi(300,410,64,64))

    #determina si el personaje esta en una plataforma o en el piso, si no lo esta lo tira para abajo hasta que lo este, no se si esta es una forma
    #decente de hacerlo pero es la que se me ocurrio sin buscar un video en youtube, porque me dio paja
    gravedadTest()
    #esto se pone en uno cuando el personaje esta en una plataforma, hay que ponerle un nombre que no sea flag
    flag = 0

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:

            x, y = pygame.mouse.get_pos()
            platforms.append(platform1(x-50,y-10,30,60))
    #hay que encontrar una forma de hacer esto que no requiera dos millones de loops porque es una crotada y va a explotar todo buenas tardes
    #forma encontrada buenas tardes
    for platform in platforms:
        if platform.rect.colliderect(man.hitbox) and man.y < platform.y:
            man.y = platform.y -55
            man.inGround = True
            flag = 1
        if(man.contador < len(platforms)):
            enemigos.append(enemigoPlat(platform.x,410,64,64))
            man.contador+= 1
    #for enemy in enemigos:
        #man.colision(enemy)

    for bullet in bullets:
        if len(enemigos) > 0:
            for enemy in enemigos:
                if bullet.y + bullet.radio < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radio > enemy.hitbox[1]:
                    if bullet.x + bullet.radio > enemy.hitbox[0] and bullet.x - bullet.radio < enemy.hitbox[0] + enemy.hitbox[2]:
                        enemy.hit()

                        if len(bullets) > 0:
                            bullets.pop()


            #si las balas empiezan a hacer cosas raras el problema esta aca, pero ahora no me voy a molestar en cambiarlo
        if bullet.x < 700 and bullet.x > 0:
                bullet.x += bullet.vel

        else:
                bullets.pop(bullets.index(bullet))

    #cuando un enemigo se choca con el personaje, juan del futuro deja de llenar todo de fors pls te quiero no me lastimes
    for enemy in enemigos:
        if enemy.rect.colliderect(man .hitbox):
            man.vida -= 1
            print("oh no")
        #boton para disparar

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q] and shootLoop == 0:
        if man.left:
           facing = -1
        else:
          facing  = 1
        if len(bullets) < 50:
             bullets.append(proyectil(round(man.x + man.width // 2), round(man.y + man. height //2),5,(0,0,0), facing))
             shootLoop = 1

    #teclas para moverse
    if keys[pygame.K_LEFT]:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT]:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
    
    #esto es para pasar d enivel y tendria que estar en otro lado porque se me va a perder
    
    if man.final.colliderect(man.hitbox):
        nivel += 1
        levelCheck(nivel)
        
    
    
        #salto
    if not(man.isJump):
        if keys[pygame.K_SPACE] and man.inGround:
            man.isJump = True
            man.standing = True
            man.walkCount = 0
    else:
        if man.jumpCount >= -8:
            neg = 1


            if man.jumpCount < 0:
                    neg = -1

            if man.isJump:
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 8

    redrawGameWindow()
    man.inGround = False
    #bordes
    if man.x > 700:
        man.x = -40
    if man.x < -50:
        man.x = 700


pygame.quit()

