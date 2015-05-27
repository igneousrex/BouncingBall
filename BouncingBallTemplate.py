import sys, pygame


class Ball():
    def __init__(self, file, speed):
        self.file = file
        self.image = pygame.image.load(file)
        self.ballrect = self.image.get_rect()
        self.speed = speed

    def move(self):
        self.ballrect = self.ballrect.move(self.speed)
        if self.ballrect.left < 0 or self.ballrect.right > width:
            self.speed[0] = -self.speed[0]
        if self.ballrect.top < 0 or self.ballrect.bottom > height:
            self.speed[1] = -self.speed[1]


pygame.init()

size = width, height = 1200, 700

speeds = [[2, 2], [3, 3], [1, 1], [4, 4]]

black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.PNG")
ballrect = ball.get_rect()

ball2 = pygame.image.load("ball2.PNG")
ballrect2 = ball2.get_rect()

ball3 = pygame.image.load("ball3.GIF")
ballrect3 = ball3.get_rect()

ball4 = pygame.image.load("Ball4.PNG")
ballrect4 = ball4.get_rect()

balls = [ball, ball2, ball3, ball4]

ballrects = [ballrect, ballrect2, ballrect3, ballrect4]

ball5 = Ball("ball5.JPG", [5, 5])

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)

    for i in range(len(balls)):

        ballrects[i] = ballrects[i].move(speeds[i])
        if ballrects[i].left < 0 or ballrects[i].right > width:
            speeds[i][0] = -speeds[i][0]
        if ballrects[i].top < 0 or ballrects[i].bottom > height:
            speeds[i][1] = -speeds[i][1]

        screen.blit(balls[i], ballrects[i])
    

    ball5.move()
    screen.blit(ball5.image, ball5.ballrect)

    pygame.display.flip()


