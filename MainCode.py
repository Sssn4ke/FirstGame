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

Coords = [0] * 2

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
        # global X_player
        # global Y_player
        Coords[0] = self.rect.x
        Coords[1] = self.rect.y
        # Mob.update(self, Coords)



# player_coord = Player()
# X_player_coord = player_coord.X_player
# Y_player_coord = player_coord.Y_player
# print(X_player_coord, Y_player_coord)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 50))
        self.image.set_colorkey(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, 100)
        self.speedx = 4
        self.speedy = 4


    # def update(self):
    #     if (self.rect.x < 500):
    #         self.rect.x += self.speedx
    #     else:
    #         self.rect.x -= self.speedx
    #     if (self.rect.y < 500):
    #         self.rect.y += self.speedy
    #     else:
    #         self.rect.y -= self.speedy

    def update(self):
        X_player = Coords[0]
        Y_player = Coords[1]

        #while (self.rect.x != X_player or self.rect.y != Y_player):
        if (abs(X_player - self.rect.x) < abs(Y_player - self.rect.y)):
            if (X_player < self.rect.x):
                self.rect.x -= self.speedx
            else:
                self.rect.x += self.speedx

        if (abs(X_player - self.rect.x) > abs(Y_player - self.rect.y)):
            if (Y_player < self.rect.y):
                self.rect.y -= self.speedy
            else:
                self.rect.y += self.speedy





class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()


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


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(3):
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




