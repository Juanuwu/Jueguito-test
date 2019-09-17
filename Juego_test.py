import pygame
pygame.init()
#configura la ventana
win = pygame.display.set_mode((700,500))
pygame.display.set_caption("uwu")
clock = pygame.time.Clock()

#cargar imágenes
walkRight =[pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\R1.png'), pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\R2.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\R3.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\R4.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\R5.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\R6.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\R7.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\R8.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\R9.png')]
walkLeft =[pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\L1.png'), pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\L2.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\L3.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\L4.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\L5.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\L6.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\L7.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\L8.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\L9.png')]
char = pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\standing.png')
bg = pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\coso.jpg')                                                                                                                                                                                                                                                                                                                                                              
enemieWalkRight =[pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\R1E.png'), pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\R2E.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\R3E.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\R4E.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\R5E.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\R6E.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\R7E.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\R8E.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\R9E.png')]
enemieWalkLeft = [pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\L1E.png'), pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\L2E.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\L3E.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\L4E.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\L5E.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\L6E.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\L7E.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\L8E.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\L9E.png')]
elefanteRight = [pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\F1.png'), pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\F2.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\F3.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\F4.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\F5.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\F6.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\F7.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\F8.png'),pygame.image.load('E:\Juan\Documents\Documentos\Python\Juego test\Game\F9.png')]
#clases con los atributos de el personaje principal y el enemigo
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
        self.jumpCount = 7
        self.standing = True
        self.hitbox = (self.x + 20, self.y, 28,60)
    #funcion que define para qué lado se está caminante y dibuja al personaje en la pantalla
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
man = player(200, 410, 64,64)
class enemy:
    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walkCount = 0
        self.vel = 3
        self.path = [self.x, self.end]
        self.hitbox = (self.x + 16, self.y+2, 28,60)

    def hit(self):
        print("hit")
        
        

    
    def draw(self,win):
            self.move()
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(elefanteRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(enemieWalkLeft[self.walkCount // 3],(self.x, self.y))
                self.walkCount += 1
            self.hitbox = (self.x + 16, self.y+2, 28,60)
            pygame.draw.rect(win,(255,0,0),self.hitbox,2)
    
    #funcion que hace que los enemigos te sigan, si tiene comentarios en inglés es probablemente porque me lo robé de por ahí
    def move(self, speed=1): # chase movement
        # Movement along x direction
        
        if self.x > man.x:
                self.x -= speed
        elif self.x < man.x:
                self.x += speed
            # Movement along y direction
        if self.y < man.y:
                self.y += speed
        elif self.y > man.y:
                self.y -= speed
         
        
#lo que dice el puto nombre fabián no te puedo explicar todo la puta madre estamos grandes ya pibe
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
            
        

#función en la que se ponen todas las cosas que se quieren mostrar en la pantalla así no es todo un quilombo
def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)    
    for bullet in bullets:
        bullet.draw(win)
    enemy1.draw(win)
    enemy2.draw(win)
    pygame.display.update()



#acá están los dos enemigos porque hay dos enemigos, BASTANTE SIMPLE
enemy1 = enemy(100,410,64,64, 450)
enemy2 = enemy(500,410,64,64, 450)
run = True
shootLoop = 0
bullets = []
#empieza el loop principial, python no tiene main así que usamos un while uwu
while run:
    
    clock.tick(27)
    #todo este choclo hasta la parte donde pone keys son las colisiones de las balas, después hay que hacer que de menos asco y sacarlo de aca
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #hay que encontrar una forma de hacer esto que no requiera dos millones de loops porque es una crotada y va a explotar todo buenas tardes
    for bullet in bullets:
        if bullet.y + bullet.radio < enemy1.hitbox[1] + enemy1.hitbox[3] and bullet.y + bullet.radio > enemy1.hitbox[1]:
            if bullet.x + bullet.radio > enemy1.hitbox[0] and bullet.x - bullet.radio < enemy1.hitbox[0] + enemy1.hitbox[2]:
                enemy1.hit()
                bullets.pop(bullets.index(bullet))
    for bullet in bullets:
        if bullet.y + bullet.radio < enemy2.hitbox[1] + enemy2.hitbox[3] and bullet.y + bullet.radio > enemy2.hitbox[1]:
            if bullet.x + bullet.radio > enemy2.hitbox[0] and bullet.x - bullet.radio < enemy2.hitbox[0] + enemy2.hitbox[2]:
                enemy2.hit()
                bullets.pop(bullets.index(bullet))
        if bullet.x < 700 and bullet.x > 0:
            bullet.x += bullet.vel
    
        else:
            bullets.pop(bullets.index(bullet))

    #boton para disparar
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q] and shootLoop == 0:
        if man.left:
           facing = -1
        else:
          facing  = 1
        if len(bullets) < 100:
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
    #salto
    if not(man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.standing = True
            man.walkCount = 0
    else:
        if man.jumpCount >= -7:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 7
            
    redrawGameWindow()
#coso que hace que si te vas por un lado salgas por el otro
    #bordes
    if man.x > 700:
        man.x = -40
    if man.x < -50:
        man.x = 700
        
    
pygame.quit()
