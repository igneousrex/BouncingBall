import sys, pygame

size = width, height = 1200, 700

class Sprite():
    def __init__(self, file, speed):
        self.file = file
        self.image = pygame.image.load(file)
        self.ballrect = self.image.get_rect()
        self.ballrect.y = height - self.ballrect.height
        self.speed = speed

    def move(self, screen):
        self.ballrect = self.ballrect.move(self.speed)
        if self.ballrect.left < 0 or self.ballrect.right > width:
            self.speed[0] = -self.speed[0]
        if self.ballrect.top < 0 or self.ballrect.bottom > height:
            self.speed[1] = -self.speed[1]
        screen.blit(self.image, self.ballrect)

pygame.init()



black = 0, 0, 0

screen = pygame.display.set_mode(size)

new_balls = [Sprite("ball5.JPG", [5, 5]), Sprite("ball.png", [2, 2]), Sprite("ball2.PNG", [3, 3]), Sprite("ball3.GIF", [1, 1]), Sprite("Ball4.PNG", [4, 4])] 

sapce_ship = Sprite("SpaceShip.PNG", [3, 0])

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)

    sapce_ship.move(screen)

    for b in new_balls:
        b.move(screen)
   
    pygame.display.flip()