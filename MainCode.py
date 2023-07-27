import pygame
import random

WIDTH = 650
HEIGHT = 650
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (122, 177, 230)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 50))
        self.image = image_player1
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -8
            self.image = image_player4
        if keystate[pygame.K_d]:
            self.speedx = 8
            self.image = image_player2
        self.rect.x += self.speedx

        if keystate[pygame.K_w]:
            self.speedy = -8
            self.image = image_player1
        if keystate[pygame.K_s]:
            self.speedy = 8
            self.image = image_player3
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.left = 0
        if self.rect.left <0:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.bottom = HEIGHT
        if self.rect.bottom > HEIGHT:
            self.rect.top = 0

        self.image.set_colorkey(BLACK)
        global X_player
        global Y_player
        X_player = self.rect.x
        Y_player = self.rect.y

    def get_coords(self):
        return (X_player, Y_player)





class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 60))
        self.image = image_bot3
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, 100)
        self.speedx = 4
        self.speedy = 4




    def update(self):

        Player.get_coords(self)

        #while (self.rect.x != X_player or self.rect.y != Y_player):
        if (X_player == self.rect.x or Y_player == self.rect.y):
            if (X_player == self.rect.x and Y_player - self.rect.y > 0):
                self.image = image_bot3
            elif (X_player == self.rect.x and Y_player - self.rect.y < 0):
                self.image = image_bot1
            elif (Y_player == self.rect.y and X_player - self.rect.x > 0):
                self.image = image_bot2
            elif (Y_player == self.rect.y and X_player - self.rect.x < 0):
                self.image = image_bot4
        elif (X_player != self.rect.x or Y_player != self.rect.y):
            if (abs(X_player - self.rect.x) <= abs(Y_player - self.rect.y)):
                if (abs(X_player - self.rect.x) < 4):
                    if (X_player < self.rect.x):
                        self.rect.x -= abs(X_player - self.rect.x)
                        self.image = image_bot4
                    else:
                        self.rect.x += abs(X_player - self.rect.x)
                        self.image = image_bot2
                if (X_player < self.rect.x):
                    self.rect.x -= self.speedx
                    self.image = image_bot4
                else:
                    self.rect.x += self.speedx
                    self.image = image_bot2

            if (abs(X_player - self.rect.x) > abs(Y_player - self.rect.y)):
                if (abs(Y_player - self.rect.y) < 4):
                    if (Y_player < self.rect.y):
                        self.rect.y -= abs(Y_player - self.rect.y)
                        self.image = image_bot1
                    else:
                        self.rect.y += abs(Y_player - self.rect.y)
                        self.image = image_bot3
                if (Y_player < self.rect.y):
                    self.rect.y -= self.speedy
                    self.image = image_bot1
                else:
                    self.rect.y += self.speedy
                    self.image = image_bot3




        self.image.set_colorkey(BLACK)





class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

        self.speedx = 4
        self.speedy = 4




# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

image1 = pygame.image.load('player1.png').convert_alpha()
image_player1 = pygame.transform.scale(image1, (60, 80))
image2 = pygame.image.load('player2.png').convert_alpha()
image_player2 = pygame.transform.scale(image2, (60, 80))
image3 = pygame.image.load('player3.png').convert_alpha()
image_player3 = pygame.transform.scale(image3, (60, 80))
image4 = pygame.image.load('player4.png').convert_alpha()
image_player4 = pygame.transform.scale(image4, (60, 80))

image5 = pygame.image.load('bot1.png').convert_alpha()
image_bot1 = pygame.transform.scale(image5, (60, 80))
image6 = pygame.image.load('bot2.png').convert_alpha()
image_bot2 = pygame.transform.scale(image6, (60, 80))
image7 = pygame.image.load('bot3.png').convert_alpha()
image_bot3 = pygame.transform.scale(image7, (60, 80))
image8 = pygame.image.load('bot4.png').convert_alpha()
image_bot4 = pygame.transform.scale(image8, (60, 80))


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(1):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False


    # Обновление
    all_sprites.update()




    # Рендеринг
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()




