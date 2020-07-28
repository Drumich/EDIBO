import pygame


pygame.init()

win = pygame.display.set_mode((1280,720))

pygame.display.set_caption("Hello")

x = 50
y = 550
height = 50
width = 50
vel = 5

bg = pygame.image.load("a.jpg")

screen = 500

isJump = False
jumpCount = 10

run = True








while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screen - width:
        x += vel

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount <= 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.blit(bg, (0,0))
    pygame.draw.rect(win , (0,0,0) , (x, y, width, height))
    pygame.display.update()




pygame.quit()
