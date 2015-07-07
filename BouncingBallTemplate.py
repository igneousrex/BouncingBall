import sys, pygame

size = width, height = 1200, 700

PLAYER_SPEED = 5
VECTOR_X = 0
VECTOR_Y = 1

class Sprite():
    def __init__(self, file, speed):
        self.file = file
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.rect.y = height - self.rect.height
        self.speed = speed
        self.show = True

    def move(self, screen):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[VECTOR_X] = -self.speed[VECTOR_X]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[VECTOR_Y] = -self.speed[VECTOR_Y]

        if self.show:
            screen.blit(self.image, self.rect)

class Player(Sprite):
    def moveleft(self):
        self.speed[VECTOR_X] = -PLAYER_SPEED

    def stop_left(self):
        if self.speed[VECTOR_X] < 0:
            self.speed[VECTOR_X] = 0

    def stop_right(self):
        if self.speed[VECTOR_X] > 0:
            self.speed[VECTOR_X] = 0

    def moveright(self):
        self.speed[VECTOR_X] = PLAYER_SPEED

    def move(self, screen):
        if (self.speed[VECTOR_X] < 0 and self.rect.left + self.speed[VECTOR_X] > 0) or (self.speed[VECTOR_X] > 0 and self.rect.right + self.speed[VECTOR_X] < width):
            self.rect = self.rect.move(self.speed)

        screen.blit(self.image, self.rect)

class Missile(Sprite):
    def move(self, screen):
        self.rect = self.rect.move(self.speed)
        if (self.rect.top < 1) or (pygame.sprite.collide_mask(self, testEnemy)):
            self.show = False

        if self.show:
            screen.blit(self.image, self.rect)

class Enemy(Sprite):
    def move(self, screen):
        self.rect = self.rect.move(self.speed)

        if pygame.sprite.collide_mask(self, missile):
            self.show = False

        if self.show:
            screen.blit(self.image, self.rect)

background_image = pygame.image.load("MoutainsBackground.JPG")

pygame.init()


black = 0, 0, 0

screen = pygame.display.set_mode(size)


#new_balls = [Sprite("ball.png", [2, 2]), Sprite("ball2.PNG", [3, 3]), Sprite("ball3.GIF", [1, 1])]

space_ship = Player("SpaceShip.png", [0, 0])

missile = Missile("Missile.png", [0, -20])

testEnemy = Enemy("SpaceInvaders1.png", [0, 0])

testEnemy.show = True

testEnemy.rect.x = 100
testEnemy.rect.y = 10

testEnemy.mask = pygame.mask.from_surface(testEnemy.image)
missile.mask = pygame.mask.from_surface(missile.image)

missile.show = False

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                space_ship.moveleft()
            if event.key == pygame.K_RIGHT:
                space_ship.moveright()

            if event.key == pygame.K_SPACE:
                missile.show = True
                missile.rect.x = space_ship.rect.x + space_ship.rect.width /2 - missile.rect.width / 2
                missile.rect.y = height - missile.rect.height
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                space_ship.stop_left()
            if event.key == pygame.K_RIGHT:
                space_ship.stop_right()

    screen.blit(background_image, [0, 0])
    #screen.fill(black)


   # for b in new_balls:

    missile.move(screen)

    space_ship.move(screen)

    testEnemy.move(screen)

    pygame.display.flip()
