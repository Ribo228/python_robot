import pygame
import random

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW=(255,255,0)
BLACK =(0,0,0)

WIDTH = 500
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Ribo's first game, have fun!")

clock = pygame.time.Clock()
background_img = pygame.image.load("background1.png")
play_img = pygame.image.load("fighter2.png")
play_mini_img = pygame.transform.scale(play_img,(20,20))
play_mini_img.set_colorkey(WHITE)
pygame.display.set_icon(play_mini_img)
rock_img = pygame.image.load("stone6.png")
bullet_img = pygame.image.load("bullet.png")

font_name = pygame.font.match_font("arial")
def draw_text(surf, text,size, x,y):
    font=pygame.font.Font(font_name,size)
    text_surface = font.render(text,True,WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface,text_rect)

def new_rock():
    r = Rock()
    all_sprites.add(r)
    rocks.add(r)
def draw_health(surf,hp,x,y):
    if hp < 0:
        hp = 0
    BAR_lENGTH =100
    BAR_HEIGHT = 10
    fill = hp/100*BAR_lENGTH
    outline_rect = pygame.Rect(x,y,BAR_lENGTH,BAR_HEIGHT)
    fill_rect = pygame.Rect(x,y,fill,BAR_HEIGHT)
    pygame.draw.rect(surf,GREEN,fill_rect)
    pygame.draw.rect(surf,WHITE,outline_rect,2)
def draw_lives(surf,lives,img,x,y):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x+25*i
        img_rect.y=y
        surf.blit(img,img_rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(play_img,(50,38))
        self.image.set_colorkey(WHITE)
        self.rect=self.image.get_rect()
        self.rect.centerx = (WIDTH/2)
        self.rect.bottom = HEIGHT-5
        self.speedx = 4
        self.health =100
        self.lives = 3
        self.hidden = False
        self.hide_time = 0
    def update(self):
        if self.hidden and pygame.time.get_ticks()-self.hide_time>1000:
            self.hidden = False
            self.rect.centerx = (WIDTH / 2)
            self.rect.bottom = HEIGHT -                 5
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    def shoot(self):
        if not(self.hidden):
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
    def hide(self):
        self.hidden = True
        self.hide_time = pygame.time.get_ticks()
        self.rect.center = (WIDTH/2, HEIGHT+500)

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(rock_img, (30, 25))
        self.image.set_colorkey(WHITE)
        self.rect=self.image.get_rect()
        self.rect.x = random.randrange(0,WIDTH-self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(2,10)
        self.speedx = random.randrange(-3, 3)
        self.rot_degree = 3
    def rotate(self):
        self.image = pygame.transform.rotate(self.image,self.rot_degree)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT or self.rect.left>WIDTH or self.rect.right<0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 10)
            self.speedx = random.randrange(-3, 3)
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bullet_img, (6, 8))
        self.rect=self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

all_sprites= pygame.sprite.Group()
rocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
rock = Rock()
all_sprites.add(rock)
for i in range(8):
    new_rock()
score = 0

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()
    hits = pygame.sprite.groupcollide(rocks,bullets,True,True)
    for hit in hits:
        score += 1
        new_rock()
    hits=pygame.sprite.spritecollide(player,rocks,True)
    for hit in hits:
        new_rock()
        player.health -= 10
        if player.health <=0:
            player.lives -=1
            player.health = 100
            player.hide()
    if player.lives ==0:
        running = False

    screen.fill(BLACK)
    screen.blit(background_img,(0,0))
    all_sprites.draw(screen)
    draw_text(screen,str(score),15,WIDTH/2,10)
    draw_health(screen,player.health,5,15)
    draw_lives(screen,player.lives,play_mini_img,WIDTH-90,15)
    pygame.display.update()

pygame.quit()