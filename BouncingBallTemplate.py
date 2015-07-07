import sys, pygame

size = width, height = 1200, 700

PLAYER_SPEED = 5
VECTOR_X = 0
VECTOR_Y = 1

class Sprite():
    def __init__(self, file, speed):
        self.file = file
        self.image = pygame.image.load(file)
        self.ballrect = self.image.get_rect()
        self.ballrect.y = height - self.ballrect.height
        self.speed = speed
        self.show = True

    def move(self, screen):
        self.ballrect = self.ballrect.move(self.speed)
        if self.ballrect.left < 0 or self.ballrect.right > width:
            self.speed[VECTOR_X] = -self.speed[VECTOR_X]
        if self.ballrect.top < 0 or self.ballrect.bottom > height:
            self.speed[VECTOR_Y] = -self.speed[VECTOR_Y]

        if self.show:
            screen.blit(self.image, self.ballrect)

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
        if (self.speed[VECTOR_X] < 0 and self.ballrect.left + self.speed[VECTOR_X] > 0) or (self.speed[VECTOR_X] > 0 and self.ballrect.right + self.speed[VECTOR_X] < width):
            self.ballrect = self.ballrect.move(self.speed)

        screen.blit(self.image, self.ballrect)

class Missile(Sprite):
    def move(self, screen):
        self.ballrect = self.ballrect.move(self.speed)
        if self.ballrect.top < 1:
            self.show = False

        if self.show:
            screen.blit(self.image, self.ballrect)

class Enemy(Sprite):
    def move(self, screen):
        self.ballrect = self.ballrect.move(self.speed)

        if self.show:
            screen.blit(self.image, self.ballrect)

background_image = pygame.image.load("MoutainsBackground.JPG")

pygame.init()


black = 0, 0, 0

screen = pygame.display.set_mode(size)


#new_balls = [Sprite("ball.png", [2, 2]), Sprite("ball2.PNG", [3, 3]), Sprite("ball3.GIF", [1, 1])]

space_ship = Player("SpaceShip.png", [0, 0])

missile = Missile("Missile.png", [0, -20])

testEnemy = Enemy("SpaceInvaders1.png", [0, 0])

words = ["cat", "window", "thing"]

for w in words:
    print w

testEnemy.show = True

testEnemy.ballrect.x = 10
testEnemy.ballrect.y = 10

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
                missile.ballrect.x = space_ship.ballrect.x + space_ship.ballrect.width /2 - missile.ballrect.width / 2
                missile.ballrect.y = height - missile.ballrect.height
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
