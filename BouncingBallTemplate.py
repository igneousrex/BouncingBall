import sys, pygame

size = width, height = 1200, 700

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
            self.speed[0] = -self.speed[0]
        if self.ballrect.top < 0 or self.ballrect.bottom > height:
            self.speed[1] = -self.speed[1]

        if self.show:
            screen.blit(self.image, self.ballrect)

class Player(Sprite):
    def moveleft(self):
        if self.speed[0] > 0:
            self.speed[0] = -self.speed[0]

    def moveright(self):
        if self.speed[0] < 0:
            self.speed[0] = -self.speed[0]

    def move(self, screen):
        if (self.speed[0] < 0 and self.ballrect.left + self.speed[0] > 0) or (self.speed[0] > 0 and self.ballrect.right + self.speed[0] < width):
            self.ballrect = self.ballrect.move(self.speed)

        screen.blit(self.image, self.ballrect)

class Missile(Sprite):


    def move(self, screen):
        self.ballrect = self.ballrect.move(self.speed)
        if self.ballrect.top < 1:
            self.show = False

        if self.show:
            screen.blit(self.image, self.ballrect)


        
      


background_image = pygame.image.load("MoutainsBackground.JPG")

pygame.init()


black = 0, 0, 0

screen = pygame.display.set_mode(size)


#new_balls = [Sprite("ball.png", [2, 2]), Sprite("ball2.PNG", [3, 3]), Sprite("ball3.GIF", [1, 1])] 

sapce_ship = Player("SpaceShip.PNG", [3, 0])

missile = Missile("Missile.PNG", [0, -14])

missile.show = False 

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                sapce_ship.moveleft()
            if event.key == pygame.K_RIGHT:
                sapce_ship.moveright()

            if event.key == pygame.K_SPACE:
                missile.show = True 
                missile.ballrect.x = sapce_ship.ballrect.x + sapce_ship.ballrect.width /2 - missile.ballrect.width / 2
                missile.ballrect.y = height - missile.ballrect.height
            

    screen.blit(background_image, [0, 0])
    #screen.fill(black)


   # for b in new_balls:
    
    missile.move(screen)
   
    sapce_ship.move(screen)

    pygame.display.flip()